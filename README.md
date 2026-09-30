# 🚀 FastAPI CRUD REST API Tutorial

A practical **FastAPI tutorial project** focused on building REST APIs with **CRUD operations, Pydantic models, request validation, API routing, and Uvicorn**.

This project is designed to understand the fundamentals of backend API development using Python and FastAPI.

---

## 📌 What This Project Covers

This tutorial covers the core concepts required to build a RESTful API with FastAPI:

* FastAPI application setup
* REST API fundamentals
* CRUD operations
* HTTP methods
* API routes and endpoints
* Pydantic models
* Request body validation
* Path parameters
* Query parameters
* HTTP status codes
* Error handling
* Uvicorn server
* Swagger / OpenAPI documentation

---

## 🔄 CRUD Operations

CRUD stands for:

| Operation | HTTP Method | Purpose                     |
| --------- | ----------- | --------------------------- |
| Create    | `POST`      | Create a new resource       |
| Read      | `GET`       | Retrieve resources          |
| Update    | `PUT`       | Update an existing resource |
| Delete    | `DELETE`    | Delete a resource           |

The project demonstrates how these operations are implemented using FastAPI endpoints.

---

## 🧩 Pydantic

**Pydantic** is used for defining data models and validating incoming API data.

Example:

```python
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
```

FastAPI can use these models to validate request bodies before passing the data to the API logic.

---

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **Pydantic**
* **Uvicorn**
* **REST API**
* **Swagger UI / OpenAPI**

---

## 📁 Project Structure

```text
FastAPI-CRUD-REST-API-Tutorial/
│
├── src/
│   ├── ...
│   └── ...
│
├── README.md
└── requirements.txt
```

> The `src` directory contains the FastAPI application and related source code.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/DataWithPdeep/FastAPI-CRUD-REST-API-Tutorial-.git
```

### 2. Navigate to the project

```bash
cd FastAPI-CRUD-REST-API-Tutorial-
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the FastAPI application using Uvicorn.

```bash
uvicorn src.main:app --reload
```

Depending on the application's entry-point file, use the corresponding module path.

The API will normally be available at:

```text
http://127.0.0.1:8000
```

---

## 📚 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to:

* View available endpoints
* Send API requests
* Test CRUD operations
* Check request schemas
* View response data

FastAPI also provides ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

## 🎯 Learning Objectives

After completing this tutorial, you should understand:

* How FastAPI applications are structured
* How REST APIs work
* How HTTP methods are used
* How to create API endpoints
* How Pydantic validates request data
* How to implement CRUD operations
* How to handle API errors
* How to run and test APIs using Uvicorn
* How to use Swagger/OpenAPI documentation

---

## 🧪 API Testing

The API can be tested using:

* Swagger UI
* Postman
* cURL
* Any REST API client

Swagger UI is particularly useful during development because FastAPI generates the interactive API documentation automatically.

---

## 📈 Future Improvements

Possible extensions for this project include:

* Database integration
* SQLAlchemy ORM
* PostgreSQL / SQLite
* Authentication and authorization
* JWT authentication
* Automated testing with Pytest
* Docker containerization
* API deployment
* CI/CD with GitHub Actions

---

## 👨‍💻 Author

**Pradeep Singh**

AI/ML | GenAI | Agentic AI | MLOps | Python | FastAPI

GitHub: [DataWithPdeep](https://github.com/DataWithPdeep)

---

## ⭐ About This Project

This project was created as a practical learning exercise to understand **FastAPI, REST API development, CRUD operations, and Pydantic-based data validation**.

If you find this repository useful, consider giving it a ⭐.
