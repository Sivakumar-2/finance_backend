# 💰 Finance Data Processing and Access Control Backend

## 📌 Overview

This project is a backend system for a **finance dashboard** that allows users to manage financial records and view summarized analytics based on their roles.

It demonstrates:

* API design using Django REST Framework
* Role-based access control
* Financial data processing
* Clean backend architecture

---

## 🚀 Features

### 👤 User & Role Management

* Create and manage users
* Assign roles:

  * **Admin** → Full access (manage users + records)
  * **Analyst** → View records + dashboard insights
  * **Viewer** → View-only access
* Active / inactive user handling

---

### 💳 Financial Records

Each record contains:

* Amount
* Type (Income / Expense)
* Category
* Date
* Notes
* Created by (user)

#### Supported operations:

* Create records
* View records
* Update records
* Delete records
* Filter records

---

### 📊 Dashboard APIs

Provides summary analytics:

* Total Income
* Total Expenses
* Net Balance
* Total Records Count
* Recent Transactions
* Category-wise Summary

---

### 🔐 Authentication & Authorization

* JWT-based authentication
* Session authentication (for browser testing)
* Role-based access control
* Protected endpoints using permissions

---

### ⚠️ Validation & Error Handling

* Input validation for all APIs
* Proper HTTP status codes
* Meaningful error messages

---

## 🛠️ Tech Stack

* **Backend:** Django, Django REST Framework
* **Database:** SQLite (default)
* **Authentication:** JWT (SimpleJWT)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd finance_backend
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create superuser

```bash
python manage.py createsuperuser
```

### 6️⃣ Run server

```bash
python manage.py runserver
```

---

## 🔑 API Endpoints

### 🔐 Authentication

* `POST /api/token/` → Get access & refresh token

---

### 👤 Users

* Managed via Django Admin

---

### 💳 Records

* `GET /records/` → List records
* `POST /records/` → Create record
* `PUT /records/{id}/` → Update record
* `DELETE /records/{id}/` → Delete record

---

### 📊 Dashboard

* `GET /dashboard/` → Get financial summary

---

## 🧪 How to Test

### 👉 Option 1: Browser (Recommended)

1. Go to:

```
http://127.0.0.1:8000/dashboard/
```

2. Click **Login**
3. Enter user credentials
4. View dashboard data

---

### 👉 Option 2: Postman

1. Get token from `/api/token/`
2. Add header:

```
Authorization: Bearer <access_token>
```

3. Call `/dashboard/`

---

## 📂 Project Structure

```
finance_backend/
│
├── users/        # User management
├── records/      # Financial records
├── dashboard/    # Dashboard logic
├── settings.py
└── urls.py
```

---

## 🧠 Assumptions

* Roles are predefined (Admin, Analyst, Viewer)
* Each record belongs to a user
* Non-admin users can only access their own data

---

## ✨ Future Improvements

* Pagination
* Search & filtering
* Soft delete
* API documentation (Swagger)
* Deployment (Render / Railway)

---

## 👨‍💻 Author

Sivakumar

---

## 📌 Conclusion

This project demonstrates a structured backend system with:

* Clean API design
* Proper access control
* Real-world financial data handling

It focuses on clarity, maintainability, and correct business logic implementation.
