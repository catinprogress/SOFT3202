# Software Requirements Specification (SRS)

## 1. Introduction

### (a) Purpose
The purpose of this document is to define the formal technical specifications (the "how")
for the GitHub Activity Tracker tool built by Contract Hub for Advanced Medical Devices. This system will fetch contribution data from GitHub repositories, analyze commit
activity, and determine the most active contributors.

### (b) Scope
This tool will analyze GitHub repositories to determine the most active contributor based
on predefined metrics. The tool will be designed to support multiple repositories and
provide clear and accurate results. The system will be used by engineering managers and
team leads.

### (c) Intended Audience
- Engineering teams at Contract Hub, responsible for development.
- QA/Test teams, ensuring that the system meets functional and performance requirements.

### (d) References
i. GitHub REST API Documentation
ii. OAuth Authentication Guide

## 2. System Overview

The GitHub Activity Tracker is a standalone tool designed to integrate with the GitHub API. It
will be used by Advanced Medical Devices (AMD) to analyze commit history, rank contributors, and generate reports. The system does not modify repository contents but reads contribution data.

**System Functions**

The system will:
- Authenticate with GitHub API using OAuth.
- Retrieve commit history from specified repositories.
- Process commit data to determine the most active contributor.
- Provide ranking and filtering options based on time periods.
- Export contributor rankings in JSON format.

**User Characteristics**

The primary users are:
- Engineering Managers - View reports on the most active contributors.
- Team Leads - Track and analyze team contributions.
- Software Engineers - Check their own rankings and contribution levels.
- IT Administrators - Manage authentication, security, and API access.

**Constraints**
- The system must use the GitHub REST API.
- API requests are subject to GitHub's rate limits.
- Authentication must be handled via OAuth tokens.
- The system must return results within 5 seconds.

**Assumptions and Dependencies**
- The repository must exist and be accessible to the user.
- Users must have the necessary permissions to retrieve commit history.
- The system depends on the availability of the GitHub API.

## 3. Functional Requirements

FR-01 (Medium) The system shall allow users to authenticate via the GitHub API by specifying a credentials file on the command line (map: URS-01).

FR-02 (Medium) If the user enters an incorrect credentials file, the system shall prevent access and display "Authentication failed: Invalid login credentials". (map: URS-12; negative)

FR-03 (Medium) The system shall allow users to view contributor rankings for a GitHub repository by specifying a GitHub repository name for an organization they have authorised access to on the command line. (map: URS-02)

FR-04 (Medium) The system shall allow users to view contributor rankings for a GitHub organization by specifying an organization name that they have authorised access to on the command line. (map: URS-03)

FR-05 (Medium) The system shall allow contributors to view their specific ranking for the project lifetime by specifying a repository name that they are a contributor of on the command line. (map: URS-04)

FR-06 (Medium) The system shall allow contributors to view their specific ranking for a given project phase by specifying a valid repository name and time-based filter on the command line. (map: URS-05)

FR-07 (Medium) The system shall calculate and display a ranking of the most active contributor(s) within the requested organisation or repository based on each contributor's commit count. (map: URS-06)
  
FR-08 (Medium) If the system calculates a given user is equally active with at least one other contributor, the system shall display all equally active contributors with the same ranking. (map: URS-06)

FR-09 (Medium) If a user specifies a time-based filter for a valid repository or organisation on the command line, the system shall process and display a ranking of the most active contributor(s) within the requested time period. (map: URS-07)

FR-10 (Medium) If no contributions are found for the specified time period, the system shall display "No contributions found for the specified time period". (map: URS-07; negative)

FR-11 (Medium) The system shall process authenticated user requests for contributor data via GitHub API and provide the retrieved results on the command line. (map: URS-08)

FR-12 (Medium) If an authentication token is specified by the user via the command line, the system shall store it in the database to access private GitHub organisations. (map: URS-09)

FR-13 (Medium) When a user requests to export contributor rankings for a valid repository/organisation via the command line, the system shall generate a JSON file and make it available for download. (map: URS-10)

