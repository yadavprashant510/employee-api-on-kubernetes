```mermaid
flowchart TB

Developer

--> Git

--> GitHub_Actions

--> Black

--> Flake8

--> Pytest

--> HelmLint[Helm Lint]

--> DockerBuild[Docker Build]

--> Trivy

--> DockerHub

--> HelmDeploy[Helm Upgrade]

--> Kubernetes

--> SmokeTests

--> Success