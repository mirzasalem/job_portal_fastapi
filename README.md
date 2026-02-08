# 🚀 Job Portal REST API

A production-ready job portal backend API demonstrating modern Python backend development practices. This project showcases secure authentication, database design, and clean API architecture suitable for real-world applications.
# ⚠️ **Project Status:** Currently **under development**. Some exciting new features are coming soon.

## 🎯 Project Highlights

- **Modern Stack**: Built with FastAPI for high performance and automatic API documentation
- **Secure Authentication**: JWT-based auth with access/refresh tokens and bcrypt password hashing
- **Role-Based Access**: Separate permissions for Employers and Job Seekers
- **Database Design**: PostgreSQL with SQLAlchemy ORM featuring proper relationships
- **Production Ready**: Includes Docker support, environment configuration, and comprehensive error handling
- **Well Documented**: Complete API docs, setup guides, and code comments

## ✨ Key Features

### For Employers
- Create, update, and delete job postings
- View all posted jobs
- Manage job status (open/closed)
- Review job applications

### For Job Seekers  
- Browse available jobs
- Apply with cover letters
- Track application history
- Duplicate application prevention

### Security & Best Practices
- JWT authentication (stateless, scalable)
- Password hashing with bcrypt
- Role-based authorization
- Input validation with Pydantic
- SQL injection prevention via ORM
- Environment-based configuration

## 🛠 Tech Stack

- **Backend Framework**: FastAPI 0.109
- **Database**: PostgreSQL 12+
- **ORM**: SQLAlchemy 2.0
- **Authentication**: JWT (python-jose)
- **Password Hashing**: Bcrypt (passlib)
- **Validation**: Pydantic v2
- **Server**: Uvicorn
- **Containerization**: Docker & Docker Compose

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- RESTful API design and implementation
- Database modeling and relationships (One-to-Many)
- Authentication & authorization patterns
- Security best practices
- Clean code architecture (layered pattern)
- Environment configuration management
- Docker containerization
- API documentation

## 🚀 Quick Start
```bash
# Clone the repository
git clone https://github.com/yourusername/job-portal-api.git
cd job-portal-api

# Setup and run
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configure database
cp .env.example .env
# Edit .env with your database credentials

# Run the application
uvicorn app.main:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.


## 🔗 API Endpoints

- **Authentication**: `/auth/register`, `/auth/login`, `/auth/me`
- **Jobs**: `/jobs/` (CRUD operations)
- **Applications**: `/applications/` (Apply and track)

Full API documentation available at `/docs` when running.


## 👨‍💻 Author

Your Name  
[GitHub](https://github.com/mirzasalem/) | [LinkedIn](https://www.linkedin.com/in/mirzasalem/) | [Portfolio](https://mirzasalem.vercel.app/)

## 💼 About This Project

Created as a portfolio project to demonstrate backend development skills for job applications. The project follows industry best practices and includes features commonly found in production applications.

