from flask import Flask
import logging
import time
from prometheus_client import start_http_server, Counter
from jaeger_client import Config

app = Flask(__name__)

# Logging
logging.basicConfig(level=logging.INFO)

# Prometheus metric
REQUEST_COUNT = Counter('request_count', 'Total Request Count')

# Jaeger tracing
def init_tracer(service):
    config = Config(
        config={
            'sampler': {'type': 'const', 'param': 1},
            'logging': True,
        },
        service_name=service,
    )
    return config.initialize_tracer()

tracer = init_tracer('flask-app')

@app.route("/")
def home():
    with tracer.start_span("request-span"):
        REQUEST_COUNT.inc()
        logging.info("Request received")
        time.sleep(1)
        return "Hello Observability"

if __name__ == "__main__":
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
