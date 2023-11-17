# 3-tier application

## Setup

```sh
# install
brew install minikube
brew install hyperkit

# start
minikube start --driver hyperkit --nodes 4
kubectl taint nodes minikube admin=true:NoSchedule

# stop
minikube stop
minikube delete
```

or:

```sh
# start
k3d cluster create jdp

# stop
k3d cluster delete jdp
```

## Install

```sh
kubectl apply -f ./frontend/frontend-kube-app.yml
kubectl apply -f ./backend/backend-kube-app.yml
kubectl apply -f ./database/postgres-config.yml
kubectl apply -f ./database/postgres-pvc-pv.yml
kubectl apply -f ./database/database-kube-app.yml

kubectl get all -o wide
```

If NodePort does not work:

```sh
kubectl port-forward service/web-httpd-service 80:80
```