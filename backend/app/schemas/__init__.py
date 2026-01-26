"""
Pydantic schemas for API request/response validation
"""
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime


# ============================================
# User Schemas
# ============================================

class UserBase(BaseModel):
    """Base user schema"""
    email: EmailStr
    full_name: Optional[str] = None
    phone: Optional[str] = None


class UserCreate(UserBase):
    """Schema for user registration"""
    password: str = Field(..., min_length=8, max_length=100)


class UserLogin(BaseModel):
    """Schema for user login"""
    email: EmailStr
    password: str


class UserResponse(UserBase):
    """Schema for user response"""
    id: UUID
    is_active: bool
    is_superuser: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    """Schema for updating user profile"""
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None


# ============================================
# Token Schemas
# ============================================

class Token(BaseModel):
    """Token response schema"""
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """Token payload schema"""
    sub: UUID
    exp: datetime
    type: str


# ============================================
# Category Schemas
# ============================================

class CategoryBase(BaseModel):
    """Base category schema"""
    name: str = Field(..., max_length=100)
    description: Optional[str] = None
    is_active: bool = True


class CategoryCreate(CategoryBase):
    """Schema for creating category"""
    pass


class CategoryUpdate(BaseModel):
    """Schema for updating category"""
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = None
    is_active: Optional[bool] = None
    sort_order: Optional[int] = None


class CategoryResponse(CategoryBase):
    """Schema for category response"""
    id: UUID
    slug: str
    image_url: Optional[str] = None
    sort_order: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# ============================================
# Product Schemas
# ============================================

class ProductBase(BaseModel):
    """Base product schema"""
    name: str = Field(..., max_length=255)
    description: Optional[str] = None
    price: float = Field(..., ge=0)
    compare_at_price: Optional[float] = Field(None, ge=0)
    stock: int = Field(default=0, ge=0)
    category_id: Optional[UUID] = None


class ProductCreate(ProductBase):
    """Schema for creating product"""
    sku: Optional[str] = None
    features: Optional[list[str]] = None
    is_featured: bool = False


class ProductUpdate(BaseModel):
    """Schema for updating product"""
    name: Optional[str] = Field(None, max_length=255)
    description: Optional[str] = None
    price: Optional[float] = Field(None, ge=0)
    compare_at_price: Optional[float] = Field(None, ge=0)
    stock: Optional[int] = Field(None, ge=0)
    category_id: Optional[UUID] = None
    is_active: Optional[bool] = None
    is_featured: Optional[bool] = None


class ProductResponse(ProductBase):
    """Schema for product response"""
    id: UUID
    slug: str
    sku: Optional[str] = None
    image_url: Optional[str] = None
    is_active: bool
    is_featured: bool
    created_at: datetime
    category: Optional[CategoryResponse] = None
    
    model_config = ConfigDict(from_attributes=True)


# ============================================
# Quote Schemas
# ============================================

class QuoteBase(BaseModel):
    """Base quote schema"""
    contact_name: str = Field(..., max_length=255)
    contact_email: EmailStr
    contact_phone: str = Field(..., max_length=20)
    company_name: str = Field(..., max_length=255)
    industry: Optional[str] = None
    uniform_type: str = Field(..., max_length=255)
    quantity: int = Field(..., ge=1)
    requirements: str
    customization_notes: Optional[str] = None


class QuoteCreate(QuoteBase):
    """Schema for creating quote"""
    pass


class QuoteResponse(QuoteBase):
    """Schema for quote response"""
    id: UUID
    quote_number: str
    status: str
    logo_url: Optional[str] = None
    admin_response: Optional[str] = None
    estimated_price: Optional[str] = None
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class QuoteUpdateStatus(BaseModel):
    """Schema for updating quote status"""
    status: str
    admin_response: Optional[str] = None
    estimated_price: Optional[str] = None


# ============================================
# Generic Response Schemas
# ============================================

class Message(BaseModel):
    """Generic message response"""
    message: str


class PaginatedResponse(BaseModel):
    """Generic paginated response"""
    items: list
    total: int
    page: int
    page_size: int
    total_pages: int
