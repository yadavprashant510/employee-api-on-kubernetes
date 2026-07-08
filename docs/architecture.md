                Internet
                    │
                    ▼
              NGINX Ingress
                    │
                    ▼
             Kubernetes Service
                    │
                    ▼
             Deployment (2-10 Pods)
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
     ConfigMap              Secret
        │                       │
        └───────────┬───────────┘
                    ▼
              Flask Application
                    │
                    ▼
                  PVC/PV

Prometheus ───────────────► Metrics

Grafana ◄────────────────── Prometheus

```mermaid
flowchart TD

    User[User]

    User --> Ingress[NGINX Ingress]

    Ingress --> Service[Employee Service]

    Service --> Pod1[Employee API Pod 1]
    Service --> Pod2[Employee API Pod 2]

    Pod1 --> PVC[Persistent Volume Claim]
    Pod2 --> PVC

    PVC --> PV[Persistent Volume]

    ConfigMap --> Pod1
    ConfigMap --> Pod2

    Secret --> Pod1
    Secret --> Pod2

    Prometheus --> Pod1

    Grafana --> Prometheus

    Pod1 --> Alloy

    Pod2 --> Alloy

    Alloy --> Loki

    Grafana --> Loki
```