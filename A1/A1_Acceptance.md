## (b) Filter Contribution Rankings by Time Periods
  - Given that I have entered a valid GitHub Repository name (i.e. URL) that is related to my product, when I request contributor rankings, the system must initially display a ranking of most active contributors over the project lifetime, along with the pre-defined metrics that the calculations were based on.
  
  - Given that I have requested contributor rankings, when the system displays the most active contributors over the project lifetime, the system must also provide option to filter the rankings by a specific time periods (e.g. last week, last month, last year) 

  - Given that I have requested contribution rankings and the tool supports time-based filtering, when I request a specific time period to filter results by, the system must display only the rankings that correspond to contributions made during the specified time period.

  - Given that there exists a time period in my project lifecycle in which no contributions were made to the selected repository, when I select that time period to filter contribution rankings by, the system must notify me with an appropriate message (e.g. "No contribution data exists for this period").

  -  Given that a repository or time period has multiple contributors with the exact same number of commits, when I request contributor rankings, the system must display all equally active contributors with the same ranking
  
  -  Given that there exists a repository with no contributions, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributor data exists for this repository") and allow me to enter a different repository name
- 
  -  Given that there exists a specific time period containing no contribution data, when I request contribution rankings to be filtered by that time period, the system must notify me with an appropriate message (e.g. "No contribution data exists for this time period") and allow me to choose a different time filter option. 
  - 
  -  Given that a repository where API rate limit has exceeded, when I request contributor rankings for that repository, the system must notify me with an appropriate message (e.g. "Cannot currently access contributor data for this repository due to an exceed in rate limit") and allow me to enter a different repository name.
- 
  - Given that there exists a private repository that I am not authorised to access, when I request contributor rankings, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different repository name.
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")
  

### (c) Show My Contribution Ranking over Different Time Periods
  
* Show My Contribution Ranking over Different Time Periods
  - Given that I have entered a repository name for a repository that I am a contributor of, when I request my personal contributor ranking, the system must display a personal dashboard of my contribution rankings for the life time and latest phase of the project, along with the metrics used to calculate this ranking (e.g. the impact of my commits, pull requests and code review) 
  
  - Given that I have entered a repository name for a repository that I am a contributor of, when I request my personal contributor ranking, the system must also provide an option to view my ranking over specific time periods (e.g. last week, last month, last year).
    
  - Given that I have specified a time period to view my contribution ranking in, when the system recalculates the contribution data, the system must display my personal ranking according to calculations made using only the contributions made to the repository during the specific time period.

  - Given that I have requested my contribution ranking for a specific time period, when the system displays my personal ranking, the system should also display the metrics used to measure and rank my contributions to my peers (e.g. number of my commits, pull requests and code reviews)
   
  - Given that there exists a repository or specific time period containing no contributions, when I request my personal ranking, the system must notify me with an appropriate message (e.g. "No contribution data exists for the specified time period") and allow me to request a different repository and/or time filter.
- 
  - Given that there exists a repository that I am a contributor of and have made no contributions to, when I request my personal ranking for that repository, the system must display my rank as last along with all other contributors who have made no contributions.
- 
  - Given that there exists a repository that I am not a contributor to, when I request my personal ranking for that repository, the system must notify me with appropriate message (e.g. "No contributor data for user exists for this repository") and allow me to enter a different repository name

  -  Given that there exists a repository or time period within a repository where I have the same number of commits to one or more contributor/s, when I request my personal contribution ranking, the system must display my rank as equal to all of the other equally active contributors. 

  -  Given that there exists a repository where API rate limit has exceeded, when I request my personal contributor ranking for that repository, the system must notify me with an appropriate message (e.g. "Cannot currently access contributor data for this repository due to an exceed in rate limit") and allow me to enter a different repository name.
  
  - Given that there exists a private repository that I am not authorised to access, when I request my personal contributor ranking, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different repository name.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")
  

  ### (d) Export Contributor Data in JSON format
* Export Contributor Data in JSON Format
  - Given that I have entered a Github repository or organization name with contributors, when I request contributor rankings, the tool must provide an option to export contributor data in JSON-format.
 
  - Given that I have selected the export option for a non-empty GitHub repository or organisation, when the tool generates a JSON file of the contributor data, the system must download this file into my device and allow me to access it within 5 seconds.

  - Given that the tool successfully generates and downloads the JSON file containing the contribution rankings into my device, when I view this report, the file must contain a complete and accurate conversion of all the contributor rankings into a JSON-format along with enough contributor data for it to be integrated with other internal analytics tools
  - - Given that the tool successfully generates and downloads the JSON file containing the contribution rankings into my device, when I view this report, the file must contain a complete and accurate conversion of all the contributor rankings into a JSON-format along with enough contributor data for it to be integrated with other internal analytics tools
- 
  - Given that the tool successfully generates and downloads the JSON file containing the accurately converted contribution rankings into my device, when I view this report, the file must include the pre-defined metrics used to calculate the rankings (e.g. number of commits, code reviews, pull requests) in a clearly identifiable and logical manner.

  -  Given that there exists a repository or organization where API rate limit has exceeded, when I request contributor data for that repository, the system must notify me with an appropriate message (e.g. "Cannot currently access contributor data for this repository due to an exceed in rate limit") and allow me to enter a different repository name.
  
  - Given that there exists a private organisation or repository that I am not authorised to access, when I request contributor data, the system must prevent access and notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") before allowing me to enter a different organisation name.
  
  - Given that there exists a private repository that I am not authorised to access within an organisation that I have access to, when I request contributor rankings, the system must produce a report using only the contributor data that I have been permitted to access.
  
  - Given that I have attempted to log into the tool using incorrect GitHub credentials, when the system authenticates my username and password, the system must prevent access and notify me with an appropriate message (e.g. "Authentication failed: invalid login credentials")
- 
 -  Given that there exists a repository or organisation with no contribution data, when I request contributor rankings, the system must notify me with an appropriate message (e.g. "No contributor data exists for this repository" (or organisation)) and allow me to enter a different repository/organisation name

 -  Given that a repository or organisation has multiple contributors with the exact same number of commits, when I request contributor rankings to be exported in JSON format, the generated file must ensure all equally active contributors are ranked equally