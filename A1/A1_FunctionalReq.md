## 3. Functional Requirements

FR-01 (Medium) Thee system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).

FR-02 (Medium) If the user enters an incorrect credentials file, the system shall prevent access and display "Invalid login credentials". (map: URS-12)

FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line for an organization they have authorised access to. (map: URS-02)

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they have authorised access to on the command line. (map: URS-03)

FR-05 (Medium) The system shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name that they are a contributor of on the command line. (map: URS-04)

FR-06 (Medium) The system shall allow contributors to view their specific ranking for a given project phase by specifying a valid repository name and time-based filter on the command line. (map: URS-05)

FR-07 (Medium) The system shall calculate and display a ranking of the most active contributor(s) within the requested organisation or repository based on each contributor's commit count. (map: URS-06)
  
FR-08 (Medium) If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. (map: URS-06)

FR-09 (Medium) When a user specifies a time-based filter for a valid repository or organisation on the command line, the system shall process and display contributor rankings based on contributions made within the requested time period. (map: URS-07)

FR-10 (Medium) If no contributions are found for the specified time period within a requested repository or organisation, the system shall display "No contributions found for the specified time period".(map: URS-07)

FR-12 (Medium) When a user requests to export contributor rankings via the command line, the system shall generate a JSON file and make it available for download. (map: URS-10)

FR-13 (Medium) When a user requests to export contributor rankings for an empty repository or organisation, the system shall display "No contributions available for export" and not proceed with the export.

## Rate limit handling
FR-14 (Medium): If a user request exceeds the API rate limit, the system shall display "GitHub API rate limit exceeded. Please try again later" and continue processing requests when the rate limit resets.

## Private Organisation
FR-15 (Medium) If a user specifies an unauthorized organization name on the command line, the system shall prevent access and display "Access denied: unauthorised organisation".(map: URS-12)

## Invalid org/repo name
FR-16 (Medium) If a user specifies an non-existing organisation name on the command line, the system shall display "Invalid URL: Organisation doesn't exist". (map: URS-12)

FR-17 (Medium) If the user specifies a non-existing repository name on the command line, the system shall display "Invalid URL: Repository doesn't exist".(map: URS-12)

## Empty repo
FR-18 (Medium) If the user specifies an empty repository name (i.e. no content/initial commit exists) on the command line, the system shall display "No contributions found". (map: URS-12)

## Empty org
FR-19 (Medium) If the user specifies an empty organization name (i.e. no content/initial commit exists) on the command line, the system shall display "No contributions found".(map: URS-12)

## No contributor contributions
FR-20 (Medium) If a contributor requests to view their personal ranking for a repository that they have made no contributions to, the system shall display "No user contributions found".(map: URS-12)

FR-21 (Medium) The system shall only include contributors with at least one commit when processing and displaying contributor rankings within a given organisation or repository. (map: URS-12)

FR-22 (Medium) If a contributor requests to view their personal ranking in a time period for which they have made no contributions, the system shall display "No user contributions found for the specified time period". (map: URS-12)

FR-23 (Medium) If an authenticated user specifies a valid repository or organisation name on the command line, the system shall process their request via GitHub API and display the corresponding contributor ranking results. (map: URS-08)

FR-24 (Medium) If an authentication token is specified by the user via the command line, the system shall store it in the database to access private GitHub organisations. (map: URS-09)