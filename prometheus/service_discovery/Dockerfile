FROM python:3.12-slim

RUN mkdir -p /app

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY service_discovery.py /app

ENTRYPOINT ["/usr/local/bin/python", "/app/service_discovery.py"]