FR-14 (Medium) When a contributor requests to export their specific ranking for a repository that they have contributed to, the system shall generate a JSON file containing their individual contributor data and make it available for download. (map: URS-10)

FR-15 (Medium) If a user specifies a valid time-based filter with their export request, the system shall generate a JSON file containing the filtered contribution data and make it available for download. (map: URS-10)

FR-16 (Medium): If a user requests contributor data when the GitHub API rate limit has exceeded, the system shall display "GitHub API rate limit exceeded. Please try again later" and resume processing requests when the rate limit resets. (map: URS-12)

FR-17 (Medium) If a user specifies an unauthorized organization name on the command line, the system shall prevent access and display "Access denied: unauthorised organisation".(map: URS-12; negative)

FR-18 (Medium) If a user specifies a non-existing organisation or repository name on the command line, the system shall display "Invalid URL provided". (map: URS-12; negative)

FR-19 (Medium) If the user specifies an empty organization or repository name (i.e. no content/initial commit exists) on the command line, the system shall display "No contributions found". (map: URS-12; negative)

FR-20 (Medium) If a contributor requests to view their specific ranking for a repository that they have made no contributions to, the system shall display "No user contributions found".(map: URS-04; negative)

FR-21 (Medium) The system shall only include contributors with at least one commit when processing and displaying contributor rankings within a given organisation or repository. (map: URS-06)

FR-22 (Medium) If a contributor requests to view their specific ranking in a time period for which they have made no contributions, the system shall display "No user contributions found for the specified time period". (map: URS-05; negative)

## 4. Interfaces

### (a) API Interfaces
- The system will interact with GitHub's REST API to fetch commit and contributor
data.
- Authentication will be handled via OAuth tokens.
- API endpoints include:
  - GET /repos/owner/repo/contributors
  - GET /repos/owner/repo/commits
  - GET /users/username/events/public

### (b) User Interface (UI)
- A command line interface for displaying ranked contributors.
- Filters for time-based contribution rankings.
- Export options for downloading JSON reports.

## 5. Data Requirements

### (a) Collected Data
- Contributor name, GitHub username
- Number of commits

### (b) Stored Data
- Temporary caching of contributor rankings
- User authentication tokens (secure storage)

## 6. System Architecture

### (a) Architecture Overview
- The system follows a client-server architecture where the server is GitHub.

### (b) Main Components
- UI: A command line UI using Python 3.12 standard libraries.
- Cache (Optional): A temporary cache for API responses.
- Authentication Module: OAuth authentication for secure API access.

## 7. Failure Handling

### (a) Error Handling
- Graceful degradation in case of API failures (retry mechanisms, user notifications).
- Handling private repository access errors.
- Validation of user inputs (e.g., invalid repository names).

### (b) API Rate Limits
- Implement exponential backoff for API requests.
- Cache recent results to reduce API calls.

## 8. Performance Benchmarks

### (a) Expected Response Times
- The system shall process API data within five seconds under normal conditions.
- Fetching and ranking contributors shall not exceed 3 seconds for repositories with
fewer than 10,000 commits.

### (b) Scalability Requirements
- The system must handle concurrent requests from multiple users.
- The system should scale to support thousands of repositories.

### (c) Load Handling
- Use load balancing for handling multiple concurrent API requests.
- Implement caching layers to minimize redundant API calls.

## 9. System Tests

T1 Scenario: Valid repository with multiple contributors
Expectation: Correct ranking of contributors displayed.

T2 Scenario: Valid repository with no contributors
Expectation: Error message: No contributions found.

T3 Scenario: Attempt to authenticate using a GitHub account
Expectation: System successfully authenticates and grant access.

T4 Scenario: Attempt to authenticate using invalid GitHub credentials file
Expectation: Error message: Authentication failed: Invalid login credentials.

T5 Scenario: Valid organisation with multiple contributors
Expectation: Correct ranking of contributors displayed.

T6 Scenario: Valid organisation with no contributors
Expectation: Error message: No contributions found.

T7 Scenario: View specific ranking for project lifetime in valid repository with multiple contributors
Expectation: Correct personal contributor ranking for project lifetime displayed

