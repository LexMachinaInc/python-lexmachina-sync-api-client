Quickstart
==========

After following the installation instructions and setting your bearer token in the environment variable ``BEARER_TOKEN``, you are ready to start!

For this example, we'll search for a case and get the case details.

First, we'll configure the client:

.. code-block:: python

    import lexmachina
    import os

    configuration = lexmachina.Configuration(
        host="https://api.lexmachina.com", access_token=os.environ["BEARER_TOKEN"]
    )
    api_client = lexmachina.ApiClient(configuration)


Now let's search for a case. For this example, we'll search for case number 9:02-cv-00058-JH, which is Samsung Electronics v. Sandisk Corporation in the U.S. District Court for the Eastern District of Texas.


.. code-block:: python

    case_search_results = fed_cases_api.find_district_case_by_number(
        case_numbers=["9:02-cv-00058-JH"], court="txed"
    )
    case_result = case_search_results[0]










