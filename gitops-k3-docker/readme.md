# GitOps Pipeline using ArgoCD & Kubernetes

## Overview

This project demonstrates a GitOps-based deployment workflow using ArgoCD and Kubernetes. Application state is managed through a Git repository, and changes are automatically synchronized to the cluster.

---

## Tools Used

* Kubernetes (Minikube/K3s)
* ArgoCD
* Docker
* GitHub

---

## Architecture

GitHub (Source of Truth) → ArgoCD → Kubernetes Cluster

---

## Setup Steps

1. Start Kubernetes cluster:

   ```bash
   minikube start
   ```

2. Install ArgoCD:

   ```bash
   kubectl create namespace argocd
   kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
   ```

3. Access ArgoCD UI:

   ```bash
   kubectl port-forward svc/argocd-server -n argocd 8080:443
   ```

4. Create application in ArgoCD and connect GitHub repo.

5. Enable Auto-Sync for continuous deployment.

---

## GitOps Workflow

1. Update Kubernetes manifests in GitHub
2. Commit and push changes
3. ArgoCD detects changes automatically
4. Kubernetes cluster syncs to desired state

---

## Features

* Automated deployment using GitOps
* Continuous synchronization with GitHub
* Declarative infrastructure management

---

## Deliverables

* Kubernetes manifest files (Deployment & Service)
* ArgoCD sync screenshots
* Demonstration of auto-deployment via Git commits


---

## Conclusion

This project showcases how GitOps enables reliable, automated, and version-controlled application deployments in Kubernetes.
