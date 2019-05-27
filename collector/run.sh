#!/bin/bash

BASEDIR="/data/$(date +"%FT%H%M%z")"
echo "Creating directory ${BASEDIR}..."

mkdir -p ${BASEDIR}
axeman -o ${BASEDIR}
