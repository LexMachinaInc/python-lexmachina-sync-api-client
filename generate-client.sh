#! /bin/bash
rm README.md
openapi-generator-cli generate -g python -c config/open_api_autogenerator_config.yml -i config/openapi.json -o src -t custom_templates
cp src/lexmachina_README.md README.md
rm src/lexmachina_README.md
