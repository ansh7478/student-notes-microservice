from fastapi import FastAPI

app = FastAPI(
    title="Student Notes Microservice",
    description="Cloud Computing Summer Semester 2026",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Student Notes Microservice!"
    }