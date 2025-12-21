<<<<<<< HEAD
from flask import Flask
import socket
import os
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
=======
from flask import Flask, request
import socket
import os
import time
from prometheus_client import (
    Counter,
    Histogram,
    generate_latest,
    CONTENT_TYPE_LATEST
)
>>>>>>> d0954da (Initial compose-prod-app)

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "backend_requests_total",
    "Total number of HTTP requests",
    ["hostname"]
)

<<<<<<< HEAD
@app.route("/")
def hello():
    REQUEST_COUNT.labels(hostname=socket.gethostname()).inc()
    return {
=======
REQUEST_LATENCY = Histogram(
    "backend_request_duration_seconds",
    "Request latency in seconds",
    buckets=(0.1, 0.3, 0.5, 1, 1.5, 2, 3, 5)
)

@app.route("/")
def hello():
    start = time.time()

    response = {
>>>>>>> d0954da (Initial compose-prod-app)
        "message": "Hello from Backend API 🚀",
        "service": os.getenv("SERVICE_NAME", "backend"),
        "hostname": socket.gethostname()
    }

<<<<<<< HEAD
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }
=======
    REQUEST_COUNT.labels(hostname=socket.gethostname()).inc()
    REQUEST_LATENCY.observe(time.time() - start)

    return response

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
>>>>>>> d0954da (Initial compose-prod-app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
