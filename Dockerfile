    # Use a base Python image
    FROM python:3.9-slim-buster

    # Set the working directory inside the container
    WORKDIR /app

    # Copy the requirements file and install dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the Flask application code
    COPY . .

    # Expose the port your Flask app runs on (default is 5000)
    EXPOSE 5000

    # Define the command to run the Flask application
    CMD ["flask", "run", "--host=0.0.0.0"]