T8 Scenario: View specific ranking for specific project phase in valid repository with multiple contributors
Expectation: Correct personal contributor ranking within specified time period displayed.

T9 Scenario: Valid repository with multiple equally active contributors
Expectation: Correct equal ranking for equally active contributors displayed.

T10 Scenario: Valid organisation with multiple equally active contributors
Expectation: Correct equal ranking for equally active contributors displayed.

T11: Scenario: View specific ranking for valid repository with multiple equally active contributors for project lifetime
Expectation: Correct same personal contributor ranking with other equally active contributors displayed.

T12: Scenario: View specific ranking for specific project phase for valid repository with multiple equally active contributors
Expectation: Correct same personal contributor ranking with other equally active contributors within specified time period displayed.

T13 Scenario: Filter contributor rankings for valid repository with multiple contributors by specific time period
Expectation: Correct contributor rankings for specified time period displayed

T14 Scenario: Filter contributor rankings for valid organisation with multiple contributors by specific time period
Expectation: Correct contributor rankings for specified time period displayed

T15 Scenario: Filter contributor rankings for valid repository with no contributors by specific time period
Expectation: Error message: No contributions found for the specified time period

T16 Scenario: Filter contributor rankings for valid organisation with no contributors by specific time period
Expectation: Error message: No contributions found for the specified time period

T17 Scenario: View specific ranking for specific project phase with no contributions in valid, non-empty repository.
Expectation: Error message: No contributions found for the specified time period.

T18: Scenario: View specific ranking for valid repository with no contributions.
Expectation: Error message: No contributions found.

T19 Scenario: Export contributor rankings for valid repository with multiple contributors in JSON format
Expectation: Correct contributor rankings downloaded in JSON formatted file.

T20 Scenario: Export contributor rankings for valid organisation with multiple contributors in JSON format
Expectation: Correct contributor rankings downloaded in JSON formatted file.

T21 Scenario: Export contributor rankings for valid repository with no contributors in JSON format
Expectation: Error message: No contributions found

T22 Scenario: Export contributor rankings for valid organisation with no contributors in JSON format
Expectation: Error message: No contributions found

T23 Scenario: Invalid authentication token provided for private organisation
Expectation: Error message: Access denied: unauthorised organisation.

T24 Scenario: Invalid repository name
Expectation: Error message: Invalid URL provided

T25 Scenario: Invalid organisation name
Expectation: Error message: Invalid URL provided

T26 Scenario: View specific ranking for valid non-empty repository with no user contributions
Expectation: Error message: No user contributions found

T27 Scenario: View specific ranking for specific project phase with no user contributions in valid non-empty repository
Expectation: Error message: No user contributions found for the specified time period

T28 Scenario: Valid repository containing contributors with no contributions
Expectation: Correct ranking of only contributors with at least one contribution displayed.

T29 Scenario: Valid organisation containing contributors with no contributions
Expectation: Correct ranking of only contributors with at least one contribution displayed.

T30: Valid repository with 1 contributor
Expectation: Single contributor is displayed with first ranking.

T31: Valid organisation with 1 contributor
Expectation: Single contributor is displayed with first ranking.

T32: View specific ranking for valid repository with no other contributors.
Expectation: Personal ranking is displayed as 1st.

T33: View specific ranking for specific project phase in valid repository with no other contributors.
Expectation: Personal ranking is displayed as 1st.

T34 Scenario: Attempt to request GitHub API data when rate limit exceeded
Expectation: Error message: GitHub API rate limit exceeded. Please try again later

T35 Scenario: Valid authentication token for private organisation provided 
Expectation: Retrieved token matches stored token and requested organisation data is displayed.

T36 Scenario: Export specific ranking for valid repository with no user contributions.
Expectation: Error message: No user contributions found

T37 Scenario: Export specific ranking for valid repository with multiple contributors
Expectation: Correct specific contributor ranking downloaded in JSON formatted file

T38 Scenario: Export contributor rankings for specific time period in valid non-empty organisation in JSON format
Expectation: Correct contributor rankings for specified time period downloaded in JSON formatted file

T39 Scenario: Export contributor rankings for specific time period in valid non-empty reposistory in JSON format
Expectation: Correct contributor rankings for specifeed time period downloaded in JSON formatted file

