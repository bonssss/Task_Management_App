# 📌 Task Management API

A **Django + Django REST Framework** backend project that provides a fully functional **Task Management API**.  
This API allows users to register, log in, and manage their tasks (create, update, delete, filter, sort, and mark as completed).  
It is designed as part of the **ALX Backend Web Development Capstone Project (Part 3)**.

---

## 🚀 Features

### 🔐 User Management
- User **registration, login, logout**
- Password hashing & authentication
- Each user can **only manage their own tasks**

### ✅ Task Management
- Create, Read, Update, and Delete tasks
- Fields: **title, description, due date, priority, status**
- Mark tasks as **complete/incomplete**
- Track **created_at, updated_at, completed_at**

### 🔎 Task Filters & Sorting
- Filter by:
  - `status` (Pending, In Progress, Completed)
  - `priority` (Low, Medium, High)
  - `due_date`
- Sort by:
  - `due_date`
  - `priority`

### 🛡️ Permissions
- Only **owners** can access/edit their tasks
- Unauthorized users are blocked from others’ data

### 🌍 Deployment
- Deployable to **Heroku** or **PythonAnywhere**

---


