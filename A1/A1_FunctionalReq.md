## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).

FR-02 (Medium) If the user enters an incorrect credentials file, the system shall prevent access and display "Authentication failed: Invalid login credentials". (map: URS-12)


FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line for an organization they have authorised access to. (map: URS-02)

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they have authorised access to on the command line. (map: URS-03)

FR-05 (Medium) The system shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name that they are a contributor of on the command line. (map: URS-04)

FR-06 (Medium) The system shall allow contributors to view their specific ranking for a given project phase by specifying a valid repository name and time-based filter on the command line. (map: URS-05)

FR-07 (Medium) The system shall calculate and display a ranking of the most active contributor(s) within a requested organisation or repository based on each contributor's commit count. (map: URS-06)

If the user requests to view contributor rankings for a repository/organisation, the system shall calculate the most active contributor(s) by measuring each contributor's commit count, and include these metrics and their name when displaying the resulting rankings. (map: URS-06)
  
FR-08 (Medium) If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. (map: URS-06)

FR-09 (Medium) When a user specifies a time-based filter for a valid repository or organisation on the command line, the system shall process and display contributor rankings based on contributions made within the requested time period. (map: URS-07)

FR-10 (Medium) If no contributions are found for a specified time period, the system shall display "No contributions found for the specified time period". (map: URS-07)

FR-12 (Medium) When a user requests to export contributor rankings via the command line, the system shall generate a JSON file containing the requested contributor data and make it available for download.(map: URS-10)

FR-13 (Medium) When a user requests to export contributor rankings for an empty repository or organisation, the system shall display "No contributions found" and not proceed with the export.

//14

## Private Organisation
FR-15 (Medium) If a user specifies an unauthorized organization name on the command line, the system shall prevent access and display "Access denied: unauthorised organisation".(map: URS-12)

## Invalid org/repo name
FR-16 (Medium) If the user requests contribution data by specifying an invalid organisation (i.e. doesn't match any existing organisations), the system shall display "Invalid URL: Organisation doesn't exist" and allow them to enter a different organisation name on the command line. (map: URS-12)

FR-17 (Medium) If the user requests contribution data by specifying an invalid repository name (i.e. doesn't match any existing repositories), the system shall display "Invalid URL: Repository doesn't exist" and allow them to enter a different repository name on the command line. (map: URS-12)

## Empty repo
FR-18 (Medium) If the user requests contribution data for an empty repository (i.e. no content/initial commit exists), the system shall display "No contributions found" and allow them to enter a different repository name on the command line. (map: URS-12)

## Empty org
FR-19 (Medium) If the user requests contribution data for an empty organization (i.e. no content/initial commit exists), the system shall display "No contributions foud" and allow them to enter a different organization name on the command line.(map: URS-12)

## No contributor contributions
FR-20 (Medium) If a contributor requests to view their personal contribution ranking for a repository that they have made no contributions to, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line. (map: URS-12)

FR-21 (Medium) If a user requests to view contributor rankings for a repository or organisation where there exists contributors with no contributions (i.e. no commit activity), the system shall exclude them when processing and displaying the ranking results. (map: URS-12)

FR-22 (Medium) If a contributor requests to view their personal contribution ranking for a time period where they have made no contributions, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line. (map: URS-12)

FR-23 (Medium) If an authenticated user requests contributor rankings for a GitHub repository/organisation, the system shall process their request via GitHub API and provide ranking results to the user on the command line. (map: URS-08)






