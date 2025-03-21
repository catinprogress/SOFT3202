## (a) Identify the most active contributor.
  - Given that I have entered a valid GitHub repository name (i.e., URL), when I request contributor rankings, the system must display the name of the most active contributor based on commit count.
  
  - Given that a repository has multiple contributors with the exact same number of commits, when I request contributor rankings, the system must display all equally active contributors.

  - Given that I have requested contributor rankings for a valid repository, when the tool generates a report of the rankings, the system must display the name of the most active contributor/s along with the predefined metrics the calculations were based on.
  
  - Given that there exists a repository with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributions found") and allow me to enter a different repository name.
  
  - Given that there exists a repository where API rate limit has exceeded, when I request contributor rankings for that repository, the system must notify me with an appropriate message (e.g. "Cannot access repository due to an exceed in rate limit") and allow me to enter a different repository name.
  - 
  - 
  - Given that there exists a private organisation that I am not authorised to access, when I request contributor rankings, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different repository name.
- 
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")

## (b) Filter Contribution Rankings by Time Periods
  - Given that I have entered a valid GitHub Repository name (i.e. URL) for my product, when I request contributor rankings, the system must display a ranking of most active contributors over the project lifetime based on commit count.
  
  - Given that I have requested contributor rankings for a valid repository, when the tool generates a report of the rankings, the system must display the rankings along with the predefined metrics the calculations were based on.
  
  - Given that I have requested contributor rankings, when the system displays the most active contributors over the project lifetime, the system must also provide the option to filter the rankings by a specific time period (e.g. last week, last month, last year).

  - Given that I have requested contribution rankings and the tool supports time-based filtering, when I request a specific time period to filter results by, the system must display only the rankings that correspond to contributions made during the specified time period.

  - Given that there exists a time period in my project lifecycle in which no contributions were made to the repository, when I select that time period to filter contribution rankings by, the system must notify me with an appropriate message (e.g. "No contributions found for the specified time period").

  -  Given that a repository or time period has multiple contributors with the exact same number of commits, when I request contributor rankings, the system must display all equally active contributors with the same ranking
  
  -  Given that there exists a repository with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributions found") and allow me to enter a different repository name
  
  -  Given that there exists a specific time period containing no contribution data, when I request contribution rankings to be filtered by that time period, the system must notify me with an appropriate message (e.g. "No contributions found for the specified time period") and allow me to choose a different time filter option. 
- 
  -  Given that a repository where API rate limit has exceeded, when I request contributor rankings for that repository, the system must notify me with an appropriate message (e.g. "Cannot access repository due to an exceed in rate limit") and allow me to enter a different repository name.
- 
  - Given that there exists a private organisation that I am not authorised to access, when I request contributor rankings, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different repository name.
- 
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")
  

### (c) Show My Contribution Ranking over Different Time Periods
  
* Show My Contribution Ranking over Different Time Periods
  - Given that I have entered a repository name for a repository that I am a contributor of, when I request my personal contributor ranking, the system must display a personal dashboard of my contribution rankings for the life time and latest phase of the project, along with the metrics used to calculate this ranking.
  
  - Given that I have entered a repository name for a repository that I am a contributor of, when I request my personal contributor ranking, the system must also provide an option to view my ranking over specific time periods (e.g. last week, last month, last year).
    
  - Given that I have specified a time period to view my contribution ranking in, when the system recalculates the contribution data, the system must display my personal ranking based on only the contributions made to the repository during the specific time period.

  - Given that I have requested my contribution ranking for a specific time period, when the system displays my personal ranking, the system should also display the metrics used to measure and rank my contributions to my peers.
   
  - Given that there exists a repository containing no contributions, when I request my personal ranking, the system must notify me with an appropriate message (e.g. "No contributions found") and allow me to request a different repository.
- 
  - Given that there exists a specific time period containing no contributions, when I request my personal ranking, the system must notify me with an appropriate message (e.g. "No contributions found for the specified time period") and allow me to request a different time filter.
  
  - Given that there exists a repository for which I am a contributor of but have made no contributions to, when I request my personal contributor ranking, the system must notify me with appropriate message (e.g. "No user contributions found") and allow me to enter a different repository name
- 
  -  Given that there exists a time period where I have made no contributions to a repository I am a contributor of, when I request my personal contributor ranking for that specific time period, the system must notify me with appropriate message (e.g. "No user contributions found") and allow me to request a different time filter.

  -  Given that there exists a repository or time period within a repository where I have the same number of commits to one or more contributor/s, when I request my personal contribution ranking, the system must display my rank as equal to all of the other equally active contributors. 

  -  Given that there exists a repository where API rate limit has exceeded, when I request my personal contributor ranking for that repository, the system must notify me with an appropriate message (e.g. "Cannot access repository due to an exceed in rate limit") and allow me to enter a different repository name.
  
  - Given that there exists a private organisation that I am not authorised to access, when I request my personal contributor ranking, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different repository name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")
  

  ### (d) Export Contributor Data in JSON format
* Export Contributor Data in JSON Format
  - Given that I have entered a Github repository or organization name with contributions, when I request contributor rankings, the tool must provide an option to export contributor data in JSON-format.
 
  - Given that I have selected the export option for a non-empty GitHub repository or organisation, when the tool generates a JSON file of the contributor data, the system must download this file into my device and allow me to access it within 5 seconds.
- 
  - Given that the tool successfully generates and downloads the JSON file containing the contribution rankings into my device, when I view this report, the file must contain a complete and accurate conversion of all the contributor rankings into a JSON-format.
  
  - Given that I have downloaded a JSON file containing the accurately converted contribution rankings into my device, when I view this report, the file must also include the pre-defined metrics used to calculate the rankings in a clearly identifiable and logical manner for integration with other internal analytics tools.
  
  - Given that there exists a repository where API rate limit has exceeded, when I request contributor data for that repository, the system must notify me with an appropriate message (e.g. "Cannot access repository due to an exceed in rate limit") and allow me to enter a different repository name.
  
  - Given that there exists a private organisation that I am not authorised to access, when I request contributor data, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different organisation name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")
- 
 -  Given that there exists a repository or organisation with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributions found) and allow me to enter a different repository/organisation name

 -  Given that a repository or organisation has multiple contributors with the exact same number of commits, when I request contributor rankings to be exported in JSON format, the generated file must ensure all equally active contributors are ranked equally.