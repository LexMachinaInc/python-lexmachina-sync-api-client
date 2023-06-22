# python-lexmachina-api-client
Python Client for Lex Machina Litigation Analytics API 

This package provides a client to access the Lex Machina API for legal analytics. Access and documentation are provided at the [Lex Machina API Developer Portal](https://developer.lexmachina.com/).

# Getting Started

1. Create a new venv with the command `python3 -m venv /path/to/new/virtual/environment`
2. Run `python3 -m pip install --upgrade pip setuptools wheel`
3. Install package with `pip3 install lexmachina-client` .
1. Create an app and get the client key and secret via the [directions here](https://developer.lexmachina.com/default/docs/generating_oauth_credentials).

1. In your project directory create a directory `config` and inside that create a file named config.ini . Populate using the below values and the key and secret from above. The below values for URLS should be used if you are using Lex Machina's production API. If you are testing this out with the [sandbox API](https://developer.lexmachina.com/default/documentation/lexmachina-sandbox) then you should use `base_url = https://api.sandbox.lexmachina.com`

    ```
    [URLS]
    token_url = /oauth2/token
    base_url = https://api.lexmachina.com

    [CREDENTIALS]
    client_id = "CLIENT_ID"
    client_secret ="CLIENT_SECRET"
    ```

1. To execute API calls you will use the LexMachinaClient of this package. This is discussed in detail later.

    For each of these, you first create the object then call the functions on that object.


# Lex Machina Client

The LexMachinaClient object is the main way to interact with the Lex Machina API.



## Instantiating the LexMachinaClient object

If called with no parameter in the constructor, the config file will be loaded from the `config` directory created earlier.
 
```python

from lexmachina import LexMachinaClient

client = LexMachinaClient()
```

If passed a string for a file path, the config file will be loaded from that location. 

```python
client = LexMachinaClient("../config/config.ini")
```


## GET functions from LexMachinaClient

The functions provided fall into several classes:
1. Lists of resources
2. Lookup by ID
3. Searches

## Lists of Resources

These functions are available from LexMachinaClient. Each returns a JSON object describing resources. 

- LexMachinaClient.list_case_resolutions()
- LexMachinaClient.list_case_tags()
- LexMachinaClient.list_case_types()
- LexMachinaClient.list_courts()
- LexMachinaClient.list_damages()
- LexMachinaClient.list_events()
- LexMachinaClient.list_judgment_sources()


## Lookup by ID(s)
These functions are available from LexMachinaClient. Each takes a single integer or an array of up to 100 integers where the parameter is the Lex Machina ID for that record. It will return a JSON object or an array of objects representing the data for that type of record.

- LexMachinaClient.get_attorneys()
- LexMachinaClient.get_district_cases()
- LexMachinaClient.get_federal_judges()
- LexMachinaClient.get_law_firms()
- LexMachinaClient.get_magistrates()
- LexMachinaClient.get_parties()
- LexMachinaClient.get_patents()

