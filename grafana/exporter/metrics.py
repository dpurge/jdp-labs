import logging
import random
from prometheus_client import Enum, Histogram

healthcheck = ['healthy', 'unhealthy', 'degraded']

foo = Enum(name='foo_health_status', documentation='FOO health', states=healthcheck)
bar = Enum(name='bar_health_status', documentation='BAR health', states=healthcheck)
baz = Enum(name='baz_health_status', documentation='BAZ health', states=healthcheck)

def get_foo():
    logging.info('getting foo metrics')
    foo.state(random.choice(healthcheck))

def get_bar():
    logging.info('getting bar metrics')
    bar.state(random.choice(healthcheck))

def get_baz():
    logging.info('getting baz metrics')
    baz.state(random.choice(healthcheck))
