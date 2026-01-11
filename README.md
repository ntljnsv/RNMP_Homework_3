# Workflow

You can run the project either by running the bash script:

```bash

chmod +x run_all.sh
./run_all.sh

```

or running each command manually, as follows:

## 1. Start Containers

```bash
docker-compose up -d
```

Check Kafka logs if needed:

```bash
docker-compose logs -f kafka
```

## 2. Start Spark Prediction App

```bash
docker exec -it spark bash
python3 -m online.prediction
```

## 3. Run the producer script on host machine (or another container):

```bash
python -m online.producer
```

## 4. Run the consumer script on host machine (or another container):


```bash
python -m  online.consumer
```