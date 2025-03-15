## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line. (map: URS-01).

URS-01 The system shall support authentication and authorization via GitHub API.
- If the user enters incorrect credentials, the system shall display "Access denied: Invalid login credentials" and prevent access.
  
URS-02 The system shall allow users to input a GitHub repository name and retrieve contributor rankings.
  - The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name on the command line for which they have authorised access to. 

URS-03 The system shall allow users to input a GitHub organization name and retrieve contributor rankings.
  - The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they are authorised to access on the command line.

URS-04 The system shall allow users to input a GitHub organization name and retrieve their specific ranking for life time of the project.
  - The system shall allow contributors to view their specific ranking for life time of the project by specifying a repository name that they are a contributor of on the command line.

URS-05 The system shall allow users to input a GitHub organization name and retrieve their specific ranking for the specific phase of the project.
  - The system shall allow contributors to view their specific ranking for the latest phase of the project by specifying a repository name that they are a contributor of on the command line.

URS-06 The system shall display the most active contributor(s) based on commit count.
  - The system shall calculate the most active contributor(s) within a given repository or organisation using predefined metrics that are based on each contributor's commit data (e.g. number of commits, pull requests merged, and lines of code added/removed)
  - If the user requests contributor rankings for a given repository or organisation by specifying the repository/organisation name on the command line, the system shall produce a report displaying the contribution rankings based on the most active contributor(s) within the specified repository or organisation.
  - If the user requests contributor rankings for a given repository or organisation and the system calculates multiple contributors with the same commit count, the system shall display all the equally active contributors with the same ranking.
  
  - If the user requests the most active contributor(s) for a given repository or organisation and the system calculates multiple contributors with the greatest commit count, the system shall display all the contributors as ranked equally most active.

URS-07 The system shall allow users to filter rankings by specific time periods (e.g., last week, last month, last year).
  - The system shall allow users to filter contributor rankings by specific time periods by specifying a time period on the command line.
  - If the user selects a time-based filter that contains no contributions, then the system shall display "No contribution data exists for the specifed time period", and allow them to specify a different time filter.
  - If the user selects a time-based filter that contains contribution data, the system shall re-calculate and display the contributor rankings using only the contribution data that exists within the specified time period.
  
URS-09 The system shall securely store authentication tokens if required for private repositories, using industry-standard encryption techniques.
  - The system shall encrypt all authentication tokens for private repositories before storing them in the database.

URS-10 The system shall provide an export option to download contributor rankings in JSON format.
  - The system shall allow users to download contributor rankings in JSON format by providing an export option on the command line.
  - If the user requests to download contributor rankings by specifying an export request on the command line, the system shall convert the contribution data into a JSON format and download the generated file into the user's device.
  
URS-11 The system shall ensure encrypted communication for all data transmissions over the network.
  - The system shall use TLS encryption to ensure secure communication for all data transmissions over the network.
  
What happens when a user is not authenticated correctly?
  - If the user enters an incorrect credentials file when authenticating via the GitHub API, the system shall prevent access and display "Authentication failed: Incorrect login credentials" and prevent access.

What happens when a repository is empty?
  - If the user requests contribution data for an empty repository, the system shall display "No contributor data available for this repository" and allow them to enter a different repository name on the command line.
  
What happens when an organization is empty?
  - If the user requests contribution data for an empty organization, the system shall display "No contributor data available for this organization" and allow them to enter a different organization name on the command line.
  
What happens if a contributor has no contributions?
  - If a contributor requests to view their contribution ranking for a repository for which there exists no contributions from them, the system shall display "No contributor data for user exists for this repository" and allow them to enter a different repository name on the command line. 




URS-08 The system shall process API data and provide results within five seconds under normal conditions.
  - The system shall fetch and process API data and display a response to any query within five seconds under normal conditions.
 /// - If temporary caching is enabled, the system shall be able to accommodate up to 100 concurrent API requests from multiple users and maintain a response time of five seconds
 - If temporary caching is not enabled, the system shall be able to accommodate up to 20 concurrent API requests from multiple uses and maintain a response time of five seconds. 
 
URS-12 The system shall provide error handling mechanisms for API failures, including rate limit handling, access restrictions, and invalid repository names.
  - The system shall enforce role-based access control to process API requests for data handling within a given repository or organisation.

URS-13 The system shall support concurrent access by multiple users and handle parallel requests efficiently.

