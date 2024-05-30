import os
import logging

from prometheus_client import start_http_server
from timeloop import Timeloop
from datetime import timedelta

from metrics import get_foo, get_bar, get_baz

port = int(os.getenv('PORT', 9100))

logging.basicConfig(level=logging.INFO)

tl = Timeloop()
tl.job(interval=timedelta(seconds=10))(get_foo)
tl.job(interval=timedelta(seconds=20))(get_bar)
tl.job(interval=timedelta(seconds=30))(get_baz)


if __name__ == '__main__':
    logging.info(f'starting exporter on port {port}')
    start_http_server(port)
    tl.start(block=True)