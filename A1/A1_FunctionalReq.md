## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).
  - T3
  - T4*

FR-02 (Medium) If the user enters an incorrect credentials file when authenticating via the GitHub API, the system shall prevent access and display "Authentication failed: Invalid login credentials" before allowing another login attempt. (map: URS-01, URS-12)
  - T4

FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line for an organization they have authorised access to. (map: URS-02)
  - T1
  - T2*
- 

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they have authorised access to on the command line. (map: URS-03)
  - T5
  - T6

FR-06 (Medium) The system shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name that they are a contributor of on the command line. (map: URS-07, URS-04)
  - T7

FR-07 (Medium) The system shall allow contributors to view their specific ranking for a given project phase by specifying a repository name that they are a contributor of and their selected time period on the command line. (map: URS-05)
  - T8

FR-08 (Medium) The system shall calculate the most active contributor(s) within a given repository or organisation using predefined metrics that are based on the number of each contributor's commits. (map: URS-06, URS-05, URS-04, URS-03, URS-02)
  - T1
  - T2
  - T5
  - T6
  - T7
  - T8
  - T9
  - T10

FR-09 (Medium) If the user requests to view contributor rankings for a given repository/organisation, the system shall produce a report displaying the contribution rankings based on the most active contributor(s) within the specified repository/organisation. (map: URS-06, URS-05, URS-04, URS-03, URS-02)
  - T1
  - T2
  - T5
  - T6
  - T7
  - T8
  - T9
  - T10

FR-10 (Medium) If the user requests contributor rankings for a given repository/organisation and the system calculates multiple contributors with the same commit count, the system shall display all the equally active contributors with the same ranking. (map: URS-06, URS-03, URS-02)
  - T9
  - T10
  
FR-11 (Medium) If the user requests their specific ranking for a given repository and the system calculates they are equally active with at least one other contributor, the system shall display them with the same rank as all other equally active contributor/s.
  - T11
  
FR-12 (Medium) The system shall allow users to filter contributor rankings by specific time periods (i.e. project phase) by specifying a time period on the command line. (map: URS-07, URS-06, URS-03, URS-02)
  - T14
  - T15
  - T16
  - T17

FR-13 (Medium) If the user requests contributor rankings for a given repository/organisation within a specific time period, the system shall re-calculate and display the contributor rankings using only the API contribution data found within the specified time period. (map: URS-07, URS-06, URS-05, URS-04, URS-03, URS-02)
  - T14
  - T15
  - T16
  - T17

FR-14 (Medium) If the user selects a time-based filter for a time period with no contributions, then the system shall display "No contributions found for the specified time period", and allow them to specify a different time filter. (map: URS-07, URS-06, URS-05, URS-04, URS-03, URS-02)
- T16
- T17

//FR-15 (Medium) The system shall store user authentication tokens for private organisations in the database. (map: URS-09)

FR-16 (Medium) The system shall allow users to download contributor rankings in JSON format by specifiyng an export request on the command line. (map: URS-10)  
  - T18

FR-17 (Medium) If the user requests to download contributor rankings for a valid, non-empty repository by specifying an export request on the command line, the system shall convert the contribution data into a JSON format and download the generated file into the user's device. (map: URS-10)
  - T18
  - T19
  - T20
  - T21

//FR-18 (Medium) The system shall use TLS encryption to ensure secure communication for all data transmissions over the network. (map: URS-11)

//FR-19 (Medium) The system shall have access to the GitHub API for processing authenticated user requests for contributor data relating to a repository or organisation that they specify on the command line. (URS-08)
- T20

//FR-20 (Medium) If temporary caching is not enabled, the system shall be able to accommodate up to 20 concurrent API requests from multiple users simultaneously and maintain a response time of five seconds. (URS-13, URS-08, URS-12)
  - T20

//FR-21 (Medium) If temporary caching is enabled, the system shall be able to accommodate up to 100 concurrent API requests from multiple users simultaneously and maintain a response time of five seconds (URS-13, URS-08, URS-12)
  - T20

## RBAC
//FR-22 (Medium) The system shall enforce role-based access control to process API requests for data handling within a given repository or organisation. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06)

## Rate limit
FR-23 (Medium) If a user requests contributor data from a repository or organisation where the API rate limit has exceeded, the system shall prevent access and display "Cannot access repository due to an exceed in rate limit" before allowing them to specify a different repository or organisation on the command line. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06)

## Private Organisation
FR-24 (Medium) If a user requests contributor data from an unauthorized organisation, the system shall prevent access and display "Access denied: user is not authorised to access this organisation" before allowing them to specify a different repository or organisation name on the command line. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06, URS-09)

## Invalid org/repo name
FR-25 (Medium) If the user requests contribution data by specifying an invalid organisation (i.e. doesn't match any existing organisations), the system shall display "Invalid URL: Organisation doesn't exist" and allow them to enter a different organisation name on the command line. (map: URS-12, URS-03, URS-09)

FR-31 (Medium) If the user requests contribution data by specifying an invalid repository name (i.e. doesn't match any existing repositories), the system shall display "Invalid URL: Repository doesn't exist" and allow them to enter a different repository name on the command line. (map: URS-12,  URS-02, URS-04, URS-05, URS-09)

## Login
FR-26 (Medium) If the user enters an incorrect credentials file when authenticating via the GitHub API, the system shall prevent access and display "Authentication failed: Invalid login credentials" before allowing another login attempt. (map: URS-12, URS-01)

## Empty repo
FR-27 (Medium) If the user requests contribution data for an empty repository (i.e. no content/initial commit exists), the system shall display "No contributions found" and allow them to enter a different repository name on the command line. (map: URS-12, URS-02, URS-04, URS-05, URS-06)

## Empty org
FR-28 (Medium) If the user requests contribution data for an empty organization (i.e. no content/initial commit exists), the system shall display "No contributions foud" and allow them to enter a different organization name on the command line.(map: URS-12, URS-03)

## No contributor contributions
FR-29 (Medium) If a contributor requests to view their personal contribution ranking for a repository that they have made no contributions to, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line. (map: URS-12, URS-04, URS-05)

FR-30 (Medium) If a user requests to view contributor rankings for a repository or organisation where there exists contributors with no contributions (i.e. no commit activity), the system shall not display them in the contributor rankings. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06, URS-07)

FR-31 (Medium) If the system processes a request for contributor rankings for a repository or organisation where there exists contributors with no contributions (i.e. no commit activity), the system shall exclude these contributors when generating the ranking of most active contributors. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06, URS-07)

FR-33 (Medium) If a contributor requests to view their personal contribution ranking for a repository in a specific time period where they have made no contributions, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line. (map: URS-12, URS-04, URS-05)