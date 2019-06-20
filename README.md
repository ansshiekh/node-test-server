# node-test-server
This repo contains task submission files for emumba devops position.

# To Check Python Script
* Install dependencies::  
   - pip install -r requirements.txt


* Use the following command to run the script::
    - python automation_script.py 
    - (the script might take some time depending on the connection speed.)
    
    - the node app should be accessible on 
    - localhost:9000

# To Check the Kubernetes Deployement
* Check if the env is set i-e minkube and kubectl is installed::
    - minikube version (If not installed then follow this tutorial https://kubernetes.io/docs/tasks/tools/install-minikube/
    - kubectl version (If not installed then follow this guide: https://docs.bitnami.com/kubernetes/get-started-kubernetes/)
* Then follow the following commands::
    - $ minikube start
    - $ kubectl create -f deployment.yml --save-config
    - $ kubectl expose deployment node-test-deployment --type="LoadBalancer"
    - $ minikube service node-test-deployment (This should open the node app on browser.)
