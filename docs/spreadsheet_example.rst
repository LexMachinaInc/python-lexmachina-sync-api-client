Adding search results to a spreadsheet
======================================


In the :doc:`quickstart`, we looked for an individual case. In this example, we'll look at a group of cases to see if we can glean any interesting information about the group of cases as a whole.


For this example, we'll look at Antitrust cases terminated in 2024, do some light analysis, and add the cases to a spreadsheet. A jupyter notebook with this code can be found in `the examples folder <https://github.com/LexMachinaInc/python-lexmachina-sync-api-client/tree/main/examples>`_


In the :doc:`quickstart`, you saw how we created an API client object which we then used to create an object with access to the Federal District case API endpoints:

.. code-block:: python

    import lexmachina
    import os

    configuration = lexmachina.Configuration(
        host="https://api.lexmachina.com",
        access_token=os.environ["BEARER_TOKEN"]
    )

    api_client = lexmachina.ApiClient(configuration)
    fed_dist_case_api_instance = lexmachina.FederalDistrictCasesApi(api_client)


To get started on our cases search, we'll create a query for Antitrust cases terminated in 2024 in the form of a dictionary. The API returns results in "pages" with each page showing a maximum of 100 results. If your search returns more than 100 results, you'll need to page through them. You'll see in the example below we request the first page to start.

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


Below, we iterate over pages and save the resulting case ids to a list. While this query returns under 700 cases, some queries return a lot of cases, so we use a print to provide progress updates.


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


Armed with case ids, we can then get case data for each of those cases. While we could use more efficient list comprehension, for this example we'll use a loop so we can use a print to get updates on progress.


.. code-block:: python

    case_data = []

    for case_id in case_ids:
        case_data.append(fed_dist_case_api_instance.get_district_case(case_id))
        if len(case_data) % 50 == 0:
             print(f'{len(case_data)} out of {len(case_ids)} processed')


We can now do some analysis. First we'll check which judges saw the most of these cases. 
We'll also get info on how long these cases lasted.

.. code-block:: python

    from collections import defaultdict

    cases_by_judge = defaultdict(list)

    for c in case_data:
        for j in c.judges:
            cases_by_judge[(j.name, j.federal_judge_id)].append(
                dict(case_id=c.district_case_id, duration=c.dates.terminated - c.dates.filed)
            )


The above shows that 378 judges saw these 671 cases.

Next, we'll get some timing info:


.. code-block:: python

    all_durations = []

    for case_group in cases_by_judge.values():
        all_durations += [c['duration'].days for c in case_group]
    

If we import the ``statistics`` library, we can check out the mean and median values:

.. code-block:: python

    import statistics

    round(statistics.mean(sorted_all_durations))
    1084

    statistics.median(sorted_all_durations)
    451


Next, let's check how long these durations were for the judges who saw the most cases.

First let's sort judges by case counts:

.. code-block:: python
    
    case_count_by_judges = [
        (judge_info, len(cases_by_judge[judge_info]))
        for judge_info in cases_by_judge
    ]

    sorted_case_counts_by_judges = sorted(
        case_count_by_judges, key=lambda x: x[-1], reverse=True
    )


Now let's check duration stats for the top five judges:

.. code-block:: python

    for j in sorted_case_counts_by_judges[:5]:
        judge_cases = cases_by_judge[j[0]]
        judge_durations = [c['duration'].days for c in judge_cases]
        print('--------------------')
        print(f'judge name: {j[0][0]}')
        print(f'total num cases: {j[1]}')
        print(f'average duration: {round(statistics.mean(judge_durations))}')
        print(f'median duration: {statistics.median(judge_durations)}')
    

    --------------------
    judge name: Edgardo Ramos
    total num cases: 37
    average duration: 133
    median duration: 95
    --------------------
    judge name: Waverly David Crenshaw Jr.
    total num cases: 34
    average duration: 280
    median duration: 307.0
    --------------------
    judge name: Sarah Elizabeth Pitlyk
    total num cases: 30
    average duration: 1146
    median duration: 1178.0
    --------------------
    judge name: P. Kevin Castel
    total num cases: 23
    average duration: 823
    median duration: 912
    --------------------
    judge name: Sara Elizabeth Lioi
    total num cases: 23
    average duration: 65
    median duration: 71


Now lets add the cases to a spreadsheet. 

For this example, since we focused on judges until now, for the spreadsheet let's focus on something different and say we are most interested in analyzing which law firms and the roles they represented. 

First, lets create the rows. We'll first determine which columns we want and then add that info for each row.

.. code-block:: python

    column_names = [
        'case id',
        'case number',
        'case title',
        'law_firm',
        'law_firm_id',
        'party',
        'party_id',
        'role'
    ]

    rows = []
    rows.append(column_names)

    for c in case_data:
        for law_firm in c.law_firms:
            for party_id in law_firm.client_party_ids:
                party = parties_by_id_by_case_id[c.district_case_id][party_id]
                rows.append(
                    (
                        c.district_case_id,
                        c.case_no,
                        c.title,
                        law_firm.name,
                        law_firm.law_firm_id,
                        party.name,
                        party.party_id,
                        party.role
                    )
                )
            
Now we'll spot check a few of them, including the header to make sure we added it.


.. code-block:: python

    len(rows)
    19083

    rows[0]
    ['case id',
    'case number',
    'case title',
    'law_firm',
    'law_firm_id',
    'party',
    'party_id',
    'role']

    rows[1]
    (97091,
    '2:06-cv-01833-MSG',
    'VISTA HEALTHPLAN, INC. v. CEPHALON, INC. et al',
    'Kessler Topaz Meltzer & Check',
    27,
    'SHIRLEY PANEBIANO',
    257121,
    'Plaintiff')

    rows[10000]
    (2005150350,
    '3:20-cv-05792-JD',
    'In re Google Play Developer Antitrust Litigation',
    "O'Melveny & Myers",
    227639559,
    'Google Asia Pacific PTE. Limited',
    52824280,
    'Defendant')

    rows[-1]
    (2034774512,
    '3:24-cv-09118-VC',
    'Kushner et al v. Chunghwa Picture Tubes, Ltd. et al',
    'Goldman Scarlato & Penny',
    15211344,
    'Barry Kushner',
    10805,
    'Plaintiff')


Now let's add these rows to a spreadsheet.

For this example we'll be using `openpyxl <https://openpyxl.readthedocs.io/en/stable/index.html>`_, which you can install using ``pip install openpyxl``.


.. code-block:: python

    from openpyxl import Workbook

    wb = Workbook()
    ws = wb.active

    for r in rows:
        ws.append(r)
    
    wb.save("antitrust_terminated_2024_law_firms.xlsx")
    wb.close()


The rows are then saved to the spreadsheet in your working directory.

The API returns a lot of data for each case, including data on resolution, damages, and remedies. If you want any help figuring out how to get the information you want, please contact support@lexmachina.com.


Previous: :doc:`quickstart`
