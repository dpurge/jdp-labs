import os
import logging
import random

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ForkingMixIn
from urllib.parse import parse_qs, urlparse
from prometheus_client import Metric, Gauge, CollectorRegistry, generate_latest, CONTENT_TYPE_LATEST

port=9256
request_timeout = int(os.environ['REQUEST_TIMEOUT']) if ('REQUEST_TIMEOUT' in os.environ) else 5

class MetricsCollector(object):

    def __init__(self, params):
        self.labels = {k: v[0] for k, v in params.items()}

    def collect(self):
        sample_metric = Metric(
            f'{self.labels['path']}_metric',
            f'{self.labels['path']} metric',
            'gauge')
        sample_metric.add_sample(
            sample_metric.name,
            value = random.random(),
            labels = self.labels)
        yield sample_metric

        up_metric = Metric(
            f'{self.labels['path']}_up',
            f'{self.labels['path']} exporter is up',
            'gauge')
        up_metric.add_sample(
            up_metric.name,
            value = random.random(),
            labels = self.labels)
        yield up_metric

def collect_metrics(params):
    registry = CollectorRegistry(auto_describe=False)
    registry.register(MetricsCollector(params))
    return generate_latest(registry)

class MetricsExporterHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    paths = {
        '/foometric': ['foometric'],
        '/barmetric': ['barmetric']}

    def send_data(self, code, content_type, data):
        self.send_response(code)
        self.send_header('Content-Type', content_type)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path in self.paths.keys():
            params = {
                **parse_qs(url.query),
                'path': self.paths[url.path]}
            logging.info(f'running collector {self.paths[url.path]}')
            self.send_data(200, CONTENT_TYPE_LATEST, collect_metrics(params))
        elif url.path == '/':
            logging.info('running index page')
            with open('/app/index.html', 'rb') as index:
                self.send_data(200, 'text/html;charset=utf-8', bytes(index.read()))
        else:
            logging.info(f"Call to non-existing page {url.path}")
            self.send_response(404)
            self.end_headers()

class ForkingHTTPServer(ForkingMixIn, HTTPServer):
    pass

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("starting metrics exporter")

    server = ForkingHTTPServer(
        ('', port),
        MetricsExporterHandler)

    server.serve_forever()

