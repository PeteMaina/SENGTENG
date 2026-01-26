"""
Category Endpoints - Manage product categories
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from datetime import datetime
from slugify import slugify
from uuid import UUID

from app.core import get_session
from app.models import Category, User
from app.schemas import CategoryCreate, CategoryUpdate, CategoryResponse
from app.api.dependencies import get_current_superuser

router = APIRouter()


@router.get("/", response_model=list[CategoryResponse])
async def list_categories(
    session: Session = Depends(get_session),
    include_inactive: bool = False
):
    """
    List all categories
    """
    statement = select(Category)
    
    if not include_inactive:
        statement = statement.where(Category.is_active == True)
    
    statement = statement.order_by(Category.sort_order)
    
    categories = session.exec(statement).all()
    return categories


@router.get("/{category_id}", response_model=CategoryResponse)
async def get_category(
    category_id: UUID,
    session: Session = Depends(get_session)
):
    """
    Get a single category by ID
    """
    category = session.get(Category, category_id)
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    return category


@router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(
    category_data: CategoryCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Create a new category (Admin only)
    """
    # Generate slug
    slug = slugify(category_data.name)
    
    # Check for duplicate
    existing = session.exec(select(Category).where(Category.slug == slug)).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category with this name already exists"
        )
    
    category = Category(
        **category_data.model_dump(),
        slug=slug
    )
    
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return category


@router.put("/{category_id}", response_model=CategoryResponse)
async def update_category(
    category_id: UUID,
    category_data: CategoryUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Update a category (Admin only)
    """
    category = session.get(Category, category_id)
    
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found"
        )
    
    update_dict = category_data.model_dump(exclude_unset=True)
    
    # Regenerate slug if name changed
    if "name" in update_dict:
        update_dict["slug"] = slugify(update_dict["name"])
    
    for key, value in update_dict.items():
        setattr(category, key, value)
    
    category.updated_at = datetime.utcnow()
    
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return category
