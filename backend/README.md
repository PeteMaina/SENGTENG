# Senteng Fashions Backend

FastAPI backend for the Senteng Fashions e-commerce platform.

## Features

- 🔐 JWT Authentication with role-based access control
- 📦 Product & Category management
- 💬 Quote request system for bulk orders
- 🛒 Order processing
- 📷 Image upload functionality
- 📚 Automatic API documentation (Swagger/OpenAPI)
- 🗄️ PostgreSQL database with SQLModel ORM
- 🐳 Docker containerization

## Tech Stack

- **Framework**: FastAPI 0.109+
- **Database**: PostgreSQL 15
- **ORM**: SQLModel + SQLAlchemy
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **File Storage**: Local uploads / S3-compatible (MinIO/AWS)

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Docker & Docker Compose (recommended)

### Installation

1. **Clone the repository**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp ../.env.example ../.env
   # Edit .env with your configuration
   ```

5. **Run with Docker (Recommended)**
   ```bash
   cd ..
   docker-compose up
   ```

   Or run locally:
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Seed the database**
   ``bash
   python scripts/seed_data.py
   ```

## API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login and get JWT tokens
- `GET /api/v1/auth/me` - Get current user profile

### Products
- `GET /api/v1/products` - List products (with filters)
- `GET /api/v1/products/{id}` - Get product details
- `POST /api/v1/products` - Create product (Admin)
- `PUT /api/v1/products/{id}` - Update product (Admin)
- `DELETE /api/v1/products/{id}` - Delete product (Admin)

### Categories
- `GET /api/v1/categories` - List categories
- `POST /api/v1/categories` - Create category (Admin)

### Quotes
- `POST /api/v1/quotes` - Submit quote request
- `GET /api/v1/quotes/my-quotes` - Get user's quotes
- `GET /api/v1/admin/quotes` - List all quotes (Admin)
- `PATCH /api/v1/admin/quotes/{id}/status` - Update quote status (Admin)

## Project Structure

```
backend/
├── app/
│   ├── api/              # API routes
│   │   └── v1/
│   │       ├── endpoints/  # Endpoint modules
│   │       └── router.py   # Main router
│   ├── core/             # Core Configuration
│   │   ├── config.py     # Settings
│   │   ├── database.py   # DB connection
│   │   └── security.py   # Auth utilities
│   ├── models/           # Database models
│   ├── schemas/          # Pydantic schemas
│   └── main.py           # Application entry
├── scripts/              # Utility scripts
├── tests/                # Test suite
├── Dockerfile
└── requirements.txt
```

## Default Admin Credentials

After seeding the database:
- **Email**: admin@sentengfashions.com
- **Password**: admin123

⚠️ **Change these credentials in production!**

## Development

### Run tests
```bash
pytest
```

### Code formatting
```bash
ruff format .
```

### Linting
```bash
ruff check .
```

## License

MIT License - See LICENSE file for details
