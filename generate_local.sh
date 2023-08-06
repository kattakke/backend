#!/usr/bin/env bash
cp ../swagger/swagger.yml ./swagger.yml
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i ./local/swagger.yml \
    -g python-flask \
    -o /local/src/