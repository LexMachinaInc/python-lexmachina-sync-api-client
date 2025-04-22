
2024-02-12 v1.2.0

Synchronized LexMachinaClient to match current live API.

- Renamed `list_damages_statet` to `list_damages_state` (fix typo)
- Removed `list_state_judgment_sources` 
- Renamed `query_state_cases_case` to `query_state_cases`
- Added `get_appeals_case` 
- Added `query_appeals_case`
- Added `list_state_judgment_events`
- Added `list_originating_venues_federal`
- Added `list_appellate_decisions_federal`
- Added `list_supreme_court_decisions_federal`


2025-04-22 v2.0.0.20250318

Used the Python generator from [openapi-generator](https://openapi-generator.tech/docs/generators/python/) to generate a Python client based on the current version of the Lex Machina API (v20250318).

- The updated client has methods for recently added endpoints such as those accessing alerts results and searching for cases by case number.
- The previous version of the client is accessible under a `v1` subpackage. We will not be providing continuing support for the `v1` subpackage and it will be removed in 2026.
