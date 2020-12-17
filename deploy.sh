kubectl delete -f worker-deployment.yaml 
kubectl delete -f producer-deployment.yaml 

echo "pushing to docker"
docker build  -t furkanax/worker:latest .
docker push  furkanax/worker:latest
echo "pushed"

kubectl apply -f worker-deployment.yaml
sleep 3 
kubectl apply -f producer-deployment.yaml 

