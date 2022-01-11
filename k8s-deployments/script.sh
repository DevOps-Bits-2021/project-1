kubectl create namespace jenkins
kubectl apply -f jenkins-volume.yaml
kubectl apply -f jenkins-sa.yaml
kubectl create -f jenkins-deployment.yaml -n jenkins
kubectl create -f jenkins-service.yaml -n jenkins