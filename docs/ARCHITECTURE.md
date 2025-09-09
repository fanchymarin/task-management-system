# Architecture Documentation

## Overview

This is a containerized task management system built with Django REST Framework as the backend API, PostgreSQL as the primary database, and Redis for caching. The system follows a microservices architecture pattern using Docker Compose for orchestration.

## System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│                 │    │                 │    │                 │
│   Django API    │◄──►│   PostgreSQL    │    │     Redis       │
│   (Port 8000)   │    │   (Database)    │    │   (Cache)       │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │
         ▼
┌─────────────────┐
│                 │
│  REST API       │
│  Endpoints      │
│                 │
└─────────────────┘
```

## Technology Stack

### Backend
- **Django 5.1.7**: Web framework
- **Django REST Framework 3.16.1**: API framework
- **Python 3.10**: Programming language

### Database
- **PostgreSQL**: Primary database
- **psycopg2-binary**: PostgreSQL adapter

### Caching & Message Broker
- **Redis**: Caching and session storage
- **django-redis**: Django Redis integration

### Additional Libraries
- **django-filter**: API filtering capabilities
- **django-cors-headers**: Cross-origin resource sharing

### Infrastructure
- **Docker & Docker Compose**: Containerization
- **Make**: Build automation

## Project Structure

```
task-management-system/
├── django_backend/
│   ├── apps/
│   │   ├── common/           # Shared utilities and views
│   │   ├── tasks/            # Task management module
│   │   └── users/            # User management module
│   ├── config/               # Django configuration
│   ├── scripts/              # Deployment scripts
│   └── requirements.txt      # Python dependencies
├── images/                   # Docker images
│   ├── postgres/
│   └── redis/
├── docker-compose.yml        # Service orchestration
├── Makefile                  # Build automation
└── README.md
```

## Core Components

### 1. User Management (`apps/users/`)
- **Model**: Custom User model extending AbstractUser
- **Features**: 
  - User authentication and authorization
  - User profile management
  - Metadata field for extensibility
- **API Endpoints**: 
  - `/api/users/` - User CRUD operations
  - `/api/users/me/` - Current user profile

### 2. Task Management (`apps/tasks/`)
- **Models**:
  - `Task`: Core task entity with status, priority, assignments
  - `Tag`: Task categorization
  - `Comment`: Task discussions
- **Features**:
  - Task CRUD operations
  - Task assignment to multiple users
  - Hierarchical tasks (parent/subtask relationships)
  - Task comments and discussions
  - Filtering and search capabilities
  - Pagination support
- **API Endpoints**:
  - `/api/tasks/` - Task CRUD operations
  - `/api/tasks/{id}/assign/` - Task assignment management
  - `/api/tasks/{id}/comments/` - Task comments

### 3. Common Utilities (`apps/common/`)
- Authentication views
- Custom templates
- Shared utilities

## Database Schema

### User Model
```python
class User(AbstractUser):
    metadata = JSONField(null=True, blank=True)
```

### Task Model
```python
class Task(Model):
    # Core fields
    title = CharField(max_length=200)
    description = TextField()
    status = CharField(choices=STATUS_CHOICES)
    priority = CharField(choices=PRIORITY_CHOICES)
    due_date = DateTimeField()
    estimated_hours = IntegerField()
    actual_hours = DecimalField()
    
    # Relationships
    created_by = ForeignKey(User)
    assigned_to = ManyToManyField(User)
    tags = ManyToManyField(Tag)
    parent_task = ForeignKey('self')
    comments = ManyToManyField(Comment)
    
    # Metadata
    metadata = JSONField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    is_archived = BooleanField(default=False)
```