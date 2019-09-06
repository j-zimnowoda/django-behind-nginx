# django-behind-nginx

The aim of this project is to provide a tool that answers a question "What if I put my Django project behind nginx server?".

By calling its API endpoint you can get to know about:
- see HTTP headers set by reverse proxy server
- obtaining canonical URLs


# Docker

Build for gcloud

docker build  -t gcr.io/django-gke-251916/django-diagnostics ./
docker push gcr.io/django-gke-251916/django-diagnostics
