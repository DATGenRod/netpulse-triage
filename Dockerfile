# Use an official lightweight Python runtime
FROM python:3.11-slim

# Install system network utilities required for infrastructure diagnostics
RUN apt-get update && apt-get install -y \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Optimize environment for real-time log ingestion
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy the local application code
COPY ./app /app

# Run the support automation engine
CMD ["python", "main.py"]
