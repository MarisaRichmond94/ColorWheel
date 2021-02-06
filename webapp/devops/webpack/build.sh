#!/bin/bash

# Remove old /dist folder
rm -rf ./dist

# Set build mode
DEV_ENVS=( 'local' )
if [[ "${DEV_ENVS[@]}" =~ "${BUILD_ENV}" ]]
then MODE='development'
else MODE='production'
fi

# Move files from the public folder into the dist folder
rsync -a ./public/ ./dist

err=$?
if [ "$err" -ne 0 ] && [ ! -d "$dir" ]; then
  echo "Error copying public folder to assets folder"
  exit "$err"
fi

# Compile JS and SCSS files
npx webpack --config webpack.config.js --progress --mode ${MODE}

err=$?
if [ "$err" -ne 0 ] && [ ! -d "$dir" ]; then
  echo "Error running webpack"
  exit "$err"
fi

NOW=$(date +%s)
cp ./dist/config.js ./dist/config.${NOW}.js
sed -i -e "s/config.js/config.${NOW}.js/" ./dist/index.html
