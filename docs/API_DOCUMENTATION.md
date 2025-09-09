# API Documentation

## Overview

This is a Django REST API for a Task Management System that provides endpoints for managing users, tasks, comments, and tags. The API uses Django REST Framework with token-based authentication.

## Base URL

```
http://localhost:8000/api/
```

## Authentication

The API uses Django REST Framework's session authentication. Users must log in through the web interface at `/api/auth/login/` to access protected endpoints.

## Endpoints

### Users

#### List Users
- **GET** `/api/users/`
- **Description**: Retrieve a paginated list of all users
- **Authentication**: Required
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `page_size`: Number of items per page (default: 10, max: 100)

**Response Example:**
```json
{
    "count": 25,
    "next": "http://localhost:8000/api/users/?page=2",
    "previous": null,
    "results": [
        {
            "url": "http://localhost:8000/api/users/1/",
            "first_name": "John",
            "last_name": "Doe",
            "username": "johndoe",
            "email": "john@example.com"
        }
    ]
}
```

#### Get User Details
- **GET** `/api/users/{id}/`
- **Description**: Retrieve details of a specific user
- **Authentication**: Required

#### Get Current User
- **GET** `/api/users/me/`
- **Description**: Retrieve details of the authenticated user
- **Authentication**: Required

#### Update User
- **PUT** `/api/users/{id}/`
- **Description**: Update user information
- **Authentication**: Required
- **Content-Type**: `application/json`

**Request Body:**
```json
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
}
```

### Tasks

#### List Tasks
- **GET** `/api/tasks/`
- **Description**: Retrieve a paginated list of tasks
- **Authentication**: Required
- **Query Parameters**:
  - `page`: Page number (default: 1)
  - `page_size`: Number of items per page (default: 10, max: 100)
  - `status`: Filter by status (`pending`, `in_progress`, `completed`, `on_hold`, `cancelled`)
  - `priority`: Filter by priority (`low`, `medium`, `high`, `urgent`)
  - `assigned_to`: Filter by assigned user ID
  - `search`: Search in title and description
  - `ordering`: Order by field (`created_at`, `due_date`, `-created_at`, `-due_date`)

**Response Example:**
```json
{
    "count": 50,
    "next": "http://localhost:8000/api/tasks/?page=2",
    "previous": null,
    "results": [
        {
            "url": "http://localhost:8000/api/tasks/1/",
            "title": "Task Title",
            "status": "pending",
            "priority": "high",
            "estimated_hours": 8,
            "actual_hours": null,
            "created_by": "http://localhost:8000/api/users/1/",
            "assigned_to": ["http://localhost:8000/api/users/2/"],
            "parent_task": null
        }
    ]
}
```

#### Create Task
- **POST** `/api/tasks/`
- **Description**: Create a new task
- **Authentication**: Required
- **Content-Type**: `application/json`

**Request Body:**
```json
{
    "title": "New Task",
    "description": "Task description",
    "status": "pending",
    "priority": "medium",
    "due_date": "2025-12-31T23:59:59Z",
    "estimated_hours": 8,
    "assigned_to": [1, 2],
    "parent_task": null,
    "metadata": {}
}
```

#### Get Task Details
- **GET** `/api/tasks/{id}/`
- **Description**: Retrieve detailed information about a specific task
- **Authentication**: Required

**Response Example:**
```json
{
    "url": "http://localhost:8000/api/tasks/1/",
    "title": "Task Title",
    "description": "Detailed task description",
    "status": "in_progress",
    "priority": "high",
    "due_date": "2025-12-31T23:59:59Z",
    "estimated_hours": 8,
    "actual_hours": "5.50",
    "created_by": "http://localhost:8000/api/users/1/",
    "assigned_to": ["http://localhost:8000/api/users/2/"],
    "parent_task": null,
    "metadata": {},
    "created_at": "2025-09-01T10:00:00Z",
    "updated_at": "2025-09-02T15:30:00Z",
    "is_archived": false,
    "tags": [
        {"name": "frontend"},
        {"name": "urgent"}
    ],
    "comments": [
        {
            "user": "http://localhost:8000/api/users/1/",
            "content": "Task in progress",
            "created_at": "2025-09-02T12:00:00Z"
        }
    ]
}
```

#### Update Task
- **PUT** `/api/tasks/{id}/`
- **PATCH** `/api/tasks/{id}/`
- **Description**: Update task information (PUT for full update, PATCH for partial)
- **Authentication**: Required
- **Content-Type**: `application/json`

#### Delete Task
- **DELETE** `/api/tasks/{id}/`
- **Description**: Delete a task
- **Authentication**: Required

#### Assign/Unassign User to Task
- **GET** `/api/tasks/{id}/assign/`
- **Description**: Get current task assignments
- **Authentication**: Required

**Response Example:**
```json
{
    "assigned_to": ["http://localhost:8000/api/users/2/"]
}
```

