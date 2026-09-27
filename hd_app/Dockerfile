FROM python:3.11-slim

WORKDIR /app

COPY processor.py .

# Create a non-root user and switch to it - a genuine Docker
# security best practice, avoiding root inside the container
RUN useradd -m appuser
USER appuser

ENTRYPOINT ["python", "processor.py"]