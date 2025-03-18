# User Requirements Specification (URS)

## 1. Introduction

### (a) Purpose
The purpose of this document is to define the user requirements for a tool that identifies the most active contributor in a given GitHub repository (the "what"). This tool will be used by Advanced Medical Devices to recognize and reward software engineers based on their contributions.

### (b) Scope
The system will:
- Authenticate via the GitHub API.
- Retrieve commit data and analyze contributor activity.
- Provide contributor rankings based on predefined metrics.
- Export results in JSON format for integration with other tools.
- Ensure security and compliance with company policies.

### (c) Intended Audience
i. Software engineers at Advanced Medical Devices
ii. Engineering managers and team leads
iii. IT administrators
iv. Contractors and developers responsible for tool development

### (d) Definitions and Acronyms
i. GitHub – A cloud-based platform for version control and collaboration.
ii. Contributor – A user who makes commits, pull requests, or other changes to a repository.
iii. Commit – A change recorded in a GitHub repository.
iv. Pull Request (PR) – A proposed change submitted for review before merging.

## 2. System Overview
The tool will connect to GitHub repositories, fetch contribution data, and determine the most active contributor based on metrics such as the number of commits, lines of code added or removed, and pull requests merged. It will generate reports and provide a ranking of contributors.

## 3. Personas

### (a) Name: Sarah Thompson
**Role**: Engineering Manager
**Background**: Sarah is responsible for overseeing multiple software development teams across different products. She ensures that engineers are contributing effectively and wants to recognize top-performing developers to boost team motivation and engagement.
**Goals**: Identify the most active contributor across all company projects.
View top contributors for individual repositories to track team-level contributions.
Use this information to reward high-performing engineers and improve team morale.
**Pain Points**:
Lack of visibility into developer contributions across multiple projects.
Manually tracking activity across repositories is time-consuming.
Recognition of engineers is inconsistent due to difficulty in measuring contributions.
**System Expectations**:
- A report summarizing top contributors across all products.
- The ability to drill down into specific repositories for per-project rankings.
- Accurate data on commit activity.
- The ability to export contributor rankings for internal reporting and performance reviews.

### (b) Name: Jane Walker
**Role**: Team lead
**Background**: Jane oversees a team of software engineers working on multiple repositories. She is responsible for ensuring that engineers contribute effectively and for monitoring their engagement in the development process. She collaborates with engineering managers to align team efforts with project goals.
**Goals**: Track team-level contributions within specific repositories.
Identify top contributors within her team to provide recognition and feedback.
Ensure team members are fairly assessed based on their contributions.
**Pain Points**: Difficulty in manually tracking individual contributions across multiple repositories.
Lack of clear visibility into team member activity over different project phases.
Inconsistent and subjective methods of evaluating developer performance.
**System Expectations**:
The ability to view contributor rankings within her specific team's repositories.
Filtering options to evaluate contributions over different project phases.
Access to detailed breakdowns of commit activity for individual team members.
Exportable reports for team performance reviews and internal discussions.

### (c) Name: Samuel Davidson
**Role**: Software Engineer
**Background**: Samuel is a software engineer who actively contributes to multiple repositories. He primarily works on implementing new features, fixing bugs, and submitting pull requests. He is eager to understand how his contributions compare to those of his peers and seeks recognition for his work.
**Goals**:
Monitor his contribution ranking within different repositories.
Gain insights into his coding activity and areas for improvement.
Ensure that his contributions are recognized in performance evaluations.
**Pain Points**:
Limited visibility into how his contributions are measured and ranked.
Difficulty in tracking his progress across different phases of a project.
Lack of a standardized system for assessing individual developer contributions.
**System Expectations**:
A personal dashboard displaying his ranking in both lifetime and phase-specific contributions.
Ability to filter and analyze his contributions over different time periods.
Clear metrics showing the impact of his commits, pull requests, and code reviews.
Exportable data for personal records and performance reviews.

### (d) Name: Sandy Hong
**Role**: IT Administrator
**Background**: Sandy is responsible for managing authentication, security, and access control for various tools used by the engineering teams. She ensures that systems comply with security policies and that only authorized users can access sensitive data. She also oversees API integrations and system performance.
**Goals**:
Ensure secure authentication and authorization for all users accessing the tool.
Maintain compliance with company security policies and encryption standards.
Support seamless integration of the tool with internal analytics and reporting systems.
**Pain Points**:
Managing authentication for a large number of users across different access levels.
Ensuring secure data storage and encrypted communication while maintaining performance.
Handling API rate limits and potential system failures in a scalable manner.
**System Expectations**:
Robust authentication and authorization mechanisms integrated with GitHub API.
Secure storage of authentication tokens using industry-standard encryption.
Encrypted network communication for all data transmissions.
Exportable reports in JSON format for integration with internal security and analytics tools.

## 4. User Requirements

URS-01 The system shall support authentication and authorization via GitHub API.

URS-02 The system shall allow users to input a GitHub repository name and retrieve contributor rankings.

URS-03 The system shall allow users to input a GitHub organization name and retrieve contributor rankings.

