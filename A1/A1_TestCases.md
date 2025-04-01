# System Tests

T1 Scenario: Valid repository with multiple contributors
Expectation: Correct ranking of contributors displayed.

T2 Scenario: Valid repository with no contributors
Expectation: Error message: No contributions found.

T3 Scenario: Attempt to authenticate using a GitHub account
Expectation: System successfully authenticates and grant access.

T4 Scenario: Attempt to authenticate using invalid GitHub credentials file
Expectation: Error message: Authentication failed: Invalid login credentials.

T5 Scenario: Valid organisation with multiple contributors
Expectation: Correct ranking of contributors displayed.

T6 Scenario: Valid organisation with no contributors
Expectation: Error message: No contributions found.

T7 Scenario: View specific ranking for project lifetime in valid repository with multiple contributors
Expectation: Correct personal contributor ranking for project lifetime displayed

T8 Scenario: View specific ranking for specific project phase in valid repository with multiple contributors
Expectation: Correct personal contributor ranking within specified time period displayed.

T9 Scenario: Valid repository with multiple equally active contributors
Expectation: Correct equal ranking for equally active contributors displayed.

T10 Scenario: Valid organisation with multiple equally active contributors
Expectation: Correct equal ranking for equally active contributors displayed.

T11: Scenario: View specific ranking for project lifetime in valid repository with multiple equally active contributors
Expectation: Correct same personal contributor ranking with other equally active contributors displayed.

T12: Scenario: View specific ranking for specific project phase in valid repository with multiple equally active contributors
Expectation: Correct same personal contributor ranking with other equally active contributors within specified time period displayed.

T13 Scenario: Filter contributor rankings for valid repository with multiple contributors by specific time period
Expectation: Correct contributor rankings for specified time period displayed

T14 Scenario: Filter contributor rankings for valid organisation with multiple contributors by specific time period
Expectation: Correct contributor rankings for specified time period displayed

T15 Scenario: Filter contributor rankings for valid, non-empty organisation by specific time period with no contributions
Expectation: Error message: No contributions found for the specified time period

T16 Scenario: Filter contributor rankings for valid, non-empty repository by specific time period with no contributions
Expectation: Error message: No contributions found for the specified time period

T17 Scenario: View specific ranking for specific project phase with no contributions in valid, non-empty repository.
Expectation: Error message: No contributions found for the specified time period.

T18: Scenario: View specific ranking for valid repository with no contributions.
Expectation: Error message: No contributions found.

T19 Scenario: Export contributor rankings for valid repository with multiple contributors in JSON format
Expectation: Correct contributor rankings downloaded in JSON formatted file.

T20 Scenario: Export contributor rankings for valid organisation with multiple contributors in JSON format
Expectation: Correct contributor rankings downloaded in JSON formatted file.

T21 Scenario: Export contributor rankings for valid repository with no contributors in JSON format
Expectation: Error message: No contributions found

T22 Scenario: Export contributor rankings for valid organisation with no contributors in JSON format
Expectation: Error message: No contributions found

T23 Scenario: Invalid authentication token provided for private organisation
Expectation: Error message: Access denied: unauthorised organisation.

T24 Scenario: Invalid repository name
Expectation: Error message: Invalid URL provided

T25 Scenario: Invalid organisation name
Expectation: Error message: Invalid URL provided

T26 Scenario: View specific ranking for valid, non-empty repository with no user contributions
Expectation: Error message: No user contributions found

T27 Scenario: View specific ranking for specific project phase with no user contributions in valid, non-empty repository
Expectation: Error message: No user contributions found for the specified time period

T28 Scenario: Export specific ranking for specific project phase with no user contributions in valid, non-empty repository
Expectation: Error message: No user contributions found for specified time period.

T29 Scenario: Export specific ranking for valid, nom-empty repository with no user contributions in JSON format
Expectation: Error message: No user contributions found

T30: Valid repository with 1 contributor
Expectation: Single contributor is displayed with first ranking.

T31: Valid organisation with 1 contributor
Expectation: Single contributor is displayed with first ranking.

T32: View specific ranking for project lifetime in valid repository with no other contributors.
Expectation: Personal ranking is displayed as 1st.

T33: View specific ranking for specific project phase in valid repository with no other contributors.
Expectation: Personal ranking is displayed as 1st.

T34 Scenario: Attempt to request GitHub API data when rate limit exceeded
Expectation: Error message: GitHub API rate limit exceeded. Please try again later

T35 Scenario: Valid authentication token for private organisation provided 
Expectation: Retrieved token matches stored token and requested organisation data is displayed.

T36 Scenario: Export specific ranking for valid repository with no contributors in JSON format
Expectation: Error message: No contributions found

T37 Scenario: Export specific ranking for project lifetime in valid, non-empty repository in JSON format
Expectation: Correct specific contributor ranking for project lifetime downloaded in JSON formatted file

T38 Scenario: Export contributor rankings for specific time period in valid, non-empty organisation in JSON format
Expectation: Correct contributor rankings for specified time period downloaded in JSON formatted file

T39 Scenario: Export contributor rankings for specific time period in valid, non-empty reposistory in JSON format
Expectation: Correct contributor rankings for specifeed time period downloaded in JSON formatted file

T40 Scenario: Export specific ranking for specific project phase in valid, non-empty reposistory in JSON format
Expectation: Correct personal ranking for specified time period downloaded in JSON formatted file

T41 Scenario: System Timeout/Delay while processing contributor ranking
Expectation: Error message: Request timeout experienced. Please check GitHub API status or try again later.

T42 Scenario: Formatting error occurs for JSON export request
Expectation: Error message: Export failed: unexpected format received. Please check GitHub API status or try again later.

T43 Scenario: Export contributor rankings for specific time period with no contributions in valid, non-empty organisation
Expectation: Error message: No contributions found for specified time period.

T44 Scenario: Export contributor rankings for specific time period with no contributions in valid, non-empty repository
Expectation: Error message: No contributions found for specified time period.

T46 Scenario: Export specific ranking for specific time period with no contributions in valid, non-empty repository
Expectation: Error message: No contributions found for specified time period.