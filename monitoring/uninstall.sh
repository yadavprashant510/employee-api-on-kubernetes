#!/bin/bash

helm uninstall monitoring -n monitoring

kubectl delete namespace monitoring