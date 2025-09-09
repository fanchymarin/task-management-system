# Decisions

This document outlines the key decisions made during the development of the Task Management System project. It serves as a reference for the chosen technologies, architectural patterns, and implementation strategies.

## Features status

### Docker Infrastructure

#### Required Services

- [x] PostgreSQL 15+ database
- [x] Redis 7+ for caching and Celery broker
- [x] Django application server
- [ ] Celery worker for background tasks
- [ ] Celery beat for scheduled tasks

Celery and Celery Beat were not a priority in terms of services.

#### Docker Requirements

- [x] Create your own  docker-compose.yml  from scratch
- [x] Multi-stage Dockerfiles for optimized images
- [x] Environment variables via  .env  file
- [x] Health checks for all services
- [x] Proper service dependencies and startup order
- [x] Volume persistence for database data
- [x] Automatic database migrations on startup
- [x] Network configuration for inter-service communication
- [x] Proper logging configuration

### API Design

#### Endpoints

- [ ] POST /api/auth/register/
- [x] POST /api/auth/login/
- [x] POST /api/auth/logout/
- [ ] POST /api/auth/refresh/

Endpoints for user registration and token refresh were not implemented in favor of a simpler session-based authentication approach using Django REST Framework's built-in authentication system.

#### User Management

- [x] GET /api/users/  (list with pagination)
- [x] GET /api/users/{id}/
- [x] PUT /api/users/{id}/
- [x] GET /api/users/me/

#### Task Management

- [x] GET /api/tasks/  (with filtering, search, pagination)
- [x] POST /api/tasks/
- [x] GET /api/tasks/{id}/
- [x] PUT /api/tasks/{id}/
- [x] PATCH /api/tasks/{id}/
- [x] DELETE /api/tasks/{id}/

#### Task Operations

- [x] POST /api/tasks/{id}/assign/
- [x] POST /api/tasks/{id}/comments/
- [x] GET /api/tasks/{id}/comments/
- [ ] GET /api/tasks/{id}/history/

### PostgreSQL Database with Django ORM

#### Required Models

- [x] User (extend Django AbstractUser)
- [x] Task
- [x] Comment
- [x] Tag
- [ ] TaskAssignment (through model)
- [ ] TaskHistory (audit log)
- [ ] Team
- [ ] TaskTemplate

TaskAssignment, TaskHistory, Team, and TaskTemplate models were not implemented to keep the project scope manageable.

### Celery Background Tasks

- [ ] `send_task_notification(task_id, notification_type)`
- [ ] `generate_daily_summary()`
- [ ] `check_overdue_tasks()`
- [ ] `cleanup_archived_tasks()`
- [ ] Schedule tasks using Celery Beat

### Frontend Application

- [x] User authentication (login/logout)
- [x] Task list view
- [x] Task detail view
- [x] Task creation form
- [ ] Use Django templating engine for server-side rendering

The frontend application was tweaked for the project's needs using Django REST Framework's browsable API, thus Django templates were not implemented.

> [!TIP]
> Visit this [GitHub repository](https://github.com/fanchymarin/invoice-management-system/) where I showcase a more complex implementation of Django templates.

## Key Decisions

The most relevant decision I made was to use Django REST Framework for completing this task. It's a framework I hadn't worked with before but wanted to test for this project. Although I could have chosen an approach using `Views` and `QuerySets`, trying the framework allowed me to glimpse the trade-offs of both approaches.

I believe that on this occasion and with more time, I would have achieved more ad-hoc results by avoiding the framework. I could also have customized the frontend more using Django templates. However, using Django REST Framework allowed me to focus on logic and project structure, setting aside implementation details that the framework already solves.