#!/usr/bin/env bash

# Build the Docker image
docker build -t delivery-prediction-app .

# Run the Docker container
docker run -p 8501:8501 delivery-prediction-app
