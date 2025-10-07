# todo-app-k8s
Kubernetes deployment repository for Todo App with MySQL database. Includes Dockerfile, manifests, PV/PVC setup, and CI/CD workflow using GitHub Actions + ArgoCD.

# Todo App Kubernetes Deployment

This repository contains all files required to deploy a **Todo App** with **MySQL** database on Kubernetes.

## Project Structure

- `Dockerfile` – Docker image build for todo-app
- `manifests/` – Kubernetes YAML files
  - `todo-app-deployment.yaml`
  - `todo-app-service.yaml`
  - `todo-db-deployment.yaml`
  - `todo-db-service.yaml`
  - `todo-db-pv.yaml`
  - `todo-db-pvc.yaml`
  - `todo-db-init.yaml`
- `.github/workflows/ci.yml` – GitHub Actions workflow

## Author
Komal Vede
