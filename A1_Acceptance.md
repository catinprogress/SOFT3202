* Filter Contribution Rankings by Time Periods
  - Given that I have entered a valid GitHub Repository name (i.e. URL) that is related to my product, when I request contributor rankings, the system must initially display a ranking of most active contributors over the project lifetime, along with the pre-defined metrics that the calculations were based on.
  
  - Given that I have requested contributor rankings, when the system displays the most active contributors over the project lifetime, the system must also provide option to filter the rankings by a specific time periods (e.g. last week, last month, last year) 

  - Given that I have requested contribution rankings and the tool supports time-based filtering, when I request a specific time period to filter results by, the system must display only the rankings that correspond to contributions made during the specified time period.

  - Given that there exists a time period in my project lifecycle in which no contributions were made to the selected repository, when I select that time period to filter contribution rankings by, the system must notify me with an appropriate message (e.g. "No contribution data exists for this period").


  -  Given that a repository has multiple contributors with the exact same number of commits, when I request contributor rankings, the system must display all equally active contributors 
  -  Given that there exists a specific time period containing multiple contributors with the exact same number of commit, when I request contribution rankings to be filtered by that time period, the system must display all equally active contributors
-  
  -  Given that there exists a repository or organisation with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributor data exists for this repository") and allow me to enter a different repository or organisation name
  -  Given that there exists a specific time period containing no contributions, when I request contribution rankings to be filtered by that time period, the system must notify me with an appropriate message (e.g. "No contribution data exists for this time period") and allow me to choose a different time filter option. 
  -  Given that a repository where API rate limit has exceeded, when I request contributor rankings for that repository, the system must notify me with an appropriate message (e.g. "Cannot currently access contributor data for this repository due to rate limit exceed") and allow me to enter a different repository name.
  - Given that there exists a repository that I am not authorised to access, when I request contributor rankings, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different repository name. 


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
* **Alternative Flow (2)**: Unauthorised or Private repository
  - The Software Engineer is told that they cannot access the repository due to access restrictions.
  **Alternative Flow (3)**: Empty repository is selected
  - The Software Engineer is told that there is no contribution data available due to the repository being empty.
* **Alternative Flow (4)**: No contribution data for specified time period
  - The Software Engineer is told that they cannot access the contribution rankings due to no contributions being made during this time period.
* **Post conditions**:
  - The user's specific contributor ranking is displayed within their selected time period, along with the metrics used to measure and rank their contributions.
  
* Show My Contribution Ranking over Different Time Periods
  - Given that I have entered a repository name for a repository that I am a contributor of, when I request my personal contributor ranking, the system must display a personal dashboard of my contribution rankings for the life time and latest phase of the project, along with the metrics used to calculate this ranking (e.g. the impact of my commits, pull requests and code review)
  
  - Given that I have entered a repository name for a repository that I am a contributor of, when I request my personal contributor ranking, the system must also provide an option to view my ranking over specific time periods (e.g. last week, last month, last year).
    
  - Given that I have specified a time period to view my contribution ranking in, when the system recalculates the contribution data, the system must display my personal ranking according to calculations made using only the contributions to the repository during the specific time period.

  - Given that I have requested my contribution ranking for a specific time period, when the system displays my personal ranking, the system should also display the metrics used to measure and rank my contributions to my peers (e.g. number of my commits, pull requests and code reviews)
   
  - Given that there exists a repository or specific time period containing no contributions from all contributors, when I request my personal ranking for that time period, the system must notify me with an appropriate message (e.g. "No contribution data exists for the specified time period") and allow me to request a different time filter.
- 
  - Given that there exists a repository for which I have made no contributions to, when I request my personal ranking for that repository, the system must notify me with an appropriate message ("No contributor data for user exists for this repository").

  -  Given that there exist a repository or time period where I have the same number of commits to one or more contributor/s, when I request my personal contribution ranking, the system must display my rank as equal to all of the other equally active contributors. 

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
  - The system displays a report of most active contributor rankings along with the pre-defined metrics the calculations were based on.
  - The system displays an option to export the report by as JSON file.
  - The IA selects the export option.
  - The tool converts contribution data into JSON format and generates a downloadable report.
  - The system downloads the JSON file into the IA's device.
* **Alternative Flow (1)**: API rate limit exceeded
  - The IT Administrator is told that they cannot access the repository due to rate limit.
* **Alternative Flow (2)**: Unauthorised or Private repository
  - The IT Administrator is told that they cannot access the repository due to access restrictions.
  **Alternative Flow (3)**: Empty repository is selected
  - The IT Administrator is told that there is no contribution data available due to the repository being empty.
* **Post conditions**:
  - The user has a JSON-formatted report of the contributor data saved into their device.
  - 
* Export Contributor Data in JSON Format
  - Given that I have entered a Github repository or organization name with contributors, when I request contributor rankings, the tool must provide an option to export contributor data in JSON-format.
 
  - Given that I have selected the export option for a non-empty GitHub repository or organisation, when the tool generates a JSON file of the contributor data, the system must download this file into my device and allow me to access it.
  
  - ///Then the file must be saved and available for me to access on my device within 5 seconds of confirmation.////


  - Given that the tool successfully generates and downloads the JSON file containing the contribution rankings into my device, when I view this report, the file must contain a complete and accurate conversion of all the contributor rankings into a JSON-format along with enough contributor data for it to be integrated with other internal analytics tools
- 
  - Given that the tool successfully generates and downloads the JSON file containing the accurately converted contribution rankings into my device, when I view this report, the file must include the pre-defined metrics used to calculate the rankings (e.g. number of commits, code reviews, pull requests) in a clearly identifiable and logical manner.
