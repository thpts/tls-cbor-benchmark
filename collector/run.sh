#!/bin/bash

BASEDIR="/data/$(date +"%FT%H%M%z")"
mkdir -p ${BASEDIR}
axeman -o ${BASEDIR}
