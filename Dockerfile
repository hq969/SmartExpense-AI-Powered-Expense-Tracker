# ---------------------------------
# Use official Python base image
FROM python:3.10-slim

# Set the working directory in container
WORKDIR /app

# Copy all files to container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]


# ---------------------------------
