# django-business-service

Business logic microservice that consumes JWT tokens from the auth service.

## Features

- Protected business logic endpoints
- JWT token validation without authentication logic
- Stateless authentication using shared JWT secret

## Endpoints

- `GET /polls/`: Access protected business data

## Usage

Run the service:
```
python manage.py runserver 8002
```

Access protected endpoint with token from auth service:
```bash
curl -X GET http://localhost:8002/polls/ \
  -H "Authorization: Bearer <your_access_token>"
```