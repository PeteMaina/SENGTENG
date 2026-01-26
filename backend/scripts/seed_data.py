"""
Database Seeding Script - Populate initial data
"""
import asyncio
from sqlmodel import Session, create_engine
from app.core.config import settings
from app.core.security import hash_password
from app.models import User, Category, Product
from datetime import datetime
from slugify import slugify
from decimal import Decimal

# Create engine
engine = create_engine(settings.DATABASE_URL)


def seed_database():
    """
    Seed database with initial Senteng Fashions data
    """
    with Session(engine) as session:
        print("🌱 Seeding database...")
        
        # Create admin user
        admin = User(
            email="admin@sentengfashions.com",
            hashed_password=hash_password("admin123"),
            full_name= "Senteng Admin",
            is_superuser=True,
            is_active=True
        )
        session.add(admin)
        print("✅ Created admin user")
        
        # Create categories
        categories_data = [
            {"name": "Industrial Wear", "description": "Durable uniforms for industrial workers", "sort_order": 1},
            {"name": "Hospitality Wear", "description": "Professional attire for hospitality industry", "sort_order": 2},
            {"name": "Health Care Wear", "description": "Medical uniforms and scrubs", "sort_order": 3},
            {"name": "Corporate Wear", "description": "Business and corporate uniforms", "sort_order": 4},
            {"name": "Security Uniforms", "description": "Security guard uniforms and accessories", "sort_order": 5},
            {"name": "Safety Wear & PPE", "description": "Personal protective equipment", "sort_order": 6},
            {"name": "Sports Wear", "description": "Athletic and team uniforms", "sort_order": 7},
            {"name": "School Uniforms", "description": "School uniforms and accessories", "sort_order": 8},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category = Category(
                name=cat_data["name"],
                slug=slugify(cat_data["name"]),
                description=cat_data["description"],
                sort_order=cat_data["sort_order"],
                is_active=True
            )
            session.add(category)
            categories[cat_data["name"]] = category
        
        session.commit()
        print(f"✅ Created {len(categories)} categories")
        
        # Refresh categories to get IDs
        for category in categories.values():
            session.refresh(category)
        
        # Create sample products
        products_data = [
            {
                "name": "Security Guard Uniform Set",
                "description": "Complete security guard uniform including shirt, trousers, and belt",
                "price": Decimal("4500.00"),
                "stock": 50,
                "category": "Security Uniforms",
                "sku": "SEC-001",
                "is_featured": True
            },
            {
                "name": "Chef Uniform White",
                "description": "Professional chef uniform with double-breasted jacket",
                "price": Decimal("3500.00"),
                "stock": 30,
                "category": "Hospitality Wear",
                "sku": "HOSP-001",
                "is_featured": True
            },
            {
                "name": "Medical Scrubs Set",
                "description": "Comfortable medical scrubs - top and bottom",
                "price": Decimal("2800.00"),
                "stock": 100,
                "category": "Health Care Wear",
                "sku": "MED-001",
                "is_featured": True
            },
            {
                "name": "Corporate Polo Shirt",
                "description": "High-quality cotton polo shirt with embroidery options",
                "price": Decimal("1200.00"),
                "compare_at_price": Decimal("1500.00"),
                "stock": 200,
                "category": "Corporate Wear",
                "sku": "CORP-001"
            },
            {
                "name": "Reflective Safety Vest",
                "description": "High-visibility safety vest with reflective strips",
                "price": Decimal("800.00"),
                "stock": 150,
                "category": "Safety Wear & PPE",
                "sku": "SAFE-001"
            },
            {
                "name": "School Uniform Set",
                "description": "Complete primary school uniform set",
                "price": Decimal("2500.00"),
                "stock": 75,
                "category": "School Uniforms",
                "sku": "SCH-001"
            },
            {
                "name": "Sports Team Jersey",
                "description": "Customizable sports jersey with sublimation printing",
                "price": Decimal("1800.00"),
                "stock": 100,
                "category": "Sports Wear",
                "sku": "SPORT-001"
            },
            {
                "name": "Industrial Coverall",
                "description": "Heavy-duty industrial coverall with multiple pockets",
                "price": Decimal("3200.00"),
                "stock": 40,
                "category": "Industrial Wear",
                "sku": "IND-001"
            },
        ]
        
        for prod_data in products_data:
            category_name = prod_data.pop("category")
            product = Product(
                **prod_data,
                slug=slugify(prod_data["name"]),
                category_id=categories[category_name].id,
                is_active=True
            )
            session.add(product)
        
        session.commit()
        print(f"✅ Created {len(products_data)} products")
        
        print("\n🎉 Database seeding completed successfully!")
        print("\n📝 Admin Credentials:")
        print("   Email: admin@sentengfashions.com")
        print("   Password: admin123")
        print("\n⚠️  IMPORTANT: Change the admin password in production!")


if __name__ == "__main__":
    seed_database()
