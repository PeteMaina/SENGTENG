"""
Product Endpoints - CRUD operations for products
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query, UploadFile, File
from sqlmodel import Session, select, func
from typing import Optional
from datetime import datetime
from slugify import slugify
import os
from uuid import UUID, uuid4

from app.core import get_session
from app.models import Product, Category, User
from app.schemas import ProductCreate, ProductUpdate, ProductResponse, PaginatedResponse
from app.api.dependencies import get_current_superuser

router = APIRouter()


@router.get("/", response_model=list[ProductResponse])
async def list_products(
    session: Session = Depends(get_session),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    category_id: Optional[UUID] = None,
    is_featured: Optional[bool] = None,
    search: Optional[str] = None
):
    """
    List all active products with optional filtering
    """
    statement = select(Product).where(Product.is_active == True)
    
    # Apply filters
    if category_id:
        statement = statement.where(Product.category_id == category_id)
    
    if is_featured is not None:
        statement = statement.where(Product.is_featured == is_featured)
    
    if search:
        statement = statement.where(
            Product.name.ilike(f"%{search}%") | 
            Product.description.ilike(f"%{search}%")
        )
    
    # Pagination
    statement = statement.offset(skip).limit(limit)
    
    products = session.exec(statement).all()
    return products


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(
    product_id: UUID,
    session: Session = Depends(get_session)
):
    """
    Get a single product by ID
    """
    product = session.get(Product, product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    return product


@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_data: ProductCreate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Create a new product (Admin only)
    """
    # Generate slug from name
    slug = slugify(product_data.name)
    
    # Ensure unique slug
    existing = session.exec(select(Product).where(Product.slug == slug)).first()
    if existing:
        slug = f"{slug}-{uuid4().hex[:8]}"
    
    # Create product
    product = Product(
        **product_data.model_dump(),
        slug=slug
    )
    
    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product


@router.put("/{product_id}", response_model=ProductResponse)
async def update_product(
    product_id: UUID,
    product_data: ProductUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Update a product (Admin only)
    """
    product = session.get(Product, product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Update fields
    update_dict = product_data.model_dump(exclude_unset=True)
    
    # If name is updated, regenerate slug
    if "name" in update_dict:
        update_dict["slug"] = slugify(update_dict["name"])
    
    for key, value in update_dict.items():
        setattr(product, key, value)
    
    product.updated_at = datetime.utcnow()
    
    session.add(product)
    session.commit()
    session.refresh(product)
    
    return product


@router.delete("/{product_id}", response_model=dict)
async def delete_product(
    product_id: UUID,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Delete a product (Admin only) - soft delete by setting is_active to False
    """
    product = session.get(Product, product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    product.is_active = False
    product.updated_at = datetime.utcnow()
    
    session.add(product)
    session.commit()
    
    return {"message": "Product deleted successfully"}


@router.post("/{product_id}/upload-image")
async def upload_product_image(
    product_id: UUID,
    file: UploadFile = File(...),
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_superuser)
):
    """
    Upload product image (Admin only)
    """
    product = session.get(Product, product_id)
    
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    
    # Create uploads directory
    upload_dir = "uploads/products"
    os.makedirs(upload_dir, exist_ok=True)
    
    # Generate unique filename
    file_extension = file.filename.split(".")[-1]
    filename = f"{product_id}_{uuid4().hex[:8]}.{file_extension}"
    file_path = os.path.join(upload_dir, filename)
    
    # Save file
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    # Update product
    product.image_url = f"/uploads/products/{filename}"
    product.updated_at = datetime.utcnow()
    
    session.add(product)
    session.commit()
    
    return {"image_url": product.image_url}
