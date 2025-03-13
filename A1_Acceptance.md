* Filter Contribution Rankings by Time Periods
  - Given that I have entered a GitHub Repository name (i.e. URL) that I oversee
  - When I access said repository 
  - The system must clearly display an option on my interface for filterinng contribution rankings according to specific time periods (e.g. last week, last month, last year) 

  - Given that the tool displays an option to filter contirbution rankings
  - When I select the filtering option
  - Then the system should NOT display any invalid time periods (i.e. outside of the project lifetime) for me to choose from

  - Given that I have requested contribution rankings,
  - When I select a valid time period filter
  - The system must display only the rankings that correspond to the specified time period.

  - Given that there exists a time period in my project lifecycle in which no contributions were made to the selected repository
  - When I select that time period to filter contribution rankings by
  - The system must notify me with an appropriate message (e.g. "No contribution data exists for this period").

  - Given that I have entered a Github Repository name that I am not authorised to (e.g. unrelated to the contributors for my product)
  - When the tool authenticates my credentials
  - Then the system must notify me with an appropriate message (e.g. "Access denied: user is not authorised to access this repository") and not allow me to access this repository

//  - The system displays the filtered results within 5 seconds of the query being made and notifies users of any delay if time exceeds 5 seconds.
// - If a repository API rate limit is exceeded, the system must notify users that they cannot access this repository due to rate limit.
  
* Show My Contribution Ranking over Different Time Periods
  - Given that I have entered a repository name that I am a contributor to
  - When the tool successfully authenticates my GitHub credentials
  - The system must display a personal dashboard of my contribution rankings for the life time and latest phase of the project, along with the metrics used to calculate this ranking (e.g. the impact of my commits, pull requests and code review)

  - Given that the tool provides a filter option to show my contribution ranking over different time periods (e.g. last week, last month, last year)
  - When I enter a repository name that I am a contributor to
  - The system must not display any invalid time periods (i.e. outside of the project lifecyle) for me to select

  - Given that I have entered a repository name that I am a contributor to and the system displays valid time filter options
  - When I select a specific time period to filter my contribution ranking by
  - The system must recalculate my contribution data and display my personal contribution ranking within that specified time period.

  - Given that I have selected a specific time period to filter my contribution ranking by
  - When the system displays my contribution ranking for that specified time period
  - Then it should also clearly show the metrics used to measure and rank my contributions (e.g. my commits, pull requests and code reviews)

  - Given that I have requested my contribution ranking for a phase of the project with no contribution data
  - When the tool processes the contribution data for this time period
  - The system must notify me with an appropriate message (e.g. "No contribution data exists for this time period") and allow me to select a different time filter

  
* Export Contributor Data in JSON Format
  - Given that I have entered a Github repository or organization name with contributors
  - When I request contributor rankings
  - The tool must display contributor rankings along with an option to export contributor data as a JSON-formatted report.
 
  - Given that I have selected the export option,
  - When the tool generates the contribution ranking report in JSON format
  - The system must clearly display an option to download the report containing the contributor data, and the file must be saved into my system within 5 seconds of confirming download.

  - Given that I have confirmed the download of the JSON-formatted report
  - When the tool processes my request
  - Then the file must be saved and available for me to access on my device within 5 seconds of confirmation.
  
  - Given that I have entered a Github repository name with no contributor data
  - When I request to export contributor data
  - The system must display an approriate message (e.g. "Cannot proceed with export as no contributor data exists for this repository") and allow me to enter a different repository name.
  
  - Given that I request an export for a repository with contributor data
  - When there is an error in processing my request (e.g. rate limit exceeded for repository)
  - The system must notify me of the error that occurred with a clear and understandable explanation (e.g. "Cannot proceed with export for this repository due to exceed in rate limit") and prompt me to try again later or enter a different repository.

  - Given that I have successfully downloaded the JSON formatted report containing the contribution rankings,
  - When I view this report,
  - The file must contain a complete and JSON-formatted report that accurately includes all contribution rankings and enough contributor data for it to be used for integration with other internal security and analytics tools.
  
  - Given that the tool has fetched my requested contributor data from the GitHub API
  - When it converts the contribution rankings into JSON-format
  - The tool must generate an accurate conversion of all contribution rankings along with the pre-defined metrics used to calculate the rankings (e.g. number of commits, code reviews, pull requests) in a clearly identifiable and logical manner.
