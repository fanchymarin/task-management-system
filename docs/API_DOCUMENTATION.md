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
- **Example**:
```bash
curl -X GET http://localhost:8000/api/users/ -u admin:admin
```

#### Get User Details
- **GET** `/api/users/{id}/`
- **Description**: Retrieve details of a specific user
- **Authentication**: Required
- **Example**:
```bash
curl -X GET http://localhost:8000/api/users/1/ -u admin:admin
```

#### Get Current User
- **GET** `/api/users/me/`
- **Description**: Retrieve details of the authenticated user
- **Authentication**: Required
- **Example**:
```bash
curl -X GET http://localhost:8000/api/users/me/ -u admin:admin
```

#### Update User
- **PUT** `/api/users/{id}/`
- **Description**: Update user information
- **Authentication**: Required
- **Content-Type**: `application/json`
- **Example**:
```bash
curl -X PUT http://localhost:8000/api/users/2/ -u admin:admin -H "Content-Type: application/json" -d '
{
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "username": "johndoe"
}'
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
- **Example**:
```bash
curl -X GET "http://localhost:8000/api/tasks/" -u admin:admin
```

#### Create Task
- **POST** `/api/tasks/`
- **Description**: Create a new task
- **Authentication**: Required
- **Content-Type**: `application/json`
- **Example**:
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

#### Get Task Details
- **GET** `/api/tasks/{id}/`
- **Description**: Retrieve detailed information about a specific task
- **Authentication**: Required
- **Example**:
```bash
curl -X GET http://localhost:8000/api/tasks/1/ -u admin:admin
```

#### Update Task
- **PUT** `/api/tasks/{id}/`
- **PATCH** `/api/tasks/{id}/`
- **Description**: Update task information (PUT for full update, PATCH for partial)
- **Authentication**: Required
- **Content-Type**: `application/json`
- **Example**:
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

#### Delete Task
- **DELETE** `/api/tasks/{id}/`
- **Description**: Delete a task
- **Authentication**: Required
- **Example**:
```bash
curl -X DELETE http://localhost:8000/api/tasks/1/ -u admin:admin
```

#### Assign/Unassign User to Task
- **GET** `/api/tasks/{id}/assign/`
- **Description**: Get current task assignments
- **Authentication**: Required

- **POST** `/api/tasks/{id}/assign/`
- **Description**: Assign or unassign a user to/from a task (toggles assignment)
- **Authentication**: Required
- **Content-Type**: `application/json`
- **Example**:
```bash
curl -X POST http://localhost:8000/api/tasks/2/assign/ -u admin:admin -H "Content-Type: application/json" -d '
{
        "assigned_to": 2
}'
```

#### Task Comments
- **GET** `/api/tasks/{id}/comments/`
- **Description**: Get all comments for a task
- **Authentication**: Required
- **Example**:
```bash
curl -X GET http://localhost:8000/api/tasks/2/comments/ -u admin:admin
```

- **POST** `/api/tasks/{id}/comments/`
- **Description**: Add a comment to a task
- **Authentication**: Required
- **Content-Type**: `application/json`
- **Example**:
```bash
curl -X POST http://localhost:8000/api/tasks/2/comments/ -u admin:admin -H "Content-Type: application/json" -d '
{
        "user": 1,
        "content": "This is a comment on the task."
}'
```

## Health Check

- **GET** `/health/`
- **Description**: Check API health status
- **Authentication**: Not required
