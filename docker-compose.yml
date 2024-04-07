# Dockerfile for hosting frontend and backend services on Render

# Stage 1: Build the frontend
FROM python:3.10.8 AS frontend

# Set the working directory for the frontend
WORKDIR /app/frontend

# Copy frontend files to the container
COPY frontend /app/frontend

# Install dependencies for the frontend
RUN pip install --upgrade pip
RUN pip install -r /app/frontend/requirements.txt

# Expose port for the frontend
EXPOSE 8501

# Stage 2: Build the backend
FROM python:3.10.8 AS backend

# Set the working directory for the backend
WORKDIR /app/backend

# Copy backend files to the container
COPY backend /app/backend
COPY data /app/data

# Install dependencies for the backend
RUN pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt

# Expose port for the backend
EXPOSE 8080

# Command to start the backend
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
