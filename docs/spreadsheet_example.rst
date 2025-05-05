Adding search results to a spreadsheet
======================================


In the quickstart, we looked for an individual case. In this example, we'll look at a group of cases to see if we can glean any interest information.


For this example, we'll look for Antitrust cases terminated in 2024, do some light analysis, and then add the cases to a spreadsheet.


In the quickstart, you saw how we created an API client object using a context manager and then an object with access to the Federal District case endpoints:

.. code-block:: python

    import lexmachina
    import os

    configuration = lexmachina.Configuration(
        host="https://api.lexmachina.com",
        access_token=os.environ["BEARER_TOKEN"]
    )

    with lexmachina.ApiClient(configuration) as api_client:
        fed_dist_case_api_instance = lexmachina.FederalDistrictCasesApi(api_client)


To simplify the code blocks used in this example, we'll simply refer to the ``fed_dist_case_api_instance`` created in the context manager.


First, we'll create a query for Antitrust cases terminated in 2024. The API returns results in "pages" with each page showing a maximum of 100 results. If your search returns more than 100 results, you'll need to page through them.

.. code-block:: python

    query = {
        "caseTypes": {
            "include": [
            "Antitrust"
            ]
        },
        "dates": {
            "terminated": {
            "onOrAfter": "2024-01-01",
            "onOrBefore": "2024-12-31"
            }
        },
        "page": 1,
        "pageSize": 100
        }


We then page through the results to get the resulting case ids. Some queries return a lot of cases, so we added a print to assure ourselves something is happening while we wait.


.. code-block:: python

    case_ids = []
    done_paging = False
    
    while not done_paging:
        query_response = fed_dist_case_api_instance.query_district_cases(query)
    
        if query_response.cases:
            current_page = query['page']
            print(f'{current_page=}')
            result_case_ids = [caseref.district_case_id for caseref in query_response.cases]
            case_ids += result_case_ids
            query['page'] = current_page + 1
    
        else:
            print(f'Antitrust cases terminated in 2024 has length {len(case_ids)}')
            done_paging=True


We can then get case data for each of case ids. While we could use list comprehension for this, for this example we'll use a loop so we can add prints to assure ourselves something is happening.


.. code-block:: python

    case_data = []

    for case_id in case_ids:
        case_data.append(fed_dist_case_api_instance.get_district_case(case_id))
        if len(case_data) % 50 == 0:
             print(f'{len(case_data)} out of {len(case_ids)} processed')

















