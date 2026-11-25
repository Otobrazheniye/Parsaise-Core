# Base image: Python 3.13 on Debian
FROM python:3.13-slim-trixie

# Python environment
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Application directory inside the container
WORKDIR /app

# PostgreSQL runtime library
RUN apt-get update \
    && apt-get install -y --no-install-recommends libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root application user
RUN useradd --create-home --uid 10001 appuser

# Copy Django project
COPY --chown=appuser:appuser . .

# Run application as a regular user
USER appuser

# Django development port
EXPOSE 8000

# Development server (not for production)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
