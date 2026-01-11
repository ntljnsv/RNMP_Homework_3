#!/usr/bin/env bash
set -e 

echo "=== 1. Starting Docker containers ==="
docker-compose up -d

sleep 20 

echo "=== 1. Running producer script ==="
python -m online.producer & 

echo "=== 2. Running consumer script ==="
python -m online.consumer

echo "=== 3. Starting Spark Prediction App ==="
docker exec -d spark bash -c "python3 -m online.prediction"

# Script will exit when consumer is stopped
