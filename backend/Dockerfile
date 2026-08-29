FROM python:3.12-slim

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY . .

EXPOSE 8000

# Production: no --reload, and bind to 0.0.0.0 so it's reachable outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
