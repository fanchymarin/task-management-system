## Test commands

Authentication Endpoints:Authentication Endpoints:
POST /api/auth/register/
POST /api/auth/login/
POST /api/auth/logout/
POST /api/auth/refresh/
User Management:User Management:
GET /api/users/  (list with pagination)
GET /api/users/{id}/
PUT /api/users/{id}/
GET /api/users/me/
Task Management:Task Management:
GET /api/tasks/  (with filtering, search, pagination)
POST /api/tasks/
GET /api/tasks/{id}/
PUT /api/tasks/{id}/
PATCH /api/tasks/{id}/
DELETE /api/tasks/{id}/
Task Operations:Task Operations:
POST /api/tasks/{id}/assign/
POST /api/tasks/{id}/comments/
GET /api/tasks/{id}/comments/
GET /api/tasks/{id}/history/

## Example curl commands