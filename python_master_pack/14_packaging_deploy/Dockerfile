# Example multi-stage Dockerfile for a small app
FROM python:3.12-slim AS build
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY . /app
CMD ["python", "09_web_frameworks/fastapi_full_example.py"]
