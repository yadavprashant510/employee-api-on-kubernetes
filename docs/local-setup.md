# 🚀 Local Development Setup

This guide explains how to set up the Employee Platform on your local machine using Docker, Kind, Helm, and Kubernetes.

---

# Prerequisites

Install the following tools before proceeding.

| Tool | Version |
|------|---------|
| Git | Latest |
| Docker Desktop | Latest |
| Kind | Latest |
| kubectl | v1.30+ |
| Helm | v3.16+ |
| Python | 3.12 |

Verify installation:

```bash
git --version
docker --version
kind version
kubectl version --client
helm version
python3 --version
```

---

# Clone Repository

```bash
git clone https://github.com/<your-github-username>/employee-platform.git

cd employee-platform
```

---

# Create Kind Cluster

```bash
kind create cluster --config kind/kind-config.yaml
```

Verify:

```bash
kubectl get nodes
```

---

# Build Docker Image

```bash
docker build -t employee-api:latest .
```

Load the image into Kind:

```bash
kind load docker-image employee-api:latest --name employee-cluster
```

---

# Install NGINX Ingress

```bash
kubectl apply -f \
https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
```

Wait until all pods are ready.

```bash
kubectl get pods -n ingress-nginx
```

---

# Deploy Application

```bash
helm upgrade --install employee-api \
./helm/employee-api \
--namespace employee \
--create-namespace
```

Verify:

```bash
kubectl get all -n employee
```

---

# Verify Application

```bash
kubectl get ingress -n employee
```

Access:

```
http://employee.local
```

---

# Install Monitoring Stack

Install kube-prometheus-stack.

```bash
helm upgrade --install monitoring \
prometheus-community/kube-prometheus-stack \
-n monitoring \
--create-namespace
```

---

# Install Loki

```bash
helm upgrade --install loki \
grafana/loki \
-n monitoring \
-f monitoring/loki/values.yaml
```

---

# Install Grafana Alloy

```bash
helm upgrade --install alloy \
grafana/alloy \
-n monitoring \
-f monitoring/alloy/values.yaml
```

---

# Access Grafana

```bash
kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring
```

Open:

```
http://localhost:3000
```

---

# Verify Monitoring

Confirm:

- Application is reachable.
- Metrics appear in Prometheus.
- Logs appear in Loki.
- Dashboards load in Grafana.

---

# Cleanup

Remove the application:

```bash
helm uninstall employee-api -n employee
```

Delete the Kind cluster:

```bash
kind delete cluster --name employee-cluster
```