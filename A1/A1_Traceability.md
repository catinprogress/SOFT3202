## 11. Traceability Matrix

- URS: URS-01 Support authentication and authorization via GitHub API
  SRS: FR-01 System shall allow users to authenticate via GitHub API
  verification: System Test (T3)
- URS: URS-08: Process API data within five seconds
  SRS: Non-Functional Requirement: Performance
  verification: System Test (Performance Benchmark)
- URS: URS-09: Securely store authentication tokens
  Non-Functional Requirement: Security
  verification: Security Audit
  
  TODO

- URS: URS-12 Provide error handling mechanisms for access restrictions. (negative)
  SRS: FR-02 If the user enters an incorrect credentials file, the system shall prevent access and display "Authentication failed: Invalid login credentials". 
  verification: System Test (T4)

- URS: URS-02 Allow users to input a GitHub repository name (i.e., URL) and retrieve contributor rankings.
  SRS: FR-03 System shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line.
  verification: System Test (T1, T2,  T9, T28, T24, T30)

- URS: URS-03 Allow users to input a GitHub organization name (i.e., URL) and retrieve contributor rankings.
  SRS: FR-04 System shall allow users to view contributor rankings for a GitHub organization by specifying a GitHub organisation name on the command line.
  verification: System Test (T5, T6, T1O, T31, T25, T29)

- URS: URS-04 Allow users to input a GitHub repository name (i.e., URL) and retrieve their specific ranking for life time of the project.
  SRS: FR-05 System shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name on the command line.
  verification: System Test (T7, T11, T26, T32, T18)

- URS: URS-05 Allow users to input a GitHub repository name (i.e., URL) and retrieve their specific ranking for the specific phase of the project.
  SRS: FR-06 System shall allow contributors to view their specific ranking for a given project phase by specifying a valid repository name and time-based filter on the command line.
  verification: System Test (T8, T33, T12)

- URS: URS-06 Display the most active contributor(s) based on commit count.
  SRS: FR-07 System shall calculate and display a ranking of the most active contributor(s) within the requested organisation or repository based on each contributor's commit count.
  verification: System Test (T1, T5, T30, T31)

- URS: URS-06 Display the most active contributor(s) based on commit count.
  SRS: FR-08 If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. 
  verification: System Test (T9, T10, T11, T12)

- URS: URS-07 Allow users to filter rankings by specific time periods
  SRS: FR-09 If a user specifies a time-based filter for a valid repository or organisation on the command line, the system shall process and display a ranking of the most active contributor(s) within the requested time period.
  verification: System Test (T8, T12, T13, T14, T33)

- URS: URS-07 Allow users to filter rankings by specific time periods (negative)
  SRS: FR-10 If no contributions are found for the specified time period, the system shall display "No contributions found for the specified time period". 
  verification: System Test (T15, T16, T17)

- URS: URS-08 System shall process API data and provide results
  SRS: FR-11 System shall process authenticated user requests via GitHub API and provide the retrieved results on the command line.
  verification: System Test (T35, T1, T5, T7, T8)

- URS: URS-09 System shall securely store authentication tokens if required for private repositories
  SRS: FR-12 If an authentication token is specified by the user via the command line, the system shall store it in the database to access private GitHub organisations. (map: URS-09)
  verification: System Test (Failure Handling, T23, T35) 

- URS: URS-10 Allow users to download contributor rankings in JSON format.
  SRS: FR-13 When a user requests to export contributor rankings via the command line, the system shall generate a JSON file and make it available for download
  verification: System Test (T19, T20, T38, T39)

- URS: URS-10 Allow users to download contributor rankings in JSON format
  SRS: FR-14 When a contributor requests to export their specific ranking for a repository that they have contributed to, the system shall generate a JSON file containing their individual contributor data and make it available for download.
  verification: System Test (T37, T40)

- URS: URS-10 Allow users to download contributor rankings in JSON format
  SRS: FR-15 If a user specifies a valid time-based filter with their export request, the system shall generate a JSON file containing the filtered contribution data and make it available for download.
  verification: System Test (T38, T39, T40)

- URS: URS-12 System shall provide error handling mechanisms for API rate limit. (negative) 
  SRS: FR-16 If a user requests contributor data when the GitHub API rate limit has exceeded, the system shall display "GitHub API rate limit exceeded. Please try again later" and resume processing requests when the rate limit resets.
  verification: System Test (T34)

- URS: URS-12 System shall provide error handling mechanisms for access restrictions (negative)
  SRS: FR-17 If a user specifies an unauthorized organization name on the command line, the system shall prevent access and display "Access denied: unauthorised organisation".
  verification: System Test (T23)

- URS: URS-12 System shall provide error handling mechanisms for invalid repository names (negative)
  SRS: FR-18 If a user specifies a non-existing organisation or repository name on the command line, the system shall display "Invalid URL provided".
  verification: System Test (T25, T24)

- URS: URS-12 System shall provide error handling mechanisms for invalid repository names (negative)
  SRS: FR-19 If a user specifies an empty repository or organisation name (i.e. no content/initial commit exists) on the command line, the system shall display "No contributions found" 
  verification: System Test (T2, T6, T18, T21, T22, T36)

- URS: URS-04 Contributor with no contributions requests specific ranking (negative)
  SRS: FR-20 If a contributor requests access to their personal ranking for a repository that they have made no contributions to, the system shall display "No user contributions found"
  verification: System Test (T26, T36)

- URS: URS-06 Contributor with no contributions in valid repository/organisation
  SRS: FR-21 the system shall only include contributors with at least one commit when processing and displaying contributor rankings within a given organisation or repository. 
  verification: System Test (T28, T29)
  
- URS: URS-05 Contributor with no contributions view specific ranking for specific time period (negative)
  SRS: FR-22 If a contributor requests to view their personal ranking in a time period for which they have made no contributions, the system shall display "No user contributions found for the specified time period".
  verification: System Test (T27)

- URS: URS-12 The system shall provide error handling mechanisms for API failures
  Non-functional requirement: Usability
  verification: System Test (T41, T42)