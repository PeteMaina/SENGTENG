"""
Quote Request Database Model
"""
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4
from enum import Enum


class QuoteStatus(str, Enum):
    """Quote request status enumeration"""
    PENDING = "pending"
    REVIEWED = "reviewed"
    RESPONDED = "responded"
    CLOSED = "closed"


class Quote(SQLModel, table=True):
    """
    Quote request model for bulk/custom uniform orders
    """
    __tablename__ = "quotes"
    
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    quote_number: str = Field(unique=True, max_length=50, index=True)
    
    # Customer (optional - can be guest or authenticated user)
    user_id: Optional[UUID] = Field(default=None, foreign_key="users.id")
    user: Optional["User"] = Relationship(back_populates="quotes")
    
    # Contact information (for guest quotes)
    contact_name: str = Field(max_length=255)
    contact_email: str = Field(max_length=255)
    contact_phone: str = Field(max_length=20)
    
    # Company details
    company_name: str = Field(max_length=255)
    industry: Optional[str] = Field(default=None, max_length=100)
    
    # Quote requirements
    uniform_type: str = Field(max_length=255)  # e.g., "Security Uniforms"
    quantity: int = Field(ge=1)
    requirements: str  # Detailed requirements
    
    # Customization
    logo_url: Optional[str] = Field(default=None, max_length=500)
    customization_notes: Optional[str] = Field(default=None)
    
    # Status and response
    status: QuoteStatus = Field(default=QuoteStatus.PENDING)
    admin_response: Optional[str] = Field(default=None)
    estimated_price: Optional[str] = Field(default=None, max_length=100)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
    responded_at: Optional[datetime] = Field(default=None)
