## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).

FR-02 (Medium) If the user enters an incorrect credentials file when authenticating via the GitHub API, the system shall prevent access and display "Authentication failed: Invalid login credentials" before allowing another login attempt. (map: URS-12)

FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line for an organization they have authorised access to. (map: URS-02)

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they have authorised access to on the command line. (map: URS-03)

FR-05 (Medium) The system shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name that they are a contributor of on the command line. (map: URS-04)

FR-06 (Medium) The system shall allow contributors to view their specific ranking for a given project phase by specifying a repository name that they are a contributor of and their selected time period on the command line. (map: URS-05)

FR-07 (Medium) If the user requests to view contributor rankings for a given repository/organisation, the system shall calculate the most active contributor(s) by measuring each contributor's commit count and display the resulting contributor rankings based on this pre-defined metric. (map: URS-06)
  
FR-08 (Medium) If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. (map: URS-06)
  
FR-09 (Medium) The system shall allow users to filter contributor rankings by specific time periods (i.e. project phase) by specifying a time period on the command line. (map: URS-07)

FR-10 (Medium) If the user requests to filter contribution rankings, the system shall display the contributor rankings based on contributions made within the specified time period. (map: URS-07)

FR-11 (Medium) If the user selects a time-based filter for a time period with no contributions, then the system shall display "No contributions found for the specified time period", and allow them to specify a different time filter. (map: URS-07)



FR-12 (Medium) The system shall allow users to download contributor rankings in JSON format by including an export request when specifying a contributor/organisaton name on the command line. (map: URS-10)

FR-13 (Medium) If the user requests to download contributor rankings for a valid, non-empty repository/organisation in JSON format, the system shall convert the contribution data into a JSON format and download the generated file into the user's device. (map: URS-10)

## Rate limit
FR-14 (Medium) The system shall detect API rate limit failures and notify users who request access with "Cannot access GitHub API data due to an exceed in rate limit, please try again later" (map: URS-12)

## Private Organisation
FR-15 (Medium) If a user requests contributor data from an unauthorized organisation, the system shall prevent access and display "Access denied: user is not authorised to access this organisation" before allowing them to specify a different repository or organisation name on the command line. (map: URS-12)

## Invalid org/repo name
FR-16 (Medium) If the user requests contribution data by specifying an invalid organisation (i.e. doesn't match any existing organisations), the system shall display "Invalid URL: Organisation doesn't exist" and allow them to enter a different organisation name on the command line. (map: URS-12)

FR-17 (Medium) If the user requests contribution data by specifying an invalid repository name (i.e. doesn't match any existing repositories), the system shall display "Invalid URL: Repository doesn't exist" and allow them to enter a different repository name on the command line. (map: URS-12)

## Empty repo
FR-18 (Medium) If the user requests contribution data for an empty repository (i.e. no content/initial commit exists), the system shall display "No contributions found" and allow them to enter a different repository name on the command line. (map: URS-12)

## Empty org
FR-19 (Medium) If the user requests contribution data for an empty organization (i.e. no content/initial commit exists), the system shall display "No contributions foud" and allow them to enter a different organization name on the command line.(map: URS-12)

## No contributor contributions
FR-20 (Medium) If a contributor requests to view their personal contribution ranking for project lifetime for a repository that they have made no contributions to, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line. (map: URS-12)

FR-21 (Medium) If a user requests to view contributor rankings for a repository or organisation where there exists contributors with no contributions (i.e. no commit activity), the system shall exclude them when processing and displaying the ranking results. (map: URS-12)

FR-22 (Medium) If a contributor requests to view their personal contribution ranking for a repository in a specific time period where they have made no contributions, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line. (map: URS-12)




//FR-23 (Medium) If the user requests contributor rankings for a GitHub repository/organisation, the system shall process GitHub API data and provide ranking results to the user on the command line. (map: URS-08)

//FR-23 (Medium) The system shall have access to the GitHub API for processing authenticated user requests for contributor data relating to a repository or organisation that they specify on the command line. (URS-08)
  
//FR-24 (Medium) The system shall store user authentication tokens for accessing private organisations as needed, in the database. (map: URS-09)