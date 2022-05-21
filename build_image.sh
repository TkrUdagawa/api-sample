#!/bin/bash

poetry export -f requirements.txt --output requirements.txt
poetry build
docker build -t api-sample:latest .
