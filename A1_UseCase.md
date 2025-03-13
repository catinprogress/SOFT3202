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
  - The system displays a personal dashboard displaying the user's ranking in both the overall and latest phase contributions for the project.
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