# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# System deps (optional, keep image small)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

# Copy dependency manifest and install first (better layer caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the port Flask listens on
EXPOSE 5000

# Set Python to not buffer stdout/err
ENV PYTHONUNBUFFERED=1

# Run the app (Flask dev server is fine for a demo)
CMD ["python", "app.py"]


