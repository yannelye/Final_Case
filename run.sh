#!/usr/bin/env bash
docker build -t comunidadconnect:latest .
docker run --rm -p 8080:8080 --env-file .env.example comunidadconnect:latest
