# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code into the container
COPY . .

# Set the environment variable to tell where the Flask application is found
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app using gunicorn instead of the development server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
