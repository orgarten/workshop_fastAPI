FROM python:3.12-slim

# Set environment variables

# Write straight to terminal
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends build-essential

COPY __init__.py src/e12deployment/
COPY __init__.py src/
COPY main.py src/e12deployment/
COPY admin.py src/e12deployment/
COPY catalog.py src/e12deployment/
COPY pyproject.toml .

RUN pip install .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "e12deployment.main:app", "--host", "0.0.0.0", "--port", "8000"]