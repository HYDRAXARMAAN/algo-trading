# Use official Python image as base
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy dependencies file first for cache optimization
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app source code
COPY ./app ./app

# Set environment variables (can also use .env or docker-compose)
ENV FLASK_APP=app/app.py

# Expose port for Flask
EXPOSE 5000

# Run the Flask app
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
