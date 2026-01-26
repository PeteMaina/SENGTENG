"""
Category Database Model
"""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4


class Category(SQLModel, table=True):
    """
    Product category model (e.g., Security, Medical, Corporate, etc.)
    """
    __tablename__ = "categories"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str = Field(unique=True, max_length=100)
    slug: str = Field(unique=True, max_length=100, index=True)
    description: Optional[str] = Field(default=None)
    image_url: Optional[str] = Field(default=None, max_length=500)
    
    # Display order
    sort_order: int = Field(default=0)
    is_active: bool = Field(default=True)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    
    # Relationships
    products: List["Product"] = Relationship(back_populates="category")
