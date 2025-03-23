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

- URS: URS-12 Provide error handling mechanisms for access restrictions.
  SRS: FR-02 System shall prevent access for failed authentication attempt and display "Authentication failed: Invalid login credentials"
  verification: System Test (T4)

- URS: URS-02 Allow users to input a GitHub repository name (i.e., URL) and retrieve contributor rankings.
  SRS: FR-03 System shall allow users to view contributor rankings for a GitHub repository
  verification: System Test (T1, T2, T28, T30)

- URS: URS-03 Allow users to input a GitHub organization name (i.e., URL) and retrieve contributor rankings.
  SRS: FR-04 System shall allow users to view contributor rankings for a GitHub organization
  verification: System Test (T5, T6, T31, T23, T25)

- URS: URS-04 Allow users to input a GitHub repository name (i.e., URL) and retrieve their specific ranking for life time of the project.
  SRS: FR-05 System shall allow contributors to view their specific ranking for the project lifetime
  verification: System Test (T7, T11, T26, T30, T18)

- URS: URS-05 Allow users to input a GitHub repository name (i.e., URL) and retrieve their specific ranking for the specific phase of the project.
  SRS: FR-06 System shall allow contributors to view their specific ranking for a given project phase
  verification: System Test (T8, T33, T12)

- URS: URS-06 Display the most active contributor(s) based on commit count.
  SRS: FR-07 System shall calculate the most active contributor(s) by measuring each contributor's commit count and display the resulting contributor rankings based on this pre-defined metric.
  verification: System Test (T1, T3, T7, T8, T9, T10, T11, T12, T13, T14, T28, T30, T32, T31, T33)

- URS: URS-06 Display the most active contributor(s) based on commit count.
  SRS: FR-08 If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. 
  verification: System Test (T9, T10, T11, T12)

- URS: URS-07 Allow users to filter rankings by specific time periods
  SRS: FR-09 System shall allow users to filter contributor rankings by specific time periods (i.e. project phase)
  verification: System Test (T8, T12, T13, T14, T33)

- URS: URS-07 Allow users to filter rankings by specific time periods
  SRS: FR-10 If the user requests to filter contribution rankings, the system shall display the contributor rankings based on contributions made within the specified time period.
  verification: System Test (T8, T12, T13, T14, T33)

- URS: URS-07 Allow users to filter rankings by specific time periods
  SRS: FR-11 System shall display "No contributions found for the specified time period" if no contributions found during specified time period.
  verification: System Test (T17, T27, T16, T15)

- URS: URS-10 Allow users to download contributor rankings in JSON format.
  SRS: FR-12 System shall allow users to download contributor rankings in JSON format by specifying an export request on the command line. 
  verification: System Test (T19, T20, T21, T22)

- URS: URS-10 Allow users to download contributor rankings in JSON format.
  SRS: FR-13 If the user requests to download contributor rankings in JSON format, the system shall convert the contribution data into a JSON format and download the generated file into the user's device.
  verification: System Test (T19, T20)

- URS: URS-12 System shall provide error handling mechanisms for API rate limit.
  SRS: FR-14 System shall detect API rate limit failures and notify users who request access with "Cannot access GitHub API data due to an exceed in rate limit, please try again later".
  verification: System Test (Failure Handling, T34)

- URS: URS-12 System shall provide error handling mechanisms for access restrictions
  SRS: FR-15 System shall prevent access to user requests for accessing unauthorised organisations and display "Access denied: user is not authorised to access this organisation".
  verification: System Test (T23)

- URS: URS-12 System shall provide error handling mechanisms for invalid repository names
  SRS: FR-16 If the user inputs invalid organisation name, the system shall display "Invalid URL: Organisation doesn't exist" and allow them to enter a different organisation name on the command line.
  verification: System Test (Failure handling, T25)

- URS: URS-12 System shall provide error handling mechanisms for invalid repository names
  SRS: FR-17 If the user inputs invalid repository name, the system shall display "Invalid URL: Repository doesn't exist" and allow them to enter a different repository name on the command line.
  verification: System Test (Failure handling, T24)

- URS: Empty repository
  SRS: FR-18 If the user requests contribution data for an empty repository, the system shall display "No contributions found" and allow them to enter a different repository name on the command line.
  verification: System Test (T18, T17, T2, T15, T21)

- URS: Empty organisation
  SRS: FR-19 If the user requests contribution data for an empty organization, the system shall display "No contributions found" and allow them to enter a different organization name on the command line.
  verification: System Test (T22, T6, T16)

- URS: Contributor with no contributions view specific ranking for project lifetime
  SRS: FR-20 If a contributor with no contributions requests to view their personal ranking, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line.
  verification: System Test (T26)

- URS: Contributor with no contributions in valid repository/organisation
  SRS: FR-21 If a user requests contributor rankings for a repository/orgnaisation containing contributors with no contributions, the system shall not display them in the contributor rankings.
  verification: System Test (T28, T29)
  
- URS: Contributor with no contributions view specific ranking for specific time period
  SRS: FR-22 If a contributor requests to view their personal contribution ranking for a specific time period where they have made no contributions, the system shall display "No user contributions found" and allow them to enter a different repository name on the command line.
  verification: System Test (T27)


  - URS: URS-09 Store authentication tokens if required for private repositories
  SRS: FR-23 System shall store user authentication tokens for accessing private organisations as needed, in the database.
  verification: System Test (T23, T1, T5, T7) ERROR HANDLING DATA REQUIREMENTS