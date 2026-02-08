# Use Python 3.11 slim image as the base image
FROM python:3.11-slim

# Set the working directory inside the container to represent the project root
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application code to the backend subdirectory
COPY . /app/backend/

# Expose port 8000 to allow communication to/from the backend
EXPOSE 8000

# Define environment variables with defaults
ENV DATABASE_URL=sqlite:///./test.db
ENV BETTER_AUTH_SECRET=your-super-secret-jwt-key-here-make-sure-it-is-at-least-32-characters-long
ENV DB_ECHO=False

# Set PYTHONPATH to include both the project root and backend directory for proper imports
ENV PYTHONPATH=/app:/app/backend

# Start the application using uvicorn from the backend directory
CMD ["sh", "-c", "cd /app/backend && python -m uvicorn main:app --host 0.0.0.0 --port 8000"]