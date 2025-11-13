# Use a lightweight official Python base image
FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered output (useful for logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set a working directory inside the container
WORKDIR /app

# Install system dependencies needed for psycopg2-binary and general builds
# (libpq and gcc are not strictly necessary for psycopg2-binary, but helpful for extensions)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first to leverage Docker layer caching
# If you keep requirements in app/requirements.txt, copy that path
COPY app/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port uvicorn will listen on
EXPOSE 8000

# Default command to run the FastAPI app using uvicorn
# app.main:app -> module:object
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
