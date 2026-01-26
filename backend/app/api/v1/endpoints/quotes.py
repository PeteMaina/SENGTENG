"""
Quote Endpoints - Handle quote requests
"""
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlmodel import Session, select
from datetime import datetime
from uuid import UUID, uuid4
import os

from app.core import get_session
from app.models import Quote, User,  QuoteStatus
from app.schemas import QuoteCreate, QuoteResponse, QuoteUpdateStatus
from app.api.dependencies import get_current_user, get_current_superuser

router = APIRouter()


def generate_quote_number() -> str:
    """Generate a unique quote number"""
    import random
    import string
    return f"QT-{datetime.now().year}-{ ''.join(random.choices(string.digits, k=6))}"


@router.post("/", response_model=QuoteResponse, status_code=status.HTTP_201_CREATED)
async def create_quote(
    quote_data: QuoteCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user) if False else None
):
    """
    Submit a new quote request (authenticated or guest)
    """
    quote = Quote(
        **quote_data.model_dump(),
        quote_number=generate_quote_number(),
        user_id=current_user.id if current_user else None
    )
    
    session.add(quote)
    session.commit()
    session.refresh(quote)
    
    # TODO: Send email notification to admin
    
    return quote


@router.get("/my-quotes", response_model=list[QuoteResponse])
async def get_my_quotes(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Get all quotes for the current user
    """
    statement = select(Quote).where(Quote.user_id == current_user.id).order_by(Quote.created_at.desc())
    quotes = session.exec(statement).all()
    return quotes


@router.get("/admin/quotes", response_model=list[QuoteResponse])
async def list_all_quotes(
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser),
    status: QuoteStatus = None
):
    """
    List all quotes (Admin only)
    """
    statement = select(Quote).order_by(Quote.created_at.desc())
    
    if status:
        statement = statement.where(Quote.status == status)
    
    quotes = session.exec(statement).all()
    return quotes


@router.get("/{quote_id}", response_model=QuoteResponse)
async def get_quote(
    quote_id: UUID,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user)
):
    """
    Get a specific quote (must be owner or admin)
    """
    quote = session.get(Quote, quote_id)
    
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    
    # Check access
    if not current_user.is_superuser and quote.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to access this quote"
        )
    
    return quote


@router.patch("/admin/{quote_id}/status", response_model=QuoteResponse)
async def update_quote_status(
    quote_id: UUID,
    status_data: QuoteUpdateStatus,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Update quote status and add admin response (Admin only)
    """
    quote = session.get(Quote, quote_id)
    
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    
    quote.status = status_data.status
    
    if status_data.admin_response:
        quote.admin_response = status_data.admin_response
        quote.responded_at = datetime.utcnow()
    
    if status_data.estimated_price:
        quote.estimated_price = status_data.estimated_price
    
    quote.updated_at = datetime.utcnow()
    
    session.add(quote)
    session.commit()
    session.refresh(quote)
    
    # TODO: Send email notification to customer
    
    return quote


@router.post("/{quote_id}/upload-logo")
async def upload_quote_logo(
    quote_id: UUID,
    file: UploadFile = File(...),
    session: Session = Depends(get_session)
):
    """
    Upload company logo for quote request
    """
    quote = session.get(Quote, quote_id)
    
    if not quote:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Quote not found"
        )
    
    # Create uploads directory
    upload_dir = "uploads/quotes"
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save file
    file_extension = file.filename.split(".")[-1]
    filename = f"{quote_id}_{uuid4().hex[:8]}.{file_extension}"
    file_path = os.path.join(upload_dir, filename)
    
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Update quote
    quote.logo_url = f"/uploads/quotes/{filename}"
    quote.updated_at = datetime.utcnow()
    
    session.add(quote)
    session.commit()
    
    return {"logo_url": quote.logo_url}