URS-04 The system shall allow users to input a GitHub organization name and retrieve their specific ranking for life time of the project.

URS-05 The system shall allow users to input a GitHub organization name and retrieve their specific ranking for the specific phase of the project.

URS-06 The system shall display the most active contributor(s) based on commit count.

URS-07 The system shall allow users to filter rankings by specific time periods (e.g., last week, last month, last year).

URS-08 The system shall process API data and provide results within five seconds under normal conditions.

URS-09 The system shall securely store authentication tokens if required for private repositories, using industry-standard encryption techniques.

URS-10 The system shall provide an export option to download contributor rankings in JSON format.

URS-11 The system shall ensure encrypted communication for all data transmissions over the network.

URS-12 The system shall provide error handling mechanisms for API failures, including rate limit handling, access restrictions, and invalid repository names.

URS-13 The system shall support concurrent access by multiple users and handle parallel requests efficiently.

## 5. User Stories

* As a team lead, I want to see the ranking of contributors in my product. I also want to filter contributor rankings by specific time periods in my product so that I can evaluate contributions of engineers over different project phases.
* As a software engineer, I want to know my ranking in both the life time of the project as well as the latest phase of the project.
* As an IT administrator, I want the tool to generate exportable reports in JSON format so that I can integrate the data with other internal analytics tools.
* As an engineering manager, I want to view the most active contributor in all our products, as well as individual active contributors in each project, so that I can recognize and reward top-performing engineers.

## 6. Use Cases

### (a) Identify the most active contributor overall.
* **Actors**: Engineering Manager
* **Preconditions**:
  - The user has access to the GitHub organization
  - The tool must have API access to retrieve organization data.
* **Main Flow**:
  - The EM logs in to tool using their GitHub Credentials
  - The EM selects a Github organization by entering a URL
  - The tool fetches and processes contribution data
  - The system displays the most active contributor based on predefined metrics.
* **Alternative Flow (1)**: Private organization
  - The Manager is told that they cannot access the organization due to access restrictions.
* **Alternative Flow (2)**: API rate limit exceeded
  - The Manager is told that they cannot access the repository due to rate limit.
* **Post conditions**:
  - The most active contributor is displayed.

### (b) Filter Contribution Rankings by Time Period
* **Actors**: Team Lead
* **Preconditions**:
  - The user has access to the GitHub repositories that they oversee.
  - The tool must have API access to retrieve repository data.
  - The tool must support a filtering option for displaying contribution data by specific time periods
* **Main Flow**:
  - The TL logs in to tool using their GitHub Credentials     
  - The TL selects a Github repository by entering a URL     
  - The tool fetches and processes contribution data.
  - The system displays contribution rankings over the lifetime of the project.
  - The TL selects a predefined time filter (e.g. last week, last month, last year).
  - The tool filters and sorts contribution data according to the specified time period.
  - The system displays the contribution rankings within the selected time period.
* **Alternative Flow (1)**: API rate limit exceeded
  - The Team Lead is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Unauthorised repository
  - The Team Lead is told that they cannot access the repository due to access restrictions
* **Alternative Flow (3)**: No contribution data for specified time period
  - The Team Lead is told that they cannot access the contribution rankings due to no contributions being made during this time period.
* **Post conditions**:
  - The individual contribution rankings within the user's specified time period are displayed.
 
### (c) Show My Contribution Ranking over Different Time Periods
* **Actors**: Software Engineer
* **Preconditions**:
  - The user has access to the GitHub repositories that they contribute to.
  - The tool must have API access to retrieve the appropriate repository data.
  - The tool must support a filtering option for displaying indivdiual contribution data over specific time periods
* **Main Flow**:
  - The SE logs in to tool using their GitHub Credentials
  - The SE selects a Github organization by entering a URL
  - The tool fetches and processes the user's contribution data based on pre-defined metrics.
  - The system displays a personal dashboard displaying the user's ranking in both the overall and latest phase contributions for the()
  - The SE selects a pre-defined time filter (e.g. last week, last month, last year).
  - The tool filters and sorts the user's contribution data according to the specified time period.
  - The system displays the SE's contribution ranking within the selected time period, along with the metric's used to measure their contributions.
* **Alternative Flow (1)**: API rate limit exceeded
  - The Software Engineer is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Unauthorised organization
  - The Software Engineer is told that they cannot access the organization due to access restrictions.
* **Alternative Flow (3)**: No contribution data for specified time period
  - The Software Engineer is told that they cannot access the contribution rankings due to no contributions being made during this time period.
* **Post conditions**:
  - The individual contribution ranking for the user is displayed within their selected time period.

### (d) Export Contributor Data in JSON format
* **Actors**: IT Administrator
* **Preconditions**:
  - The user has access to the GitHub organization.
  - The tool must have API access to retrieve organization data.
  - The tool must support an export option in JSON format.
* **Main Flow**:
  - The IA logs in to tool using their GitHub Credentials
  - The IA selects a Github organization by entering a URL
  - The tool fetches and processes contribution data
  - The system displays a report of contributor rankings based on predefined metrics.
  - The IA selects the "Export Report as JSON" option
  - The tool structures the contribution data into JSON format
  - The system allows IA to download the JSON-formatted report
