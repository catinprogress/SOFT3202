## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).

FR-02 (Medium) If the user enters an incorrect credentials file when authenticating via the GitHub API, the system shall prevent access and display "Authentication failed: Invalid login credentials" before allowing another login attempt. (map: URS-01, URS-12)

FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line for which they have authorised access to. (map: URS-02)

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they are authorised to access on the command line. (map: URS-03)

FR-05 (Medium) If a user requests contributor rankings for an organisation that contains private repositories for which they are not permitted access, the system shall produce a report using only the contributor data for which they have access privileges for. (map: URS-03)

FR-06 (Medium) The system shall allow contributors to view their specific ranking for life time of the project by specifying a repository name that they are a contributor of on the command line. (map: URS-04)

FR-07 (Medium) The system shall allow contributors to view their specific ranking for the latest phase of the project by specifying a repository name that they are a contributor of on the command line. (map: URS-05)

FR-08 (Medium) The system shall calculate the most active contributor(s) within a given repository or organisation using predefined metrics that are based on each contributor's commit data (e.g. number of commits, pull requests merged, and lines of code added/removed) (map: URS-06, URS-05, URS-04, URS-03, URS-02)

FR-09 (Medium) If the user requests contributor rankings for a given repository or organisation by specifying the repository/organisation name on the command line, the system shall produce a report displaying the contribution rankings based on the most active contributor(s) within the specified repository or organisation. (map: URS-06, URS-05, URS-04, URS-03, URS-02)

FR-10 (Medium) If the user requests contributor rankings for a given repository or organisation and the system calculates multiple contributors with the same commit count, the system shall display all the equally active contributors with the same ranking. (map: URS-06, URS-05, URS-04, URS-03, URS-02)

FR-11 (Medium) If the user requests the most active contributor(s) for a given repository or organisation and the system calculates multiple contributors with the greatest commit count, the system shall display all the contributors as ranked equally most active. (map: URS-06, URS-03, URS-02)

FR-12 (Medium) The system shall allow users to filter contributor rankings by specific time periods by specifying a time period (e.g. start and end date) on the command line. (map: URS-07, URS-06, URS-05, URS-04, URS-03, URS-02)

FR-13 (Medium) If the user selects a time-based filter that contains contribution data, the system shall re-calculate and display the contributor rankings using only the GitHub API contribution data that exists within the specified time period. (map: URS-07, URS-06, URS-05, URS-04, URS-03, URS-02)

FR-14 (Medium) If the user selects a time-based filter that contains no contributions, then the system shall display "No contribution data exists for the specifed time period", and allow them to specify a different time filter. (map: URS-07, URS-06, URS-05, URS-04, URS-03, URS-02)

FR-15 (Medium) The system shall encrypt all authentication tokens for private repositories before storing them in the database. (map: URS-09)

FR-16 (Medium) The system shall allow users to download contributor rankings in JSON format by providing an export option on the command line. (map: URS-10)  

FR-17 (Medium) If the user requests to download contributor rankings by specifying an export request on the command line, the system shall convert the contribution data into a JSON format and download the generated file into the user's device. (map: URS-10)

FR-18 (Medium) The system shall use TLS encryption to ensure secure communication for all data transmissions over the network. (map: URS-11)

FR-19 (Medium) The system shall have access to the GitHub API and allow users to request contribution data by specifying a GitHub repository or organisation name on the command line. (map: URS-08)

FR-20 (Medium) The system shall process and display results to a user's API data request within 5 seconds of the query being made, given standard operating conditions. (URS-08)

FR-20 (Medium) If temporary caching is not enabled, the system shall be able to accommodate up to 20 concurrent API requests from multiple users simultaneously and maintain a response time of five seconds. (URS-13, URS-08, URS-12)

FR-21 (Medium) If temporary caching is enabled, the system shall be able to accommodate up to 100 concurrent API requests from multiple users simultaneously and maintain a response time of five seconds (URS-13, URS-08, URS-12)

## RBAC
FR-22 (Medium) The system shall enforce role-based access control to process API requests for data handling within a given repository or organisation. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06)

FR-22 (Medium) If a user requests contributor data from a repository or organisation where the API rate limit has exceeded, the system shall prevent access and display "Cannot currently access contributor data for this repository due an exceed in rate limit" before allowing them to specify a different repository or organisation on the command line. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06)

FR-23 (Medium) If a user requests contributor data for an unauthorised private repository/organisation, the system shall prevent access and display "Access denied: user is not authorised to access this repository/organisation" before allowing them to specify a different repository or organisation name on the command line. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06, URS-09)

FR-24 (Medium) If the user requests contribution data by specifying an invalid organisation or repository name (i.e. doesn't match any existing organisations/repositories), the system shall display "The requested organisation/repository doesn't exist" and allow them to enter a different repository/organisation name on the command line. (map: URS-12, URS-02, URS-03, URS-04, URS-05, URS-06, URS-09)

FR-25 (Medium) If the user enters an incorrect credentials file when authenticating via the GitHub API, the system shall prevent access and display "Authentication failed: Invalid login credentials" before allowing another login attempt. (map: URS-12, URS-01)

FR-26 (Medium) If the user requests contribution data for an empty repository (i.e. no content/initial commit exists), the system shall display "No contributor data available for this repository" and allow them to enter a different repository name on the command line. (map: URS-12, URS-02, URS-04, URS-05, URS-06)

FR-27 (Medium) If the user requests contribution data for an empty organization (i.e. no content/initial commit exists), the system shall display "No contributor data available for this organization" and allow them to enter a different organization name on the command line.(map: URS-12, URS-03)

FR-28 (Medium) If a user requests to view their personal contribution ranking for a repository for which they are a contributor of but have made no contributions to, the system shall display their rank as equally last with any other contributors containing no commit data. (map: URS-12, URS-04, URS-05)

FR-29 (Medium) If a user requests to view their personal contribution ranking for a repository for which they are not a contributor to, the system shall display "No contributor data for user exists for this repository" and allow them to enter a different repository name on the command line. (map: URS-12, URS-04, URS-05)

FR-29 (Medium) If a user requests to view the contributor rankings for a repository or organisation where there exists contributors who have made no contributions (i.e. no commit data), the system shall display those contributors as ranked equally last. (map: URS-12, URS-02, URS-03)