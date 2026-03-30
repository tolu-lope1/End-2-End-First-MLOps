# 1. Use the official python image with the correct tag syntax
# 'slim' is recommended for ML to keep the image size small
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt .

# 4. Install dependencies
# --no-cache-dir keeps the image lean by not storing the pip cache
RUN pip install --no-cache-dir -r requirements.txt

# 5. Now copy the rest of your application code
COPY . /app

# 6. Expose the port FastAPI/Uvicorn will run on
EXPOSE 8000

# 7. Start the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]