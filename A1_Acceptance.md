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