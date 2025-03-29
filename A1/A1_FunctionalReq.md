## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).

FR-02 (Medium) If the user enters an incorrect credentials file, the system shall prevent access and display "Authentication failed: Invalid login credentials". (map: URS-12)

FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name for an organization they have authorised access to on the command line. (map: URS-02)

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they have authorised access to on the command line. (map: URS-03)

FR-05 (Medium) The system shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name that they are a contributor of on the command line. (map: URS-04)

FR-06 (Medium) The system shall allow contributors to view their specific ranking for a given project phase by specifying a valid repository name and time-based filter on the command line. (map: URS-05)

FR-07 (Medium) The system shall calculate and display a ranking of the most active contributor(s) within the requested organisation or repository based on each contributor's commit count. (map: URS-06)
  
FR-08 (Medium) If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. (map: URS-06)

FR-09 (Medium) If a user specifies a time-based filter for a valid repository or organisation on the command line, the system shall process and display a ranking of the most active contributor(s) within the requested time period. (map: URS-07)

FR-10 (Medium) If no contributions are found for the specified time period, the system shall display "No contributions found for the specified time period". (map: URS-07)

FR-11 (Medium) The system shall process authenticated user requests for contributor data via GitHub API and provide the retrieved results on the command line. (map: URS-08)

FR-12 (Medium) If an authentication token is specified by the user via the command line, the system shall store it in the database to access private GitHub organisations. (map: URS-09)

FR-13 (Medium) When a user requests to export contributor rankings for a valid repository/organisation via the command line, the system shall generate a JSON file and make it available for download. (map: URS-10)

FR-14 (Medium) When a contributor requests to export their specific ranking for a repository that they have contributed to, the system shall generate a JSON file containing their individual contributor data and make it available for download. (map: URS-10)

FR-15 (Medium) If a user specifies a valid time-based filter with their export request, the system shall generate a JSON file containing the filtered contribution data and make it available for download. (map: URS-10)

## Rate limit handling
FR-16 (Medium): If a user requests contributor data when the GitHub API rate limit has exceeded, the system shall display "GitHub API rate limit exceeded. Please try again later" and resume processing requests when the rate limit resets. (map: URS-12)

## Private Organisation
FR-17 (Medium) If a user specifies an unauthorized organization name on the command line, the system shall prevent access and display "Access denied: unauthorised organisation".(map: URS-12)

FR-18 (Medium) If a user specifies a non-existing organisation or repository name on the command line, the system shall display "Invalid URL provided". (map: URS-12)

FR-19 (Medium) If the user specifies an empty organization or repository name (i.e. no content/initial commit exists) on the command line, the system shall display "No contributions found". (map: URS-12)

## No contributor contributions
FR-20 (Medium) If a contributor requests to view their specific ranking for a repository that they have made no contributions to, the system shall display "No user contributions found".(map: URS-04)

FR-21 (Medium) The system shall only include contributors with at least one commit when processing and displaying contributor rankings within a given organisation or repository. (map: URS-06)

FR-22 (Medium) If a contributor requests to view their specific ranking in a time period for which they have made no contributions, the system shall display "No user contributions found for the specified time period". (map: URS-05)



