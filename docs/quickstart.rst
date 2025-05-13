Quickstart
==========

After following the :doc:`installation` instructions and setting your bearer token in the environment variable ``BEARER_TOKEN``, you are ready to start!

For this example, we'll search for a case and get its details.

To get detailed information on an individual case, we'll need the Lex Machina id for that case. One way to get the Lex Machina case id is to search for it by case number.

In the first code block, you will see the following steps:

#. We configure the client. In this example we set the value of the bearer token in an environment variable (mostly to prevent contributors to this documentation from accidentally exposing credentials), but you could also feed the value directly to ``access_token``.

#. Using the configured client, we create an object with access to the Federal District Case endpoints.
#. We do a case number search. For this example, we search for the Samsung Electronics v. Sandisk Corporation case with case number 9:02-cv-00058-JH. The case number search ignores judge initials at the end of a case number so they've been left out in the search example below. But they could be left in and the results would be the same. We further refine the search by using the optional court filter to limit our search to cases in the U.S. District Court for the Eastern District of Texas.

Now to get started. In a jupyter notebook or ``ipython`` try out the following:

.. code-block:: python

    import lexmachina
    import os

    configuration = lexmachina.Configuration(
        host="https://api.lexmachina.com",
        access_token=os.environ["BEARER_TOKEN"]
    )

    api_client = lexmachina.ApiClient(configuration)
    
    fed_dist_case_api_instance = lexmachina.FederalDistrictCasesApi(api_client)
    
    case_search_results = fed_dist_case_api_instance.find_district_case_by_number(
        case_numbers=["9:02-cv-00058"], court="txed"
    )


When we look at ``case_search_results``, this search conveniently returns just one result (if we had left out the court filter, it would have returned three results):

.. code-block:: python

    case_search_results
    [
    DistrictCaseNumberSearchResult(
        total_count=1,
        input_case_number='9:02-cv-00058',
        input_court='txed',
        matches=[
            DistrictCaseNumberReference(
                url='https://api.lexmachina.com/district-cases/88',
                district_case_id=88,
                case_number='9:02-cv-00058',
                court='U.S. District Court for the Eastern District of Texas',
                title='Samsung Electronics v. Sandisk Corporation'
            )
        ]
    ]

We can see from the output above the Lex Machina id for the case is 88. We will use that in the endpoint to get data on an individual case:


.. code-block:: python
    
    apple_v_sandisk_case = fed_dist_case_api_instance.get_district_case(88)


Just for example purposes, here is a sampling of data provided for this individual case. You'll see a number of ids that you can then use to get more information on invidual judges, law firms, attorneys, and parties.

.. code-block:: python

    apple_v_sandisk_case.case_type
    ['Patent']

    apple_v_sandisk_case.patents
    [Patent(number='5473563', title='Nonvolatile semiconductor memory'),
    Patent(number='5514889', title='Non-volatile semiconductor memory device and method for manufacturing the same'),
    Patent(number='5546341', title='Nonvolatile semiconductor memory'),
    Patent(number='5642309', title='Auto-program circuit in a nonvolatile semiconductor memory device')]

    apple_v_sandisk_case.judges
    [FederalJudge(name='John H. Hannah Jr.', federal_judge_id=969)]

    apple_v_sandisk_case.law_firms
    [LawFirm(name='Fish & Richardson', law_firm_id=906, client_party_ids=[123]),
    LawFirm(name='McKool Smith', law_firm_id=3425, client_party_ids=[25635]),
    LawFirm(name='Weil, Gotshal & Manges', law_firm_id=4521, client_party_ids=[123]),
    LawFirm(name='Ramey & Flock', law_firm_id=17879, client_party_ids=[25635]),
    LawFirm(name='The Roth Law Firm (rothfirm.com)', law_firm_id=18116, client_party_ids=[111]),
    LawFirm(name='Chandler Law Offices (cmzlaw.net)', law_firm_id=19244, client_party_ids=[123]),
    LawFirm(name='Law Office of Claude E Welch', law_firm_id=38775, client_party_ids=[123]),
    LawFirm(name='Richards & Penn', law_firm_id=7915397, client_party_ids=[123]),
    LawFirm(name='Wilson Sonsini Goodrich & Rosati', law_firm_id=75246884, client_party_ids=[25635])]


This example uses the case number search endpoint to find the case id, but there are other ways to find it, such as the Federal District case query endpoint.

To know your search options, it helps to be familiar with the user-facing Lex Machina website. We recognize that, for new users, the search options are not always immediately obvious. If you would like any help using the Lex Machina API, please contact support@lexmachina.com. 






