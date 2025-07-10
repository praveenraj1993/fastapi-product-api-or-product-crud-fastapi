FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# Point to the app.main module, not just "main"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
