# E-commerce API with FastAPI

A professional e-commerce REST API built with FastAPI, SQLAlchemy, and SQLite. This project demonstrates modern Python backend development practices with proper project structure and CRUD operations.

## 🚀 Features

- **Product Management**: Complete CRUD operations for products
- **RESTful API**: Following REST conventions and best practices
- **Data Validation**: Automatic request/response validation with Pydantic
- **Database ORM**: SQLAlchemy for database operations
- **Auto Documentation**: Interactive API docs with Swagger UI
- **Structured Architecture**: Clean separation of models, schemas, controllers, and routes

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapping
- **Pydantic**: Data validation using Python type annotations
- **SQLite**: Lightweight database for development
- **UV**: Modern Python package manager

## 📁 Project Structure

```
CRUD/
├── app/
│   ├── config/
│   │   └── database.py          # Database configuration
│   ├── models/
│   │   └── product_model.py     # Database models
│   ├── schemas/
│   │   └── product_schema.py    # Pydantic schemas for validation
│   ├── controllers/
│   │   └── product_controller.py # Business logic
│   └── routes/
│       └── product_routes.py    # API endpoints
├── main.py                      # Application entry point
├── .env                         # Environment variables
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## 🚦 Getting Started

### Prerequisites

- Python 3.8+
- UV package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd CRUD
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Create environment file**

   ```bash
   cp .env.example .env
   ```

4. **Update environment variables**
   ```env
   DATABASE_URL=sqlite:///./test.db
   DEBUG=True
   ```

### Running the Application

1. **Start the development server**

   ```bash
   uv run fastapi dev
   ```

2. **Access the application**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

## 📚 API Endpoints

### Products

| Method   | Endpoint                | Description                      |
| -------- | ----------------------- | -------------------------------- |
| `GET`    | `/api/v1/products/`     | Get all products with pagination |
| `GET`    | `/api/v1/products/{id}` | Get product by ID                |
| `POST`   | `/api/v1/products/`     | Create new product               |
| `PUT`    | `/api/v1/products/{id}` | Update product                   |
| `DELETE` | `/api/v1/products/{id}` | Delete product (soft delete)     |

### Example API Usage

**Create a Product:**

```bash
curl -X POST "http://localhost:8000/api/v1/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "iPhone 15",
       "description": "Latest iPhone model",
       "price": 999.99,
       "quantity": 50,
       "category": "Electronics",
       "image_url": "https://example.com/iphone15.jpg"
     }'
```

**Get All Products:**

```bash
curl "http://localhost:8000/api/v1/products/?skip=0&limit=10"
```

### Project Architecture

This project follows a **layered architecture** pattern:

1. **Models Layer**: Database models using SQLAlchemy ORM
2. **Schemas Layer**: Pydantic models for data validation and serialization
3. **Controllers Layer**: Business logic and data processing
4. **Routes Layer**: API endpoints and HTTP handling
5. **Config Layer**: Database and application configuration

### Adding New Features

1. **Create Model**: Add database model in `app/models/`
2. **Create Schema**: Add Pydantic schemas in `app/schemas/`
3. **Create Controller**: Add business logic in `app/controllers/`
4. **Create Routes**: Add API endpoints in `app/routes/`
5. **Register Routes**: Include router in `main.py`

## 🚀 Deployment

### Environment Variables

```env
DATABASE_URL=your_production_database_url
DEBUG=False
SECRET_KEY=your_secret_key
```

### Production Setup

1. **Switch to PostgreSQL or MySQL**

   ```env
   DATABASE_URL=postgresql://user:password@localhost/dbname
   ```

2. **Install production dependencies**

   ```bash
   uv add psycopg2-binary  # for PostgreSQL
   # or
   uv add pymysql         # for MySQL
   ```

3. **Run with production server**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## 🧪 Testing

Visit the interactive API documentation at `http://localhost:8000/docs` to test all endpoints directly in your browser.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI team for the amazing framework
- SQLAlchemy for the powerful ORM
- Pydantic for elegant data validation

## 📞 Contact

Your Name - [rohitgite03@gmail.com](mailto:rohitgite03@gmail.com)

---

⭐ **Star this repository if it helped you learn FastAPI!** ⭐
