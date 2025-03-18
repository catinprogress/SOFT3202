As a team lead, I want to see the ranking of contributors in my product. I also want to
filter contributor rankings by specific time periods in my product so that I can evaluate
contributions of engineers over different project phases

### (b) Filter Contribution Rankings by Time Period
* **Actors**: Team Lead
* **Preconditions**:
  - The user has access to the GitHub repositories that are related to the product they oversee.
  - The repository that the user selects is not empty.
  - The tool must have API access to retrieve repository data.
  - The tool must support a filtering option for displaying contribution data by specific time periods
* **Main Flow**:
  - The TL logs in to tool using their GitHub Credentials     
  - The TL selects a Github repository by entering a repository name.   
  - The tool fetches and processes contribution data.
  - The system displays overall project lifetime contribution rankings for the most active contributors based on pre-defined metrics.
  - The TL selects a pre-defined time filter (e.g. last week, last month, last year).
  - The tool filters and sorts contribution data according to the specified time period.
  - The system displays the contribution rankings within the selected time period.
* **Alternative Flow (1)**: API rate limit exceeded
  - The Team Lead is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Private repository
  - The Team Lead is told that they cannot access the repository due to access restrictions
  **Alternative Flow (3)**: Empty repository is selected
  - The Team Lead is told that there is no contribution data available due to the repository being empty.
* **Alternative Flow (4)**: No contribution data for specified time period
  - The Team Lead is told that they cannot access the contribution rankings due to no contributions being made during this time period.
* **Post conditions**:
  - The contributor rankings are displayed based on contributions made within the user's specified time period.
 

As a software engineer, I want to know my ranking in both the life time of the project as
well as the latest phase of the project

### (c) Show My Contribution Ranking over Different Time Periods
* **Actors**: Software Engineer
* **Preconditions**:
  - The user has access to the GitHub repositories that they contribute to.
  - The tool must have API access to retrieve repository data.
  - The tool must support a filtering option for displaying indivdiual contribution data over specific time periods
* **Main Flow**:
  - The SE logs in to tool using their GitHub Credentials
  - The SE selects a Github repository by entering a repository name
  - The tool fetches and processes the user's contribution data based on pre-defined metrics.
  - The system displays a personal dashboard displaying the user's ranking in both the overall and latest phase contributions for the project.
  - The SE selects a pre-defined time filter (e.g. last week, last month, last year).
  - The tool filters and sorts the user's contribution data according to the specified time period.
  - The system displays the SE's contribution ranking within the selected time period, along with the metric's used to measure their contributions.
* **Alternative Flow (1)**: API rate limit exceeded
  - The Software Engineer is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Private repository
  - The Software Engineer is told that they cannot access the repository due to access restrictions.
  **Alternative Flow (3)**: Empty repository is selected
  - The Software Engineer is told that there is no contribution data available due to the repository being empty.
* **Alternative Flow (4)**: No contribution data for specified time period
  - The Software Engineer is told that they cannot access the contribution rankings due to no contributions being made during this time period.
* **Post conditions**:
  - The user's specific contributor ranking is displayed within their selected time period, along with the metrics used to measure and rank their contributions.

As an IT administrator, I want the tool to generate exportable reports in JSON format so that I can integrate the data with other internal analytics tools.
  ### (d) Export Contributor Data in JSON format
* **Actors**: IT Administrator
* **Preconditions**:
  - The user has access to the GitHub organization.
  - The tool must have API access to retrieve organization data.
  - The tool must support an export option in JSON format.
* **Main Flow**:
  - The IA logs in to tool using their GitHub Credentials
  - The IA selects a Github organization by entering an organization name.
  - The tool fetches and processes contributor data for repositories within the organization.
  - The system displays a report of the most active contributor rankings along with the pre-defined metrics the calculations were based on.
  - The IA selects requests to download the contributor data as a JSON file by specifying an export request 
  - The tool converts contribution data into JSON format and generates a downloadable report.
  - The system downloads the JSON file into the IA's device.
* **Alternative Flow (1)**: API rate limit exceeded
  - The IT Administrator is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Unauthorised or Private organization
  - The IT Administrator is told that they cannot access the organization due to access restrictions.
  **Alternative Flow (3)**: Empty organisation is selected
  - The IT Administrator is told that there is no contribution data available due to the organisation being empty.
* **Post conditions**:
  - The user has a JSON-formatted report of the contributor data saved into their device.
  - 