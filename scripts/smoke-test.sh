#!/bin/bash

set -x # debug mode

kubectl get pods -n employee

kubectl get ingress -n employee

kubectl get svc -n employee

kubectl get hpa -n employee

kubectl top pods

curl http://employee.local/health