- **POST** `/api/tasks/{id}/assign/`
- **Description**: Assign or unassign a user to/from a task (toggles assignment)
- **Authentication**: Required
- **Content-Type**: `application/json`

**Request Body:**
```json
{
    "assigned_to": 2
}
```

#### Task Comments
- **GET** `/api/tasks/{id}/comments/`
- **Description**: Get all comments for a task
- **Authentication**: Required

**Response Example:**
```json
[
    {
        "user": "http://localhost:8000/api/users/1/",
        "content": "This is a comment",
        "created_at": "2025-09-02T12:00:00Z"
    }
]
```

- **POST** `/api/tasks/{id}/comments/`
- **Description**: Add a comment to a task
- **Authentication**: Required
- **Content-Type**: `application/json`

**Request Body:**
```json
{
    "user": 1,
    "content": "New comment on this task"
}
```

## Data Models

### Task Status Options
- `pending`: Pending
- `in_progress`: In Progress  
- `completed`: Completed
- `on_hold`: On Hold
- `cancelled`: Cancelled

### Priority Options
- `low`: Low
- `medium`: Medium
- `high`: High
- `urgent`: Urgent

## Error Responses

### Authentication Required (401)
```json
{
    "detail": "Authentication credentials were not provided."
}
```

### Not Found (404)
```json
{
    "detail": "Not found."
}
```

### Bad Request (400)
```json
{
    "field_name": ["This field is required."]
}
```

### Validation Error (400)
```json
{
    "Error": "user_id is required"
}
```

## Health Check

- **GET** `/health/`
- **Description**: Check API health status
- **Authentication**: Not required

**Response Example:**
```json
{
    "status": "ok"
}
```

## Testing using curl commands

### List Users
```bash
curl -X GET http://localhost:8000/api/users/ -u admin:admin
```

### Get User Details
```bash
curl -X GET http://localhost:8000/api/users/1/ -u admin:admin
```

### Get Current User
```bash
curl -X GET http://localhost:8000/api/users/me/ -u admin:admin
```

### Update User
```bash
curl -X PUT http://localhost:8000/api/users/2/ -u admin:admin -H "Content-Type: application/json" -d '
{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "username": "johndoe"
}'
```

### List Tasks
```bash
curl -X GET "http://localhost:8000/api/tasks/" -u admin:admin
```

<!-- INSERT INTO tasks_task (
    id, title, description, status, priority, due_date, estimated_hours, actual_hours,
    created_by_id, parent_task_id, metadata, created_at, updated_at, is_archived
) VALUES
-- Tareas principales
(1, 'Implementar sistema de autenticación', 
 'Desarrollar un sistema completo de autenticación con JWT, incluyendo login, registro, recuperación de contraseña y gestión de sesiones.', 
 'completed', 'high', '2024-12-15 17:00:00', 40.00, 42.50, 1, NULL, 
 '{"complexity": "high", "technologies": ["Django", "JWT", "Redis"], "review_required": true}', 
 '2024-11-01 09:00:00', '2024-12-16 14:30:00', false), -->

### Create Task
```bash
curl -X POST http://localhost:8000/api/tasks/ -u admin:admin -H "Content-Type: application/json" -d '
{
    "title": "New Task",
    "description": "Task description",
    "status": "pending",
    "priority": "medium",
    "estimated_hours": 8,
    "parent_task": null,
    "metadata": {},
    "created_by": "http://localhost:8000/api/users/1/",
    "assigned_to": ["http://localhost:8000/api/users/2/"]
}'
```

### Get Task Details
```bash
curl -X GET http://localhost:8000/api/tasks/1/ -u admin:admin
```

### Update Task
```bash
curl -X PUT http://localhost:8000/api/tasks/1/ -u admin:admin -H "Content-Type: application/json" -d '
{
    "title": "Updated Task Title",
    "description": "Updated task description",
    "status": "in_progress",
    "priority": "high",
    "estimated_hours": 10,
    "actual_hours": 5.50,
    "created_by": "http://localhost:8000/api/users/1/",
    "assigned_to": ["http://localhost:8000/api/users/2/"],
    "parent_task": null,
    "metadata": {}
}'
```

### Delete Task
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ -u admin:admin
```

### Assign/Unassign User to Task
```bash
curl -X POST http://localhost:8000/api/tasks/2/assign/ -u admin:admin -H "Content-Type: application/json" -d '
{
    "assigned_to": 2
}'
```

### Post a Comment to Task
```bash
curl -X POST http://localhost:8000/api/tasks/2/comments/ -u admin:admin -H "Content-Type: application/json" -d '
{
    "user": 1,
    "content": "This is a comment on the task."
}'
```

### Get Task Comments
```bash
curl -X GET http://localhost:8000/api/tasks/2/comments/ -u admin:admin
```