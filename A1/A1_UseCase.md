### (a) Identify the most active contributor.
- **Actors:** Engineering Manager
- **Preconditions:**
  - The user has access to the GitHub organization
  - The tool must have API access to retrieve organization data.
- **Main Flow:**
  - The EM logs in to tool using their GitHub Credentials
  - The EM selects a Github repository by entering a URL
  - The tool fetches and processes contribution data
  - The system displays the most active contributor based on predefined metrics.
- **Alternative Flow (1):** Private organization
  - The Manager is told that they cannot access the organization due to access restrictions.
- **Alternative Flow (2):** API rate limit exceeded
  - The Manager is told that they cannot access the repository due to rate limit.
- **Post conditions:**
  - The most active contributor is displayed.

### (b) Filter Contribution Rankings by Time Period
* **Actors**: Team Lead
* **Preconditions**:
  - The user has access to the GitHub organization.
  - The tool must have API access to retrieve organization data.
  - The user has access to the GitHub repository for the product they oversee.
  - The tool must support time-based filtering for displaying contribution rankings over a specific project phase.
* **Main Flow**:
  - The TL logs in to tool using their GitHub Credentials. 
  - The TL selects a Github repository by entering a URL and specific time period to filter results by (e.g. last week, last month, last year).  
  - The tool fetches and processes contribution data that exists for the specified time period.
  - The system displays filtered contribution rankings for the most active contributors, based only on the commits made within the selected time period.
* **Alternative Flow (1)**: API rate limit exceeded
  - The Team Lead is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Private organization
  - The Team Lead is told that they cannot access the organization due to access restrictions
* **Alternative Flow (3)**: Empty repository is selected
  - The Team Lead is told that there is no contribution data available.
* **Alternative Flow (4)**: No contribution data for specified time period
  - The Team Lead is told that there is no contribution data available for the specified time period.
* **Alternative Flow (5)**: Invalid GitHub URL is entered
  - The Team Lead is told that the GitHub URL they have provided doesn't exist.
* **Post conditions**:
  - The filtered contributor rankings for the specified time period are displayed.
 
### (c) Show My Contribution Ranking over Different Time Periods
* **Actors**: Software Engineer
* **Preconditions**:
  - The user has access to the GitHub organization.
  - The user has access to the GitHub repository that they contribute to.
  - The tool must have API access to retrieve organization data.
  - The tool must support time-based filtering for displaying a personal contribution ranking over a specific project phase.
* **Main Flow**:
  - The SE logs in to tool using their GitHub Credentials
  - The SE selects a Github repository by entering a URL and specific time period to filter results by (e.g last week, last month, last year)
  - The tool fetches and processes the contribution data.
  - The system displays a personal dashboard displaying the SE's contributor ranking for the selected time period, based on their commit count.
* **Alternative Flow (1)**: API rate limit exceeded
  - The Software Engineer is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Private organization
  - The Software Engineer is told that they cannot access the organization due to access restrictions.
* **Alternative Flow (3)**: Empty repository is selected
  - The Software Engineer is told that there is no contribution data available.
* **Alternative Flow (4)**: No contribution data for specified time period
  - The Software Engineer is told that there is no contribution data available for the specified time period.
* **Alternative Flow (5)**: No user contributions found for selected repository
  - The Software Engineer is told that there is no user contribution data available.
* **Alternative Flow (6)**: No user contributions found for selected time period
  - The Software Engineer is told that there is no user contribution data available for the specified time period.
* **Alternative Flow (7)**: Invalid GitHub URL is entered
  - The Software Engineer is told that the GitHub URL they have provided doesn't exist.
* **Post conditions**:
  - The Software Engineer's specific contributor ranking for the specified time period is displayed.

  ### (d) Export Contributor Data in JSON format
* **Actors**: IT Administrator
* **Preconditions**:
  - The user has access to the GitHub organization.
  - The tool must have API access to retrieve organization data.
  - The tool must support an export option to generate downloadable reports in JSON format.
* **Main Flow**:
  - The IA logs in to tool using their GitHub Credentials
  - The IA selects a Github organization by entering a URL along with an export request.
  - The tool fetches and processes contributor data for repositories within the organization.
  - The tool generates a JSON file of the contributor rankings calculated based on predefined metrics.
  - The system downloads the JSON file into the IA's device.
* **Alternative Flow (1)**: API rate limit exceeded
  - The IT Administrator is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Private organization
  - The IT Administrator is told that they cannot access the organization due to access restrictions.
* **Alternative Flow (3)**: Empty organisation is selected
  - The IT Administrator is told that there is no contribution data available to export.
* **Alternative Flow (4)**: GitHub Repository is selected for export
  - System generates a JSON file of repository-level contributor rankings and makes it available for download. 
* **Alternative Flow (5)**: Invalid GitHub URL is entered
  - The IT Administrator is told that the GitHub URL they have provided doesn't exist.
* **Post conditions**:
  - A JSON file containing the requested contributor ranking data is downloaded into the IT Administrator's device.