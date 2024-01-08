#!/bin/bash

# login
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 805601245952.dkr.ecr.eu-central-1.amazonaws.com

# build + push
docker build --platform linux/amd64 -t 805601245952.dkr.ecr.eu-central-1.amazonaws.com/my-flask-app:latest .
docker push 805601245952.dkr.ecr.eu-central-1.amazonaws.com/my-flask-app:latest
