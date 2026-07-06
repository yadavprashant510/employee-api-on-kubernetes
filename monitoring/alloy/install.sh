#!/bin/bash

set -e

kubectl create configmap alloy-config \
  --from-file=config.alloy=monitoring/alloy/config.alloy \
  -n monitoring \
  --dry-run=client -o yaml | kubectl apply -f -

helm upgrade --install alloy grafana/alloy \
  -n monitoring \
  -f monitoring/alloy/values.yaml