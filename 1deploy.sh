#!/bin/bash
docker build --rm -f "Dockerfile" -t tequinity:latest .
# docker tag tequinity gcr.io/cdn-dinoia/tequinity:latest
# docker push gcr.io/cdn-dinoia/tequinity:latest
# gcloud run deploy --image gcr.io/cdn-dinoia/tequinity --platform managed
docker run --rm -it tequinity:latest