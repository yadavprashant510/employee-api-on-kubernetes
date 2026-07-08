# 🔧 Troubleshooting Guide

This document contains the real issues encountered while building the Employee Platform and how they were resolved.

---

# 1. Pod Fails with `runAsNonRoot`

## Error

```text
container has runAsNonRoot and image has non-numeric user (appuser)
```

## Root Cause

The Docker image was using a named user while the Kubernetes `securityContext` expected a numeric user ID.

## Solution

Ensure the Docker image and Kubernetes `securityContext` use the same non-root UID.

Example:

```yaml
securityContext:
  runAsUser: 1000
  runAsNonRoot: true
```

Verify the image user:

```bash
docker inspect employee-api:latest
```

---

# 2. PersistentVolumeClaim Not Found

## Error

```text
0/1 nodes are available:
persistentvolumeclaim "employee-pvc" not found
```

## Root Cause

The Deployment referenced a PVC that had not been created.

## Solution

Verify the PVC exists:

```bash
kubectl get pvc -n employee
```

Verify the Deployment references the correct claim.

```yaml
persistentVolumeClaim:
  claimName: employee-api-pvc
```

---

# 3. Loki Installation Failed

## Error

```text
Please define
loki.storage.bucketNames.chunks
```

## Root Cause

Required storage configuration was missing from `values.yaml`.

## Solution

Update the Loki values file with the required storage configuration before installation.

---

# 4. Alloy Configuration Error

## Error

```text
illegal character '#'
```

## Root Cause

The generated `config.alloy` file contained comments.

Grafana Alloy configuration does not support YAML comments because it uses its own configuration language.

## Solution

Remove comments from the generated configuration.

Incorrect:

```text
# This is Alloy configuration
```

Correct:

```
logging {
    level = "info"
}
```

---

# 5. Helm Namespace Error

## Error

```text
namespaces "employee-ns" not found
```

## Root Cause

Namespace names were hardcoded inside Helm templates.

## Solution

Remove hardcoded namespaces.

Install using:

```bash
helm upgrade --install employee-api \
./helm/employee-api \
--namespace employee \
--create-namespace
```

---

# 6. Docker Hub Authentication Failed

## Error

```text
authentication required

access token has insufficient scopes
```

## Root Cause

Docker Hub Personal Access Token did not have the required permissions.

## Solution

Generate a new Personal Access Token with Read, Write, and Delete permissions.

Store the token as a GitHub Actions secret.

---

# 7. GitHub Actions Failed Locally

## Error

```text
ReadableStream is not defined
```

## Root Cause

The local Act runner used an outdated Node.js image.

## Solution

Use a newer runner image or update the action version to support the required Node.js runtime.

---

# 8. Readiness Probe Failed

## Symptoms

Pods remained in the `NotReady` state.

## Root Cause

Application startup took longer than the probe configuration allowed.

## Solution

Increase:

- initialDelaySeconds
- failureThreshold

or add a Startup Probe.

---

# 9. Liveness Probe Restart Loop

## Symptoms

Container restarted continuously.

## Root Cause

The liveness probe executed before the application was fully initialized.

## Solution

Use a Startup Probe to protect slow-starting applications.

---

# 10. HPA Not Scaling

## Symptoms

HorizontalPodAutoscaler remained at one replica.

## Root Cause

Resource requests were not defined.

## Solution

Configure CPU and memory requests.

```yaml
resources:
  requests:
    cpu: 100m
    memory: 128Mi
```

---

# Useful Commands

## Describe Pod

```bash
kubectl describe pod <pod-name> -n employee
```

---

## View Logs

```bash
kubectl logs <pod-name> -n employee
```

---

## Previous Container Logs

```bash
kubectl logs <pod-name> --previous
```

---

## Check Events

```bash
kubectl get events -n employee --sort-by=.metadata.creationTimestamp
```

---

## Verify Helm Resources

```bash
helm status employee-api -n employee
```

---

## Render Helm Templates

```bash
helm template employee-api ./helm/employee-api
```

---

# Debugging Strategy

Whenever an issue occurs, follow this order:

```text
Application

↓

Container

↓

Pod

↓

Deployment

↓

Service

↓

Ingress

↓

Cluster
```

This top-down approach helps isolate problems efficiently.