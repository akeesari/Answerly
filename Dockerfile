# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Create and activate virtual environment
RUN python -m venv venv
RUN . venv/bin/activate && pip install --upgrade pip

# Install Python dependencies
RUN . venv/bin/activate && pip install -r requirements.txt

# Streamlit runs on port 8501
EXPOSE 8501

# Run the app
CMD ["venv/bin/streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
