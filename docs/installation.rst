Installation
============

Install using pip within a virtual environment:

.. code-block:: bash

  $ pip install lexmachina-client


The examples in the quickstart assume a valid bearer token is set in the environment variable ``BEARER_TOKEN``. You can get a bearer token by using the ``/oauth2/token`` endpoint:

.. code-block:: bash

    $ curl -i -X POST 'https://api.lexmachina.com/oauth2/token' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'client_id=<client id>' \
    --data-urlencode 'client_secret=<client secret>' \
    --data-urlencode 'grant_type=client_credentials'


Then set that bearer token in the environment variable:

.. code-block:: bash

    $ export BEARER_TOKEN=<bearer token>


Next: :doc:`quickstart`
