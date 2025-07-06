FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

EXPOSE 5004
CMD ["python", "app.py"]