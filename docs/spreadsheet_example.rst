Adding Case Data to a Spreadsheet
=================================


In this example, we will look at Antitrust cases that terminated in 2024, do some light timing analysis, and add data on those cases to a spreadsheet.

We'll be using `openpyxl <https://openpyxl.readthedocs.io/en/stable/index.html>`_ to add data to an Excel file. You can install this package with the command ``pip install openpyxl``.

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
            print(f'Number of Antitrust cases terminated in 2024: {len(case_ids)}')
            done_paging=True


Armed with case ids, we can then get case data for each of those cases. While we could use more efficient list comprehension, for this example we'll use a loop so we can use a print to get updates on progress.


.. code-block:: python

    case_data = []

    for case_id in case_ids:
        case_data.append(fed_dist_case_api_instance.get_district_case(case_id))
        if len(case_data) % 20 == 0:
             print(f'{len(case_data)} out of {len(case_ids)} processed')


We can now do some analysis. First we'll check which judges saw the most cases among Antitrust cases that terminated in 2024.
We'll also get info on how long these cases lasted.

.. code-block:: python

    from collections import defaultdict

    cases_by_judge = defaultdict(list)

    for c in case_data:
        for j in c.judges:
            cases_by_judge[(j.name, j.federal_judge_id)].append(
                dict(case_id=c.district_case_id, duration=c.dates.terminated - c.dates.filed)
            )


If we check the length of keys in ``cases_by_judge``, we'll see that 378 judges saw these 671 cases. We'll also check one of the judges to see how the data is represented. We see timing is represented in days.

.. code-block:: python

    len(cases_by_judge)
    378

    list(cases_by_judge)[:5]
    [('Mitchell S. Goldberg', 3193),
    ('Edmond E-Min Chang', 3342),
    ('Miriam Goldman Cedarbaum', 406),
    ('Lorna Gail Schofield', 3451),
    ('Joel A. Pisano', 2851)]

    cases_by_judge[('Lorna Gail Schofield', 3451)]
    [{'case_id': 2000009555, 'duration': datetime.timedelta(days=4981)}]

Next, we'll get some timing info:

.. code-block:: python

    all_durations = []

    for case_group in cases_by_judge.values():
        all_durations += [c['duration'].days for c in case_group]
    

If we import the ``statistics`` library, we can check out the mean and median timing values for all Antitrust cases terminated in 2024 (timing is in days):

.. code-block:: python

    import statistics

    round(statistics.mean(all_durations))
    1084

    statistics.median(all_durations)
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

And then check duration stats for the top five judges:

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

For this example, since we focused on judges until now, for the spreadsheet let's focus on law firms and the roles of the parties they represented.


First we'll check the structure of the law firm and party data provided:


.. code-block:: python

    case_data[0].law_firms[:3]
    [LawFirm(name='Kessler Topaz Meltzer & Check', law_firm_id=27, client_party_ids=[257121, 52552843, 231694, 37904, 23356662, 20047290, 24917852, 37648157]),
    LawFirm(name='Hagens Berman Sobol Shapiro', law_firm_id=30, client_party_ids=[231694]),
    LawFirm(name='Berger Montague', law_firm_id=51, client_party_ids=[231694])]

    case_data[0].parties[:3]
    [Party(name='Pennsylvania Employees Benefit Trust Fund', party_id=37904, role='Plaintiff'),
    Party(name='Cephalon, Inc.', party_id=20036179, role='Defendant'),
    Party(name='Vista Health Plan, Inc.', party_id=20047290, role='Plaintiff')]


To translate party ids provided in law firm information to party names, we will create a dictionary mapping party ids to party names:

.. code-block:: python

    parties_by_id_by_case_id = {}

    for c in case_data:
        parties_by_id_by_case_id[c.district_case_id] = {}
        for p in c.parties:
            parties_by_id_by_case_id[c.district_case_id][p.party_id] = p

Now we are ready to create our spreadsheet rows! We'll first determine which columns we want and then add that info for each row.

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
