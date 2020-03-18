#!/bin/bash
gcloud builds submit --tag gcr.io/cdn-dinoia/tequinity
gcloud run deploy --image gcr.io/cdn-dinoia/tequinity --platform managed
