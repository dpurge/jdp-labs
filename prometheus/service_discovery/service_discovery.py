import os
import time
import logging
import json
import timeloop
import datetime

request_timeout = 10
update_interval = int(os.environ['UPDATE_INTERVAL']) if ('UPDATE_INTERVAL' in os.environ) else 30
exporter_address = os.environ['EXPORTER_ADDRESS'] if ('EXPORTER_ADDRESS' in os.environ) else '127.0.0.1'
input_file = os.environ['INPUT_FILE'] if ('INPUT_FILE' in os.environ) else 'metrics'
output_file = os.environ['OUTPUT_FILE'] if ('OUTPUT_FILE' in os.environ) else 'service_discovery.json'

tl = timeloop.Timeloop()
logging.basicConfig(level=logging.INFO)

@tl.job(interval=datetime.timedelta(seconds=update_interval))
def update_service_discovery_file():
    logging.info(f"running service discovery file update, update interval: {update_interval} seconds")

    service_discovery_config = []
    for line in open(input_file, 'rt').readlines():
        parsed_line = line.strip().split(',')
        labels = {}
        for label in parsed_line:
            parts = label.strip().split(':')
            labels[parts[0]] = parts[1]
        service_discovery_config.append({
            "targets": [exporter_address],
            "labels": {
                **labels,
                "__metrics_path__": "/foometric",
                'job': 'foometric'}})
        service_discovery_config.append({
            "targets": [exporter_address],
            "labels": {
                **labels,
                "__metrics_path__": "/barmetric",
                'job': 'barmetric'}})
    
    with open(output_file, 'w') as service_index:
        json.dump(service_discovery_config, service_index, indent=2)

if __name__ == "__main__":
    tl.start(block=True)
