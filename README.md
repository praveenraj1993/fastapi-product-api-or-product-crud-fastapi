# FastAPI Product API

A simple CRUD API for managing product inventory, built using **FastAPI** and **Pydantic**.

This project demonstrates my ability to quickly learn and implement modern Python web frameworks and follow RESTful design principles.

## 🚀 Features

- Create, Read, Update, Delete (CRUD) products
- UUID-based product IDs
- Request validation using Pydantic
- Auto-generated Swagger UI docs
- In-memory storage (can be swapped with real DB)

## 📦 Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- Uvicorn (ASGI server)

## 📄 API Endpoints

| Method | Endpoint             | Description              |
|--------|----------------------|--------------------------|
| POST   | `/products/`         | Create a new product     |
| GET    | `/products/`         | Get list of all products |
| GET    | `/products/{id}`     | Get product by ID        |
| PUT    | `/products/{id}`     | Update product           |
| DELETE | `/products/{id}`     | Delete product           |

## ▶️ Getting Started

### 1. Install dependencies
```bash
pip install fastapi uvicorn
