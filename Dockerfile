# Python image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy backend code
COPY backend/ ./backend

# Copy requirements
COPY backend/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy .env
COPY .env .

# Expose port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]