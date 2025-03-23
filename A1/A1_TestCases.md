# System Tests

## T1 Scenario: Valid repository with multiple contributors
- Expectation: Correct ranking of contributors displayed.
## T2 Scenario: Valid repository with no contributors
- Expectation: Error message: No contributions found.
## T3 Scenario: Attempt to authenticate using a GitHub account
- Expectation: System successfully authenticates and grant access.
## T4 Scenario: Attempt to authenticate using invalid GitHub credentials file
- Expectation: Error message: Authentication failed: Invalid login credentials.
## T5 Scenario: Valid organisation with multiple contributors
- Expectation: Correct ranking of contributors displayed.
## T6 Scenario: Valid organisation with no contributors
- Expectation: Error message: No contributions found.
## T7 Scenario: View specific ranking for project lifetime in valid repository with multiple contributors
- Expectation: Correct personal contributor ranking for project lifetime displayed
## T8 Scenario: View specific ranking for specific project phase in valid repository with multiple contributors
- Expectation: Correct personal contributor ranking within specified time period displayed 
  
## T9 Scenario: Valid repository with multiple equally active contributors
- Expectation: Correct equal ranking for equally active contributors displayed.
## T10 Scenario: Valid organisation with multiple equally active contributors
- Expectation: Correct equal ranking for equally active contributors displayed.
## T11: Scenario: View specific ranking for valid repository with multiple equally active contributors for project lifetime
- Expectation: Correct same personal contributor ranking displayed to other equally active contributors.
## T12: Scenario: View specific ranking for specific time period with multiple equally active contributors for valid repository 
- Expectation: Correct same personal contributor ranking with other equally active contributors within specified time period displayed.
## T13 Scenario: Filter contributor rankings for valid repository with multiple contributors by specific time period
- Expectation: Correct contributor rankings for specified time period displayed
## T14 Scenario: Filter contributor rankings for valid organisation with multiple contributors by specific time period
- Expectation: Correct contributor rankings for specified time period displayed
## T15 Scenario: Filter contributor rankings for valid repository with no contributors by specific time period
- Expectation: Error message: No contributions found for the specifed time period
## T16 Scenario: Filter contributor rankings for valid organisation with no contributors by specific time period
- Expectation: Error message: No contributions found for the specified time period
## T17 Scenario: View specific ranking for specific project phase with no contributions in valid, non-empty repository.
- Expectation: Error message: No contributions found for the specified time period.
## T18: Scenario: View specific ranking for valid repository with no contributions.
- Expectation: Error message: No contributions found.
## T19 Scenario: Export contributor rankings for valid repository with multiple contributors in JSON format
- Expectation: Correct contributor rankings downloaded in JSON formatted file.
## T20 Scenario: Export contributor rankings for valid organisation with multiple contributors in JSON format
- Expectation: Correct contributor rankings downloaded in JSON formatted file.
## T21 Scenario: Export contributor rankings for valid repository with no contributors in JSON format
- Expectation: Error message: No contributions found
## T22 Scenario: Export contributor rankings for valid organisation with no contributors in JSON format
- Expectation: Error message: No contributions found

## T23 Scenario: Attempt to access unauthorised private organisation
- Expectation: Error message: Access denied: user is not authorised to access this organisation.
## T24 Scenario: Invalid repository name
- Expectation: Error message: Invalid URL: Repository doesn't exist
## T25 Scenario: Invalid organisation name
- Expectation: Error message: Invalid URL: Organisation doesn't exist
## T26 Scenario: View specific ranking for valid non-empty repository with no user contributions
- Expectation: Error message: No user contributions found
## T27 Scenario: View specific ranking for specific project phase with no user contributions in valid non-empty repository
- Expectation: Error message: No user contributions found
## T28 Scenario: Valid repository containing contributors with no contributions
- Expectation: Correct ranking of only contributors with at least one contribution displayed.
## T29 Scenario: Valid organisation containing contributors with no contributions
- Expectation: Correct ranking of only contributors with at least one contribution displayed.
## T30: Valid repository with 1 contributor
- Expectation: Single contributor is displayed with first ranking.
## T31: Valid organisation with 1 contributor
- Expectation: Single contributor is displayed with first ranking.
## T32: View specific ranking for valid repository with no other contributors.
- Expectation: Personal ranking is displayed as 1st.
## T33: View specific ranking for specific project phase in valid repository with no other contributors.
- Expectation: Personal ranking is displayed as 1st.
## T34 Scenario: Attempt to request GitHub API data when rate limit exceeded
- Expectation: Error message: Cannot access GitHub API data due to an exceed in rate limit, please try again later











## T20 Scenario: Query response time test
- Expectation: Query results displayed within 5 seconds.
## T21 Scenario: Concurrent user load test with temporary caching
- Expectation: System responds for up to 20 concurrent API requests from multiple users simultaneously with no performance degredation.
## T22 Scenario: Concurrent user load test without temporary caching
- Expectation: System responds for up to 100 concurrent API requests from multiple users simultaneously with no performance degredation

