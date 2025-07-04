# Docker container config
# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --progress-bar off -r requirements.txt


#RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the FastAPI default port
EXPOSE 8000

# Start the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
