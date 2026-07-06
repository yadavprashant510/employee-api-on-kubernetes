
### Update the helm repo
```sh
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
```

### Install alloy
```sh
helm upgrade --install alloy grafana/alloy \
  -n monitoring \
  --create-namespace
```

### Uninstal Alloy

```sh
helm uninstall alloy -n monitoring