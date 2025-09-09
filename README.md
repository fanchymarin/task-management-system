# Task Management System

A robust task management system built with Django REST Framework, featuring user management, task assignments, comments, tags, and comprehensive filtering capabilities.

## Quick Start

```bash
git clone https://github.com/fanchymarin/task-management-system
cd task-management-system
cp .env.sample .env
make up
```

## 📋 Features

- **User Management**: Custom user model with authentication
- **Task Management**: Complete CRUD operations for tasks
- **Task Organization**: 
  - Status tracking (Pending, In Progress, Completed, On Hold, Cancelled)
  - Priority levels (Low, Medium, High, Urgent)
  - Tags system for categorization
  - Subtask support with parent-child relationships
- **Collaboration**: 
  - Multi-user task assignment
  - Comment system for task discussions
  - User activity tracking
- **Advanced Filtering**: Search, filter, and sort tasks by multiple criteria
- **API-First Design**: RESTful API with Django REST Framework
- **Containerized**: Docker-based deployment with PostgreSQL and Redis

## 🚀 Prerequisites

- Docker
- Docker Compose
- Make

## 🛠️ Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/fanchymarin/task-management-system
cd task-management-system
```

### 2. Environment Configuration
```bash
cp .env.sample .env
```

Edit `.env` file with your configuration:
```env
# Database
POSTGRES_DB=task_management
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=your_password

# Django
DJANGO_SUPERUSER_EMAIL=admin@example.com
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin_password
DJANGO_PORT=8000

# Add other required environment variables
```

### 3. Build and Run
```bash
make up
```

> [!TIP]
> You may check all available commands by running `make list`

The application will be available at `http://localhost:8000`

## 📊 Data Models

### Task Model
```python
{
    "title": "string",
    "description": "text",
    "status": "pending|in_progress|completed|on_hold|cancelled",
    "priority": "low|medium|high|urgent",
    "due_date": "datetime",
    "estimated_hours": "integer",
    "actual_hours": "decimal",
    "created_by": "user_id",
    "assigned_to": ["user_ids"],
    "tags": ["tag_names"],
    "parent_task": "task_id",
    "comments": ["comment_ids"],
    "metadata": "json",
    "created_at": "datetime",
    "updated_at": "datetime",
    "is_archived": "boolean"
}
```

## 🗄️ Database

- **PostgreSQL**: Primary database for data persistence
- **Redis**: Caching and session storage
- Automatic migrations and superuser creation on startup

## 📈 Health Monitoring

Health check endpoint available at `/health/` that monitors:
- Database connectivity
- Redis connectivity

## 🐳 Docker Services

- **django**: Main application server (port 8000)
- **postgres**: PostgreSQL database
- **redis**: Redis cache server

## 🧪 Development

### Access Container Shells
```bash
# Django shell
make shell

# PostgreSQL shell
make shelldb

# View logs
make logs
```

### Database Management
The application automatically:
- Creates database migrations
- Applies migrations
- Creates superuser account
- Loads initial data from `dump.sql.postgres`
