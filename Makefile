IMAGE_NAME=employee-api
IMAGE_TAG=v5
CLUSTER_NAME=employee-cluster


load:
	kind load docker-image $(IMAGE_NAME):$(IMAGE_TAG) --name $(CLUSTER_NAME)

.PHONY: lint test build deploy clean

lint:
	helm lint helm/employee-api

template:
	helm template employee-api ./helm/employee-api

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

deploy:
	helm upgrade --install employee-api ./helm/employee-api \
		--namespace employee-ns \
		--create-namespace

logs:
	kubectl logs -f deployment/employee-api -n employee-ns

clean:
	helm uninstall employee-api -n employee