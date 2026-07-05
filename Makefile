IMAGE_NAME=employee-api
IMAGE_TAG=v5
CLUSTER_NAME=employee-cluster

build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .

load:
	kind load docker-image $(IMAGE_NAME):$(IMAGE_TAG) --name $(CLUSTER_NAME)

deploy:
	kubectl apply -f k8s/

test:
	./scripts/smoke-test.sh

clean:
	kubectl delete -f k8s/