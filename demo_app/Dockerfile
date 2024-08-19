# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apt-get update && apt-get install -y gcc

# Copy the requirements file and install dependencies
COPY requirements.txt /demo_app/
RUN pip install --no-cache-dir -r /demo_app/requirements.txt

# Copy the rest of the application code
COPY . /demo_app/

# Set the working directory
WORKDIR /demo_app

# Expose the necessary port
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]