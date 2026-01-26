"""
Database Connection and Session Management
"""
from sqlmodel import create_engine, Session, SQLModel
from app.core.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=True if settings.ENVIRONMENT == "development" else False,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20
)


def get_session():
    """
    Dependency to get database session
    """
    with Session(engine) as session:
        yield session


def init_db():
    """
    Initialize database - create all tables
    """
    SQLModel.metadata.create_all(engine)
    print("✅ Database tables created successfully")
