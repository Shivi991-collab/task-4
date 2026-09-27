# Base image with Python runtime
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file first (better layer caching -
# rebuilds are faster if only app.py changes, not requirements.txt)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY app.py .

# Document which port the container listens on
EXPOSE 5000

# Command to run when the container starts
CMD ["python", "app.py"]