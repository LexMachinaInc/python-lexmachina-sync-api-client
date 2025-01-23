1. Update openapi schema json file.
2. Make note of where the config and open API schema json files are located relative to where you will run the autogeneration command.
3. Config notes
    - If you want to generate source code only, add this line to the config yaml: ``generateSourceCodeOnly: True``
    - Update the package version in the config yaml if needed
    - To get help on config options: `openapi-generator-cli config-help -g python`
4. To autogenerate client (example): `openapi-generator-cli generate -g python -c open_api_generator_config/config.yml -i src/lexmachina/openapi.json -o src/lexmachina/v2` 