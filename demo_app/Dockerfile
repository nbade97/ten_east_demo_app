# Dockerfile for Django
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app/

# Expose the necessary port
EXPOSE 8000

# Define the command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]