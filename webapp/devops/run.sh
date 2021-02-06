#!/bin/bash

CURR_PATH=${PWD##*/}

if [[ ("$CURR_PATH" != "devops" && "$CURR_PATH" != "webapp") ]]; then
  echo "Please run from webapp or webapp/devops"
  exit 1
fi

if [ "$CURR_PATH" == "devops" ]; then
  cd ../
fi

BUILD_ENV="local"
export BUILD_ENV

sh devops/webpack/run.sh

err=$?

if [ "$err" -ne 0 ] && [ ! -d "$dir" ]; then
    echo "Error running server"
    exit "$err"
fi
