FROM python:3.12-slim

RUN mkdir -p /app

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY metrics_exporter.py /app
COPY index.html /app

ENTRYPOINT ["/usr/local/bin/python", "/app/metrics_exporter.py"]
