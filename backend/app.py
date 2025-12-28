from flask import Flask, jsonify
import socket
import os
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "backend_requests_total",
    "Total number of HTTP requests",
    ["hostname"]
)

REQUEST_LATENCY = Histogram(
    "backend_request_duration_seconds",
    "Request latency in seconds",
    buckets=(0.1, 0.3, 0.5, 1, 1.5, 2, 3, 5)
)

http_requests_total = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"]
)

@app.route("/")
def health():
    start = time.time()

    REQUEST_COUNT.labels(hostname=socket.gethostname()).inc()
    http_requests_total.labels("GET", "/", "200").inc()

    REQUEST_LATENCY.observe(time.time() - start)

    return jsonify({
        "message": "Hello from Backend API 🚀",
        "service": os.getenv("SERVICE_NAME", "backend"),
        "hostname": socket.gethostname()
    }), 200


@app.route("/api")
def api():
    start = time.time()

    REQUEST_COUNT.labels(hostname=socket.gethostname()).inc()
    http_requests_total.labels("GET", "/api", "200").inc()

    REQUEST_LATENCY.observe(time.time() - start)

    return jsonify({
        "message": "API response successful",
        "hostname": socket.gethostname()
    }), 200


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
