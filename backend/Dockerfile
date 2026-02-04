FROM python:3.12-slim

WORKDIR /app

# Copy only requirements first for better layer caching
COPY requirements.txt .

# Fix ImageMagick CVE-2026-23876 and CVE-2026-22770
RUN apt-get update && apt-get install -y --no-install-recommends \
    imagemagick=8:7.1.1.43+dfsg1-1+deb13u5 \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
