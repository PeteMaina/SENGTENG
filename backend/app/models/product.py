"""
Product Database Model
"""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4
from decimal import Decimal


class Product(SQLModel, table=True):
    """
    Product model for items in the catalog
    """
    __tablename__ = "products"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(max_length=255, index=True)
    slug: str = Field(unique=True, max_length=255, index=True)
    description: Optional[str] = Field(default=None)
    
    # Pricing
    price: Decimal = Field(decimal_places=2, ge=0)
    compare_at_price: Optional[Decimal] = Field(default=None, decimal_places=2)
    
    # Inventory
    stock: int = Field(default=0, ge=0)
    sku: Optional[str] = Field(default=None, max_length=100, unique=True)
    
    # Media
    image_url: Optional[str] = Field(default=None, max_length=500)
    images: Optional[str] = Field(default=None)  # JSON array of image URLs
    
    # Category relationship
    category_id: Optional[UUID] = Field(default=None, foreign_key="categories.id")
    category: Optional["Category"] = Relationship(back_populates="products")
    
    # Product details
    features: Optional[str] = Field(default=None)  # JSON array
    specifications: Optional[str] = Field(default=None)  # JSON object
    
    # Status
    is_active: bool = Field(default=True)
    is_featured: bool = Field(default=False)
    
    # SEO
    meta_title: Optional[str] = Field(default=None, max_length=255)
    meta_description: Optional[str] = Field(default=None, max_length=500)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    
    # Relationships
    order_items: List["OrderItem"] = Relationship(back_populates="product")
