# Google-X-MLB-Hackathon

Here's a well-structured **README.md** description for your project:

---

# **Auth System for Project Integration**

This module provides a robust authentication system for the larger project. It includes essential features like user registration, login, and token-based authentication with role-based access control.

## **Features**
- **User Registration** (`/signup`):
  - Allows users to create accounts with email, password, and a specified role (`fan`, `coach`, or `admin`).
- **User Login** (`/signin`):
  - Authenticates users and provides JSON Web Tokens (JWT) for secure session management.
- **Token Refresh** (`/refresh`):
  - Allows users to refresh their access tokens using a valid refresh token.
- **Role-Based Authentication**:
  - Assigns roles (`fan`, `coach`, `admin`) to users for access control.
- **Django Admin Panel**:
  - Manage users and roles via an easy-to-use web interface.

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- Django 4.x or higher
- Virtual environment (recommended)

### **Installation**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/auth-system.git
   cd auth-system
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Open your browser and go to:
     ```
     http://127.0.0.1:8000/
     ```

---

## **Endpoints**
| Endpoint         | Method | Description                       |
|-------------------|--------|-----------------------------------|
| `/api/auth/signup/`   | POST   | Register a new user             |
| `/api/auth/signin/`   | POST   | Log in a user and get tokens    |
| `/api/auth/refresh/`  | POST   | Refresh an access token         |

### **Example API Usage**
#### User Registration (`/signup`)
```json
POST http://127.0.0.1:8000/api/auth/signup/
{
  "email": "user@example.com",
  "password": "password123",
  "role": "coach"
}
```

#### User Login (`/signin`)
```json
POST http://127.0.0.1:8000/api/auth/signin/
{
  "email": "user@example.com",
  "password": "password123"
}
```

#### Token Refresh (`/refresh`)
```json
POST http://127.0.0.1:8000/api/auth/refresh/
{
  "refresh": "<your_refresh_token>"
}
```

---

## **Project Structure**
```
auth_project/
│
├── auth_system/         # Main project folder
│   ├── settings.py      # Django settings
│   ├── urls.py          # Project-level URL routing
│
├── users/               # App for user management
│   ├── models.py        # User model with roles
│   ├── views.py         # Views for authentication
│   ├── serializers.py   # API serializers
│
├── manage.py            # Django management script
└── requirements.txt     # Project dependencies
```

---

## **Future Enhancements**
- Implement email verification for user registration.
- Add password reset functionality.
- Introduce OAuth integration for third-party logins (e.g., Google, Facebook).

---

Feel free to modify this to fit your project specifics. Let me know if you'd like additional customization! 😊
