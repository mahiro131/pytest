#!/bin/sh
docker run -p 5432:5432 -p 5431:5431 --name db-container --network pytest-network -e POSTGRES_USER=dev -e POSTGRES_PASSWORD=password postgres:10-alpine