T40 Scenario: Export specific ranking for specific project phase in valid non-empty reposistory in JSON format
Expectation: Correct personal ranking for specified time period downloaded in JSON formatted file

T41 Scenario: System Timeout/Delay while processing contributor ranking
Expectation: Error message: Request timeout experienced. Please check GitHub API status or try again later.

T42 Scenario: Formatting error occurs for JSON export request
Expectation: Error message: Export failed: unexpected format received. Please check GitHub API status or try again later.

## 10. Non-Functional Requirements

### (a) Scalability Requirements:
The system shall support simultaneous access by thousands of engineers without performance degradation.
The system shall be designed to handle multiple concurrent API requests efficiently using
caching and rate-limiting mechanisms.
The system shall scale horizontally by distributing API requests and processing workloads
across multiple instances if necessary.

### (b) Performance Requirements:
The system shall process API data and return results within five seconds under normal
operating conditions.
The system shall fetch and rank contributors within three seconds for repositories with
fewer than 10,000 commits.
The system shall optimize API calls by implementing caching and batching mechanisms
where applicable.
The system shall include logging and monitoring tools to detect and resolve performance
bottlenecks.

### (c) Usability Requirements:
The system shall provide a user-friendly command-line interface (CLI) with clear instructions and minimal configuration steps.
The system shall allow users to filter contributor rankings by specific time periods (e.g.,
last week, last month, last year).
The system shall present error messages with meaningful descriptions and possible resolutions to guide users.
The system shall support exporting contributor rankings in JSON format for integration
with external analytics and reporting tools.
The system shall provide detailed usage documentation for engineers, team leads, and IT
administrators.

### (d) Security Requirements:
The system shall use OAuth authentication for secure access to the GitHub API and shall
not store user credentials in plain text.
The system shall encrypt all stored authentication tokens using industry-standard encryption techniques such as AES-256.
The system shall ensure all data transmissions occur over a secure channel using TLS 1.2
or higher.
The system shall log authentication attempts and API access activities for auditing and
security monitoring.
The system shall implement rate limiting and request throttling mechanisms to prevent
API abuse.
The system shall follow the principle of least privilege, ensuring that users can only access
data relevant to their role.

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
  verification: System Test (T23, T35) 
- URS: URS-10 Allow users to download contributor rankings in JSON format.
  SRS: FR-13 When a user requests to export contributor rankings via the command line, the system shall generate a JSON file and make it available for download
  verification: System Test (T19, T20, T38, T39)
- URS: URS-10 Allow users to download contributor rankings in JSON format
  SRS: FR-14 When a contributor requests to export their specific ranking for a repository that they have contributed to, the system shall generate a JSON file containing their individual contributor data and make it available for download.
  verification: System Test (T37, T40)
- URS: URS-10 Allow users to download contributor rankings in JSON format
  SRS: FR-15 If a user specifies a valid time-based filter with their export request, the system shall generate a JSON file containing the filtered contribution data and make it available for download.
  verification: System Test (T38, T39, T40)
- URS: URS-12 System shall provide error handling mechanisms for API rate limit. 
  SRS: FR-16 If a user requests contributor data when the GitHub API rate limit has exceeded, the system shall display "GitHub API rate limit exceeded. Please try again later" and resume processing requests when the rate limit resets.
  verification: System Test (T34)
- URS: URS-12 System shall provide error handling mechanisms for access restrictions (negative)
  SRS: FR-17 If a user specifies an unauthorized organization name on the command line, the system shall prevent access and display "Access denied: unauthorised organisation".
  verification: System Test (T23)
- URS: URS-12 System shall provide error handling mechanisms for invalid repository names (negative)
  SRS: FR-18 If a user specifies a non-existing organisation or repository name on the command line, the system shall display "Invalid URL provided".
  verification: System Test (T25, T24)
- URS: URS-12 Empty repository/organisation (negative)
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

## 12. Changelog

2025-02-25 — Created by (Contract Hub Engineering Team)
2025-02-26 — Signed off by (Contract Hub Customer Team lead)