* **Alternative Flow (1)**: API rate limit exceeded
  - The IT Administrator is told that they cannot access the repository due to rate limit.
* **Post conditions**:
  - The user has exported the contributor data as a JSON-formatted report.

## 7. Use case diagram
(Skipped)
## 8. Non-Functional Requirements

### (a) Scalability Requirements:
The system should support simultaneous access by thousands of engineers.

### (b) Performance Requirements:
The system shall process API data and return results within five seconds under normal operating conditions.
The system shall efficiently manage API requests to prevent excessive delays or timeouts.

### (c) Usability Requirements:
The system shall provide a clear and intuitive interface for users to input repository details and retrieve rankings.
The system shall allow users to filter rankings by specific time periods to analyze contributions over different project phases.
The system shall present error messages in a user-friendly manner, ensuring that users understand any issues and possible resolutions.
The system shall allow exporting contributor rankings in a structured format for further analysis and reporting.

### (d) Security Requirements:
The system shall enforce authentication and authorization mechanisms to restrict access to authorized users only.
The system shall securely store authentication credentials and access tokens using industry-standard security practices.
The system shall ensure all data transmissions occur over an encrypted channel.
The system shall log authentication attempts and access activities for auditing and compliance purposes.
The system shall implement proper error handling to prevent unauthorized access to repository data.

## 9. Risks & Mitigation Strategies

* **Technical Risk**: The tool may hit Github rate limits
  **Mitigation**: Implement caching and request optimization through batch processing.
* **Security Risk**: Risk: Unauthorized access to contributor data.
  **Mitigation**: Implement strict authentication and authorization mechanisms to ensure that only authorized users can access the system. Enforce role-based access controls (RBAC) to limit data exposure.
  **Risk**: Exposure of sensitive authentication credentials.
  **Mitigation**: Store authentication tokens securely using industry-standard encryption techniques. Ensure that credentials are never stored in plain text and implement secure token management policies.
  **Risk**: Data interception during transmission.
  **Mitigation**: Enforce encrypted communication (e.g., TLS/SSL) for all data transmitted over the network to prevent man-in-the-middle attacks.

## 10. Constraints:
**Technology**:
- The company uses GitHub for its project.
- The company standardizes on Python, and expects Python to be the language of choice.
**Regulatory and Compliance**:
- The company expects you to follow industry practice in any data handling

## 11. Acceptance Criteria
* Identify the most active contributor overall.
  - The tool accepts a GitHub repository URL and correctly identifies the most active contributor.
  - The tool accepts a GitHub repository with multiple equally active contributors and displays all of them

* Filter Contribution Rankings by Time Periods
  - The tool allows users to filter contribution rankings according to specific time periods (e.g. last week, last month, last year)
  - The tool correctly identifies and displays valid time periods (i.e. within the project lifetime) that users can select to filter contribution rankings by.
  - When a user applies a time period filter, the system correctly displays only the contribution rankings within the specified time period.
//  - The system displays the filtered results within 5 seconds of the query being made and notifies users of any delay if time exceeds 5 seconds.
  - The system must display an appropriate message (e.g. "No contribution data for this period") if users select a time period with no contributions.
// - If a repository API rate limit is exceeded, the system must notify users that they cannot access this repository due to rate limit.
  
* Show My Contribution Ranking over Different Time Periods
  - The tool correctly identifies the repositories that the currently logged in software engineer is working on ///edit
  - The tool must calculate and display the user's contribution ranking according to pre-defined metrics (e.g. commits, lines of code added/removed, pull requests merged).
  - Upon successful login, the system must display a person dashboard of the user's overall and phase-specific contribution rankings.
  - The tool allows users to filter their personal contribution ranking over different time periods (e.g. last week, last month, last year)
  - The tool correctly identifies and displays valid time periods (i.e. within the project lifetime) that users can select to view their ranking in.
  - Upon selecting a time filter, the system correctly displays the contribution ranking within the specified time period.
  
* Export Contributor Data in JSON Format
  - The tool must clearly provide an option to export contributor data as a JSON-formatted report on the user interface that the user can select.
  - Upon selecting the Export Report as JSON option, the tool must generate a downloadable report in JSON format containing the contribution rankings.
  - The tool must accurately convert the contribution rankings that the currently logged in user has access to into JSON-format, and the generated report must include  all relevant contributor data in a clearly identifiable and logical manner.
  - The tool must generate a complete JSON-formatted report of the organization's contributor rankings that contains enough data for it to be used for integration with other internal analytics tools.
  - Given that the tool successfully generates the JSON formatted report, the file must be easily accessible on the user interface and the user must be notified that it is ready for download.
  - If no contributor data is available to export, the system must notify the user with an appropriate message (e.g. "No contributor data ready for export")
  
## 12. Changelog
2025-02-24 — Created by (Contract Hub Customer Team)
2025-02-25 — Signed off by (AMD Team lead)