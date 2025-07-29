# Solution Steps

1. 1. Create a new FastAPI project structure with an 'app' directory containing __init__.py, main.py, models.py, schemas.py, crud.py, and database.py.

2. 2. In models.py, define the User SQLAlchemy model with id, name, email, role, and status fields. Add unique and indices as appropriate.

3. 3. In database.py, configure SQLAlchemy to connect to the PostgreSQL database, using environment variables for Docker compatibility.

4. 4. In schemas.py, define Pydantic models UserBase, UserCreate, UserUpdate, and User (with id and orm_mode).

5. 5. In crud.py, add functions for user CRUD: create_user, get_user, get_user_by_email, get_users (with filtering by role and status), update_user, and delete_user. Ensure filters are combined with AND logic in get_users.

6. 6. In main.py, create FastAPI routes for CRUD endpoints and a /users endpoint supporting role and status as query params. Call the appropriate crud functions. Return 404 or 400 errors as needed.

7. 7. Add requirements.txt with FastAPI, Uvicorn, SQLAlchemy, psycopg2-binary, and Pydantic with email support.

8. 8. Write a Dockerfile for the API and reference requirements.txt and the app.

9. 9. Write a docker-compose.yml with two services: db (Postgres) and api (FastAPI app). Use environment variables for credentials, map ports, and create a Docker volume for data persistence.

10. 10. Test the API using the /users endpoint: create users, then query /users?role=admin&status=active and verify only users matching all filters are returned.

11. 11. Ensure the codebase is maintainable, well-structured, and suitable for further extension.

