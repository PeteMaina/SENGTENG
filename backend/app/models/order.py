"""
Order and OrderItem Database Models
"""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from uuid import UUID, uuid4
from decimal import Decimal
from enum import Enum


class OrderStatus(str, Enum):
    """Order status enumeration"""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class Order(SQLModel, table=True):
    """
    Order model for customer purchases
    """
    __tablename__ = "orders"
    
    id: UUID = Field(default_factory=uuid 4, primary_key=True)
    order_number: str = Field(unique=True, max_length=50, index=True)
    
    # Customer
    user_id: UUID = Field(foreign_key="users.id")
    user: "User" = Relationship(back_populates="orders")
    
    # Order details
    total_amount: Decimal = Field(decimal_places=2, ge=0)
    status: OrderStatus = Field(default=OrderStatus.PENDING)
    
    # Shipping information
    shipping_address: Optional[str] = Field(default=None)
    shipping_city: Optional[str] = Field(default=None, max_length=100)
    shipping_phone: Optional[str] = Field(default=None, max_length=20)
    
    # Notes
    customer_notes: Optional[str] = Field(default=None)
    admin_notes: Optional[str] = Field(default=None)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    shipped_at: Optional[datetime] = Field(default=None)
    delivered_at: Optional[datetime] = Field(default=None)
    
    # Relationships
    items: List["OrderItem"] = Relationship(back_populates="order")


class OrderItem(SQLModel, table=True):
    """
    Order line items
    """
    __tablename__ = "order_items"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    
    # Order relationship
    order_id: UUID = Field(foreign_key="orders.id")
    order: Order = Relationship(back_populates="items")
    
    # Product relationship
    product_id: UUID = Field(foreign_key="products.id")
    product: "Product" = Relationship(back_populates="order_items")
    
    # Item details
    quantity: int = Field(ge=1)
    unit_price: Decimal = Field(decimal_places=2, ge=0)
    total_price: Decimal = Field(decimal_places=2, ge=0)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
