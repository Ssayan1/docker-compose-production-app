<<<<<<< HEAD
# Production-Grade Docker Compose Application

A production-style microservices application built with Docker Compose, featuring
frontend, backend, ingress routing, health checks, scaling, and observability.

---

## 🚀 Architecture Overview

- Frontend: Nginx-based UI service
- Backend: Python Flask API
- Ingress: Nginx reverse proxy
- Networking: Docker bridge network
- Observability: Prometheus metrics
- Scaling: Multiple backend replicas

---

## Architecture Diagram (conceptual)

```lua
Browser
   |
   v
[ Nginx Ingress ]
   |
   +--> Frontend (Nginx)
   |
   +--> Backend (Flask, scaled)
```

---

## 🛠️ Tech Stack

- Docker & Docker Compose
- Python (Flask)
- Nginx
- Prometheus
- Linux networking concepts

---

## ⚙️ Features Implemented

- Multi-container Docker Compose setup
- Path-based routing using Nginx ingress
- Service discovery via Docker DNS
- Backend health checks
- Horizontal scaling (--scale)
- Prometheus metrics endpoint
- Graceful failure handling
- Environment-based configuration

---

## ▶️ How to Run
=======
# Production-Style Microservices App (Docker → Kubernetes)

## 🔥 Overview
This project demonstrates a **production-grade DevOps workflow**:
- Containerized microservices
- Docker Compose for local orchestration
- Kubernetes migration with Ingress
- Monitoring using Prometheus & Grafana

Built as part of my preparation for a **Junior Cloud / DevOps Engineer role**.

---

## 🧱 Architecture

Frontend (Nginx)
        |
Ingress (Nginx)
        |
Backend (Flask API)
        |
Prometheus → Grafana

---

## ⚙️ Tech Stack
- Docker, Docker Compose
- Kubernetes (Minikube)
- Nginx (Reverse Proxy / Ingress)
- Flask (Backend API)
- Prometheus (Monitoring)
- Grafana (Visualization)

---

## 🚀 Features
- Stateless backend with multiple replicas
- Load balancing via Kubernetes Service
- Ingress-based routing (`/` → frontend, `/api` → backend)
- Application metrics exposed at `/metrics`
- Prometheus scraping backend metrics
- Grafana dashboards for visualization
- Health checks and service dependency management

---

## 🐳 Docker Compose (Local)

 ▶️ How to Run
>>>>>>> d0954da (Initial compose-prod-app)

```bash
docker compose up -d
```
Access:

<<<<<<< HEAD
- Application: http://localhost:8080
- Backend API: http://localhost:8080/api
- Metrics: http://localhost:5000/metrics
=======
- Frontend: http://localhost:8080
- Backend: http://localhost:5000

---

## ☸️ Kubernetes (Minikube)

```bash
minikube start
kubectl apply -f k8s/
```
Ingress:

```bash
http://app.local
http://app.local/api
```
>>>>>>> d0954da (Initial compose-prod-app)

---

## 🔁 Scaling Backend

```bash
docker compose up -d --scale backend=3
```

---

<<<<<<< HEAD
## 🧪 Health Checks

Backend service includes health checks to ensure only healthy containers serve traffic.

---

## 📊 Observability

- Exposes Prometheus-compatible metrics
- Ready for Grafana dashboards

=======
## 📊 Monitoring

- Prometheus UI
- Grafana dashboards
- Backend metrics scraped automatically

---

## 📸 Screenshots

See /screenshots directory:

- Application UI
- Prometheus targets
- Grafana dashboards
>>>>>>> d0954da (Initial compose-prod-app)
---

## 🧠 What I Learned

<<<<<<< HEAD
- Docker networking and service discovery
- Reverse proxy behavior and routing issues
- Debugging 502 / 301 / DNS failures
- Container health checks and dependency handling
- Production-style Compose patterns

---

## 🎯 Why This Project Matters

This project demonstrates real-world DevOps skills including debugging,
service orchestration, and production readiness — beyond basic container usage.
=======
- Container image lifecycle
- Service discovery in Docker & Kubernetes
- Ingress vs reverse proxy
- Debugging networking issues
- Production-style monitoring setup

---

## 🎯 Next Improvements

- Helm charts
- Horizontal Pod Autoscaling
- CI/CD pipeline
- Cloud deployment (AWS / GCP)
>>>>>>> d0954da (Initial compose-prod-app)
