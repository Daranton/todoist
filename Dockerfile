# Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /todoist

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose FastAPI's port (default is 8000)
EXPOSE 8443

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8443", "--ssl-keyfile=key.pem", "--ssl-certfile=cert.pem"]
