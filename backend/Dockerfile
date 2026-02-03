FROM python:3.12

WORKDIR /app
COPY . /app/

# Fix ImageMagick CVE-2026-23876 and CVE-2026-22770
RUN apt-get update && apt-get install -y --no-install-recommends \
    imagemagick=8:7.1.1.43+dfsg1-1+deb13u5 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
