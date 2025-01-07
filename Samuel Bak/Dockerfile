# Use Python 3.10 as base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libxml2-dev libxslt-dev && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the default command to execute the script
CMD ["python", "main.py"]
