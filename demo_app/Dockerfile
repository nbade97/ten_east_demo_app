# Dockerfile for Django
FROM python:3.9-slim

# Copy the rest of the application code
COPY . /demo_app/

# Set the working directory
WORKDIR /demo_app

# Copy the requirements file and install dependencies
COPY requirements.txt /demo_app/
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port
EXPOSE 8000

# Define the command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]