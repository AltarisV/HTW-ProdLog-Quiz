# Use an official Python image as a base
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements into the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the working directory
COPY . .

# Set the environment variable to run Flask in production mode
ENV FLASK_ENV=production

# Expose the port the app will run on
EXPOSE 7007

# Command to run the app
CMD ["python", "app.py"]
