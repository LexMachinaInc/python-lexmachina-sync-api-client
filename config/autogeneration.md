# Generating a Python client

These steps are provided as an example of how to generate a client in the event you would like to generate your own.

We used the python generator from openapi-generator (https://openapi-generator.tech/docs/generators/python/). They provide generators for various languages.

1. Install OpenAI Generator (https://openapi-generator.tech/docs/installation)
2. To get help with options for the python generator: ``openapi-generator-cli config-help -g python``
3. To generate a python client specifying a directory of custom templates: ``openapi-generator-cli generate -g python -c config/open_api_autogenerator_config.yml -i config/openapi.json -o src -t custom_templates``