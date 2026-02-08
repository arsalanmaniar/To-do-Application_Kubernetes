@echo off
REM Delete old deployments and pods
kubectl delete deployments --all -n hackathon-app 2>nul
kubectl delete services --all -n hackathon-app 2>nul
kubectl delete pods --all -n hackathon-app 2>nul

REM Apply the namespace first
kubectl apply -f namespace.yaml

REM Apply the updated deployments and services
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml

REM Verify pods reach Running state
echo Waiting for pods to reach Running state...
kubectl get pods -n hackathon-app -w

REM Verify services are accessible
echo Checking services:
kubectl get services -n hackathon-app

REM Get minikube service URLs
echo Minikube service URLs:
minikube service frontend-service -n hackathon-app
minikube service backend-service -n hackathon-app

REM Show final status
echo Final pod status:
kubectl get pods -n hackathon-app
echo Final service status:
kubectl get services -n hackathon-app