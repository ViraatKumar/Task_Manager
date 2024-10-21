# Task Management API

This project implements a Task Management API using Django and Django Rest Framework. It allows users to create tasks, assign them to multiple users, and fetch tasks assigned to a specific user.

## 1. Table of Contents

- Project Setup
- Running the Project
- API Endpoints
- Sample API Requests and Responses
- Test Credentials

## Project Setup

### Prerequisites

Execute the following command to download all dependencies

```
pip install -r requirements.txt
```

### 1. Clone the repository:

```
git clone <repository-url>
cd task_manager
```

### 2. Set up a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate # For Linux/macOS
venv\Scripts\activate # For Windows

```

### 3. Apply database migrations:

```
python manage.py migrate
```

### 4. Run the development server:

```
python manage.py runserver
```

The project will now be available at http://127.0.0.1:8000/.

### 5. Running the Project

Once the project is set up, you can start the development server and make API requests to the following endpoints.

Base URL: http://127.0.0.1:8000/api/

## API Endpoints

Here are the available API endpoints:

- Create Task: POST /api/tasks/
- Assign Task to Users: POST /api/tasks/<task_id>/assign/
- Get Tasks for a Specific User: GET /api/users/<user_id>/tasks/
- Create User: POST /api/users/
- API Overview: GET /api/ (shows all available API endpoints)

### Sample API Requests and Responses

1. Create Task
   . Request: POST /api/tasks/
   . Example Input:

   ```{
   "name": "Complete project documentation",
   "description": "Finalize the API documentation for the task management app.",
   "task_type": "work",
   "status": "pending"
   }
   ```

   - Response:

   ```
   {
   "id": 1,
   "name": "Complete project documentation",
   "description": "Finalize the API documentation for the task management app.",
   "created_at": "2024-10-21T10:00:00Z",
   "task_type": "work",
   "completed_at": null,
   "status": "pending",
   "users": []
   }
   ```

### 2. Assign Task to Users

- Request: POST /api/tasks/<task_id>/assign/
- Example Input:

```
  {
  "users": [1, 2]
  }
```

Response:

```
{
"message": "Task assigned to users"
}
```

### 3. Get Tasks for a Specific User

- Request: GET /api/users/<user_id>/tasks/
- Example Response:

```
   [
   {
   "id": 1,
   "name": "Complete project documentation",
   "description": "Finalize the API documentation for the task management app.",
   "created_at": "2024-10-21T10:00:00Z",
   "task_type": "work",
   "completed_at": null,
   "status": "pending",
   "users": [
   {
   "id": 1,
   "name": "John Doe",
   "email": "john.doe@example.com",
   "mobile": "1234567890"
   }
   ]
   }
   ]
```

### 4. Create User

- Request: POST /api/users/
- Example Input:

```
{
"name": "John Doe",
"email": "john.doe@example.com",
"mobile": "1234567890"
}
```

- Response:

```
{
"id": 1,
"name": "John Doe",
"email": "john.doe@example.com",
"mobile": "1234567890"
}
```

5. API Overview
   - Request: GET /api/
   - Response:
   ```
   {
   "Create Task": "/api/tasks/",
   "Assign Task": "/api/tasks/<int:task_id>/assign/",
   "Get Tasks for User": "/api/users/<int:user_id>/tasks/",
   "Create User": "/api/users/"
   }
   ```
