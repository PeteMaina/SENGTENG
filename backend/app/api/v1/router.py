"""
API V1 Router - Combines all endpoint routers
"""
from fastapi import APIRouter

from app.api.v1.endpoints import auth, products, categories, quotes

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
api_router.include_router(products.router, prefix="/products", tags=["Products"])
api_router.include_router(categories.router, prefix="/categories", tags=["Categories"])
api_router.include_router(quotes.router, prefix="/quotes", tags=["Quotes"])
