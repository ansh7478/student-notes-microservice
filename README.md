# Student Notes Microservice

This project is developed for my Cloud Computing subject.

It is a REST API built with FastAPI that allows users to create, view, update and delete student notes. The project is containerized using Docker and deployed to the cloud using Render.

## Technologies that are Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Docker
- Docker Compose
- GitHub
- GitHub Actions
- Render

## Features of this project

- Create notes
- View all notes
- View a single note
- Update notes
- Delete notes
- Input validation
- Swagger API documentation

## Project Structure

   text
app/
    main.py
    database.py
    models.py
    schemas.py
    crud.py

tests/
    test_main.py

Dockerfile
docker-compose.yml
requirements.txt
README.md


## Running the project

Create a virtual environment.

   bash
python -m venv venv


Activate it.

   bash
venv\Scripts\activate


Install the required packages.

   bash
pip install -r requirements.txt


Run the application.

   bash
uvicorn app.main:app --reload
   

Open Swagger documentation:


http://127.0.0.1:8000/docs


## Docker

Build the Docker image.

   bash
docker build -t student-notes-microservice .
   

Run the container.
   
   bash
docker run -p 8000:8000 student-notes-microservice


You can also use Docker Compose.

   bash
docker compose up --build
   

## Testing

The project includes automated tests using pytest.

Run tests with:

   bash
python -m pytest


## Deployment

The application is deployed on Render.

Live Application URL:

https://student-notes-microservice.onrender.com

Swagger Documentation:

https://student-notes-microservice.onrender.com/docs

## GitHub Actions

GitHub Actions automatically runs the tests whenever changes are pushed to the main branch.

## Future Improvements

In the future, this project can be improved by:

- Using PostgreSQL instead of SQLite
- Adding user login
- Adding search functionality
- Improving the user interface

## Student

Anshveer Singh

Subject- Cloud Computing