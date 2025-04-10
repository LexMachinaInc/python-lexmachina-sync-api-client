# Autogenerate a Python client

These steps are provided as an example of how to generate a client in the event you would like to autogenerate your own.

We used the python generator from openapi-generator (https://openapi-generator.tech/docs/generators/python/). They provide generators for various lanugages.

1. Install OpenAI Generator (https://openapi-generator.tech/docs/installation)
2. Update the openapi schema json file if needed.
3. Update the package version in the config yaml if needed
4. Make note of where the config and open API schema json files are located relative to where you will run the autogeneration command.
5. To get help with options: openapi-generator-cli config-help -g python
6. To autogenerate python client specifying custom templates: ``openapi-generator-cli generate -g python -c config/open_api_autogenerator_config.yml -i config/openapi.json -o src -t custom_templates``