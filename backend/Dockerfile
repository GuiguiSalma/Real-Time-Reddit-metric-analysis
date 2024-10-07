FROM python:3.8-slim-buster

WORKDIR /usr/src/app

# Copy everything from the backend directory into the container's working directory
COPY . /usr/src/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "app/main.py"]
