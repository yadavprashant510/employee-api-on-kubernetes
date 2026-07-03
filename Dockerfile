# -------------------------
# Base Image
# -------------------------
FROM python:3.13-slim

# -------------------------
# Labels
# -------------------------
LABEL maintainer="Prashant"
LABEL project="employee-api"

# -------------------------
# Environment Variables
# -------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# -------------------------
# Working Directory
# -------------------------
WORKDIR /app

# -------------------------
# Install Dependencies
# -------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -------------------------
# Copy Application
# -------------------------
COPY . .

# -------------------------
# Create Non-root User
# -------------------------
RUN useradd --create-home appuser

RUN chown -R appuser:appuser /app

USER appuser

# -------------------------
# Expose Port
# -------------------------
EXPOSE 5000

# -------------------------
# Health Check
# -------------------------
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" || exit 1

# -------------------------
# Start Application
# -------------------------
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]