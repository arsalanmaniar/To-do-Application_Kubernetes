#!/bin/bash

# Delete old deployments and pods
kubectl delete deployments --all -n hackathon-app || true
kubectl delete services --all -n hackathon-app || true
kubectl delete pods --all -n hackathon-app || true

# Apply the namespace first
kubectl apply -f namespace.yaml

# Apply the updated deployments and services
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml

# Verify pods reach Running state
echo "Waiting for pods to reach Running state..."
kubectl get pods -n hackathon-app -w

# Verify services are accessible
echo "Checking services:"
kubectl get services -n hackathon-app

# Get minikube service URLs
echo "Minikube service URLs:"
minikube service frontend-service -n hackathon-app
minikube service backend-service -n hackathon-app

# Show final status
echo "Final pod status:"
kubectl get pods -n hackathon-app
echo "Final service status:"
kubectl get services -n hackathon-app