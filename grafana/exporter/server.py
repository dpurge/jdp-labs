import os
import logging

from prometheus_client import start_http_server
from timeloop import Timeloop
from timedelta import timedelta

from metrics import get_foo, get_bar, get_baz

port = int(os.getenv('PORT', 9100))

logging.basicConfig(level=logging.INFO)

tl = Timeloop()
tl.add_job(get_foo, interval=timedelta(seconds=10))
tl.add_job(get_bar, interval=timedelta(seconds=20))
tl.add_job(get_baz, interval=timedelta(seconds=30))


if __name__ == '__main__':
    tl.start(block=True)
    logging.info(f'starting exporter on port {port}')
    start_http_server(port)