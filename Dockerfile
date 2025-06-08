# Use the official Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the application code to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]
