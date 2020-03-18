#!/bin/bash
gcloud builds submit --tag gcr.io/cdn-dinoia/tequinity
gcloud run deploy --image gcr.io/cdn-dinoia/tequinity --platform managed



# docker build --rm -f "Dockerfile" -t tequinity:latest .
# docker tag tequinity gcr.io/cdn-dinoia/tequinity:latest
# docker push gcr.io/cdn-dinoia/tequinity:latest
# gcloud run deploy --image gcr.io/cdn-dinoia/tequinity --platform managed

# aplay /usr/share/sounds/purple/alert.wav
# date +"%T"
