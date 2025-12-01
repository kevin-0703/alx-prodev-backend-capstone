# Use an official Python image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire backend project
COPY . .

# Expose port 8000 (for Django dev server or gunicorn)
EXPOSE 8000

# Default command
CMD ["gunicorn", "Prodev_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
