# Using a small official Python image
FROM python:3.11-slim

# Create and use application folder inside  container
WORKDIR /app

# Copy the requirements file first
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the complete project into the container
COPY . .

# Inform the Docker that the application uses port 8000
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]