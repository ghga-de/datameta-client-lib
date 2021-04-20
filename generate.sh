#!/bin/bash

DIR_OF_THIS_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

OPENAPI_SOURCE="https://raw.githubusercontent.com/ghga-de/datameta/main/datameta/api/openapi.yaml"

docker run --rm \
    -v "${DIR_OF_THIS_SCRIPT}:/datameta_client_lib" \
    openapitools/openapi-generator-cli \
        generate \
        -i "${OPENAPI_SOURCE}" \
        -g python \
	-p "infoName=DataMeta Dev Team" \
	-p "infoEmail=leon.kuchenbecker@uni-tuebingen.de" \
	-p "packageVersion=0.12.0p1" \
        --package-name datameta_client_lib \
        -o /datameta_client_lib
