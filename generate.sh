#!/usr/bin/env bash

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/kattakke/swagger/main/swagger.yml \
    -g python-flask \
    -o /local/src/