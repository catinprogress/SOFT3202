## (a) Identify the most active contributor.
  - Given that I have entered a valid GitHub repository name (i.e., URL), when I request contributor rankings, the system must display the name of the most active contributor based on commit count.
  
  - Given that a repository has multiple contributors with the exact same number of commits, when I request contributor rankings, the system must display all equally active contributors.

  - Given that there exists a repository with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributions found") and allow me to enter a different repository name.
  
  - Given that the GitHub API rate limit has exceeded, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "GitHub API rate limit exceeded. Please try again later") and allow me to access the repository data when the rate limit resets.
  
  - Given that there exists a private organisation that I am not authorised to access, when I request contributor rankings, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: unauthorised organisation") before allowing me to enter a different repository name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: Invalid login credentials")
  
  - Give that I have entered an invalid GitHub repository name (i.e. URL), when I request contributor rankings, the system must notify me with an appropriate message (e.g. "Invalid URL: Repository doesn't exist") and allow me to enter a different repository name. 

  - Given that I have entered a valid GitHub repository name (i.e. URL), when I request contributor rankings, the system must display results within 5 seconds under normal conditions.

## (b) Filter Contribution Rankings by Time Periods
  - Given that I have entered a valid GitHub Repository name (i.e. URL) for my product and specific time period to filter results by, when I request contributor rankings, the system must display contributor rankings based only on contributions made to the repository during the selected time period.

  - Given that there exists a time period where no contributions were made to the repository I oversee, when I request contribution rankings for that time period, the system must notify me with an appropriate message (e.g. "No contributions found for the specified time period") and allow me to enter a different time-based filter.

  - Given that there exists a time period where multiple contributors made the exact same number of commits to the repository I oversee, when I request contributor rankings, the system must display all equally active contributors with the same ranking.
  
  - Given that there exists a repository with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributions found") and allow me to enter a different repository name.
  
  - Given that the GitHub API rate limit has exceeded, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "GitHub API rate limit exceeded. Please try again later") and allow me to access the repository data when the rate limit resets.
  
  - Given that there exists a private organisation that I am not authorised to access, when I request contributor rankings, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: unauthorised organisation") before allowing me to enter a different repository name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: Invalid login credentials")

  - Give that I have entered an invalid GitHub repository name (i.e. URL), when I request contributor rankings, the system must notify me with an appropriate message (e.g. "Invalid URL: Repository doesn't exist") and allow me to enter a different repository name. 

  - Given that I have entered a valid GitHub repository name (i.e. URL) for the project I oversee, when I request contributor rankings, the system must display results within 5 seconds under normal conditions.
  

### (c) Show My Contribution Ranking over Different Time Periods
  
* Show My Contribution Ranking over Different Time Periods
  - Given that I have entered a valid GitHub repository name (i.e. URL) for my product and specific time period to filter results by, when I request my personal contributor ranking, the system must display my personal ranking based only on contributions made to the repository during the selected time period.

  - Given that there exists a specific project phase where I have made the same number of commits to the repository as one or more other contributor/s, when I request my personal contribution ranking for that time period, the system must display me with the same ranking with all the other equally active contributors. 

  - Given that no contributions have been made to the repository I am a contributor of, when I request my personal ranking, the system must notify me with an appropriate message (e.g. "No contributions found").
  
  - Given that there exists a specific project phase where no commits were made to the repository, when I request my personal ranking for that time peiord, the system must notify me with an appropriate message (e.g. "No contributions found for the specified time period") and allow me to enter a different time-based filter.
  
  - Given that I have entered a URL for a repository that I have made no contributions to, when I request my personal contributor ranking, the system must notify me with an appropriate message (e.g. "No user contributions found") and allow me to enter a different repository name.
  
  - Given that there exists a specific project phase where I have made no commits to the repository, when I request my personal contributor ranking for that specific time period, the system must notify me with appropriate message (e.g. "No user contributions found for the specified time period") and allow me to enter a different time-based filter.

  - Given that the GitHub API rate limit has exceeded, when I request my personal contributor ranking, the system must notify me with an appropriate message (e.g. "GitHub API rate limit exceeded. Please try again later") and allow me to access my ranking when the rate limit resets.
  
  - Given that there exists a private organisation that I am not authorised to access, when I request my personal contributor ranking, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: unauthorised organisation") before allowing me to enter a different repository name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: Invalid login credentials")
  
  - Give that I have entered an invalid GitHub repository name (i.e. URL), when I request my personal contributor ranking, the system must notify me with an appropriate message (e.g. "Invalid URL: Repository doesn't exist") and allow me to enter a different repository name. 

  - Given that I have entered a valid GitHub repository name (i.e. URL) for my product, when I request my personal contributor ranking, the system must display results within 5 seconds under normal conditions.

### (d) Export Contributor Data in JSON format
* Export Contributor Data in JSON Format
  - Given that I have entered a valid, non-empty Github organization name (i.e. URL), when I request to export the contributor data, the system must generate and download a JSON file of the organization-level contributor rankings into my device within 5 seconds.

  - Given that I have entered a valid, non-empty GitHub repository name (i.e. URL), when I request to export the contributor data, the system must generate and download a JSON file of the repository-level contributor rankings into my device within 5 seconds.
  
  - Given that the tool successfully generates and downloads a JSON file into my device, when I view this report, the file must contain a complete and accurate calculation of all the requested contributor rankings based on commit count into a JSON-format.
  
  - Given that my downloaded JSON file contains accurately converted contributor rankings, when I view this report, the file must also contain enough relevant contributor data (e.g. name, commit activity, time period) in a clearly identifiable and logical manner so that I can integrate it with other internal analytics tools.
  
  - Given that the GitHub API rate limit has exceeded, when I request to export the contributor data, the system must notify me with an appropriate message (e.g. "GitHub API rate limit exceeded. Please try again later") and allow me to access the organisation data when the rate limit resets.
  
  - Given that there exists a private organisation that I am not authorised to access, when I request to export contributor data, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: unauthorised user") before allowing me to enter a different organisation name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: Invalid login credentials").
  
  - Given that there exists an organisation or repository with no contributions, when I request to export the contributor data, the system must notify me with an appropriate message (e.g. "No contributions available for export") and allow me to enter a different GitHub URL.

  - Given that I requested to export contributor data for a repository or organisation containing multiple contributors with the exact same number of commits, when the system generates the JSON file, the exported contributor rankings must include all equally active contributors with the same ranking.
  
  - Given that I have entered an invalid GitHub organisation name (i.e. URL), when I request to export the contributor data, the system must notify me with an appropriate message (e.g. "Invalid URL: Organisation doesn't exist") and allow me to enter a different organisation name.

  - Given that I have entered an invalid GitHub repository name (i.e. URL), when I request to export the contributor data, the system must notify me with an appropriate message (e.g. "Invalid URL: Repository doesn't exist") and allow me to enter a different organisation name.
