# ⎈ Helm Guide

## Overview

This project uses Helm to package and manage all Kubernetes resources.

Helm provides:

- Reusable templates
- Environment-specific configuration
- Versioned releases
- Simplified upgrades and rollbacks

Instead of managing multiple Kubernetes YAML files manually, Helm generates Kubernetes manifests dynamically using templates and values.

---

# Chart Structure

```
helm/
└── employee-api/
    ├── Chart.yaml
    ├── values.yaml
    ├── values-dev.yaml
    ├── values-prod.yaml
    └── templates/
        ├── _helpers.tpl
        ├── deployment.yaml
        ├── service.yaml
        ├── ingress.yaml
        ├── configmap.yaml
        ├── secret.yaml
        ├── serviceaccount.yaml
        ├── role.yaml
        ├── rolebinding.yaml
        ├── pvc.yaml
        ├── hpa.yaml
        └── NOTES.txt
```

---

# Chart Components

## Chart.yaml

Contains chart metadata.

Example:

```yaml
apiVersion: v2
name: employee-api
description: Employee Platform Helm Chart
type: application
version: 1.0.0
appVersion: "1.0.0"
```

---

## values.yaml

Contains default configuration.

Example:

```yaml
replicaCount: 2

image:
  repository: your-dockerhub-username/employee-api
  tag: latest
  pullPolicy: IfNotPresent
```

No template should contain hardcoded values.

---

## Templates

Templates generate Kubernetes manifests.

This project templates:

- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- ServiceAccount
- Role
- RoleBinding
- PersistentVolumeClaim
- HorizontalPodAutoscaler

---

## Helper Templates

`_helpers.tpl` contains reusable functions.

Examples:

- Chart Name
- Full Resource Name
- Labels
- Selector Labels
- Service Account Name

Using helper templates avoids duplication across manifests.

---

# Helm Lifecycle

## Install

```bash
helm install employee-api ./helm/employee-api \
    --namespace employee \
    --create-namespace
```

---

## Upgrade

```bash
helm upgrade employee-api ./helm/employee-api
```

---

## Rollback

View release history:

```bash
helm history employee-api -n employee
```

Rollback:

```bash
helm rollback employee-api 1 -n employee
```

---

## Uninstall

```bash
helm uninstall employee-api -n employee
```

---

# Validation

Before every deployment:

Lint:

```bash
helm lint ./helm/employee-api
```

Render templates:

```bash
helm template employee-api ./helm/employee-api
```

Dry Run:

```bash
helm upgrade \
--install employee-api \
./helm/employee-api \
--dry-run \
--debug
```

---

# Environment Configuration

Development

```bash
helm install employee-api \
./helm/employee-api \
-f values-dev.yaml
```

Production

```bash
helm install employee-api \
./helm/employee-api \
-f values-prod.yaml
```

This allows different configurations without changing templates.

---

# Release Management

Useful commands:

List releases

```bash
helm list
```

Release status

```bash
helm status employee-api
```

History

```bash
helm history employee-api
```

Rollback

```bash
helm rollback employee-api <revision>
```

---

# Best Practices

## Keep Templates Generic

Avoid:

```yaml
image:
  repository: employee-api
```

Use:

```yaml
image:
  repository: {{ .Values.image.repository }}
```

---

## Never Hardcode Namespaces

Avoid:

```yaml
namespace: employee
```

Use:

```bash
--namespace employee
```

or

```yaml
{{ .Release.Namespace }}
```

---

## Validate Every Change

Run:

```bash
helm lint

helm template
```

before every deployment.

---

## Keep Secrets Outside Templates

Store sensitive values in:

- Kubernetes Secrets
- External Secrets Operator
- Vault

Avoid hardcoding credentials in templates.

---

# Current Resources

This chart deploys:

- Namespace
- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- PersistentVolumeClaim
- ServiceAccount
- Role
- RoleBinding
- HorizontalPodAutoscaler

---

# Future Improvements

Planned enhancements:

- PodDisruptionBudget
- NetworkPolicy
- Helm Tests
- OCI Helm Registry
- Dependency Charts
- External Secrets
- Cert-Manager Integration
- Argo CD Support