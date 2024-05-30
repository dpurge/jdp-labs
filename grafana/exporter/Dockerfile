FROM python:3.8.1-slim

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py /app/

ENTRYPOINT ["/usr/local/bin/python", "/app/server.py"]
