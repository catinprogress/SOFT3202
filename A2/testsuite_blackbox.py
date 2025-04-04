import unittest
from typing import Tuple, List, Dict, Union
from enum import Enum

### Part 1 of the assignment ###
# Look for the triple question marks. They indicate the locations in this file where there are questions awaiting your answers.

def count_active_contributors(number_of_repos, number_of_commits):
    """
    Counts the number of contributors who have more than the specified number of repositories and commits.
    
    Args:
        number_of_repos (int): Minimum number of repositories a contributor must exceed to be counted.
                              Valid range: 1 <= number_of_repos <= 100
        number_of_commits (int): Minimum number of commits a contributor must exceed to be counted.
                                Valid range: 1 <= number_of_commits < 1000
    
    Returns:
        int: The count of contributors who exceed both the specified number of repositories and the specified number of commits.
    """
    pass


def compute_ranking(number_of_months, num_contributors):
   """
   Computes a ranking of contributors based on their commit activity.
   
   Args:
       number_of_months (int): The time range in months to consider when counting commits.
                              Valid range: 1 <= number_of_months <= 24
       num_contributors (int): The length of the contributor list to be returned.
                             Valid range: 2 <= num_contributors <= 100
   
   Returns:
       list: A list of length `num_contributors` of the top contributors, ordered by descending number of commits.
   
   """
   pass



class Scope(Enum):
    REPOSITORY = "repository"
    ORGANIZATION = "organization"

class Metric(Enum):
    COMMITS = "commits"
    PULL_REQUESTS = "pull_requests"
    ISSUES = "issues"
    COMPOSITE = "composite"

class TimeGranularity(Enum):
    DAY = "day"
    WEEK = "week"
    MONTH = "month"
    QUARTER = "quarter"
    YEAR = "year"


def score_contributors(time_granularity: TimeGranularity, scope: Scope, metric: Metric):
   """
   Scores contributors based on their activity in a given time period, scope, and metric.
   
   Args:
       time_granularity (TimeGranularity): The time period granularity for calculating scores.
                                          Options: DAY, WEEK, MONTH, QUARTER, YEAR
       scope (Scope): The scope level at which to aggregate contribution data.
                     Options: REPOSITORY, ORGANIZATION
       metric (Metric): The specific activity metric used for scoring.
                       Options: COMMITS, PULL_REQUESTS, ISSUES, COMPOSITE
   
   Returns:
       dict: A dictionary mapping contributor names or IDs to their calculated scores
             based on the specified parameters.
   
   Notes:
       - When using COMPOSITE metric, scores are calculated using the other metrics.
   """
   pass


def are_stats_available(repo_name:str, user:str):
    """
    For this assignment, we use a simplified model of GitHub.
    An organization is either public or private.
    Each repository belongs to one organization.
    Users can be a member of an organization.

    Statistics are available for a repository only if:
    * The repository is accessible to the user, which requires:
    The repository to belongs to a public organization, or
    The repository belongs to a private organization that the user is a member of.
    * The repository is not empty (contains some data).

    If the repository is both accessible and not empty, the code returns True. 
    If the repository is not accessible, the code will raise an NotAccessibleException.
    If the repository is accessible and empty, the code returns False.
    """
    pass



class TestScoreContributors(unittest.TestCase):
    def test_count_active_contributors(self):
        # Question 1: write a test suite for `count_active_contributors` using boundary value testing under the weak normal assumption.
        # Refer to the docstring of the `count_active_contributors` function, which can be found above.
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values
        # 
        # e.g., each test case should be a call to the function:
      #  count_active_contributors(1, 1)
        #Nominal: (50,500)
        #Min: 1, 1
        #Max: 100, 999

        #vary x, keep y nominal:
        count_active_contributors(1, 500)
        count_active_contributors(2, 500)
        count_active_contributors(99, 500)
        count_active_contributors(100, 500)

        #nominal
        count_active_contributors(50, 500)

        #vary y, keep x nominal:
        count_active_contributors(50, 1)
        count_active_contributors(50, 2)
        count_active_contributors(50, 998)
        count_active_contributors(50,999)
    
        

    def test_compute_rankings(self):
        # Question 2: write a test suite for `compute_ranking` using boundary value testing under the strong robust assumption
        # Refer to the docstring of the `compute_ranking` function, which can be found above.
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values.
    #    compute_ranking(1, 2)
        #Nominal: (12, 51)
        #Min: 1, 2
        #Max: 24, 100
        #invalid min: 0, 1
        #invalid max: 25, 100

        #invalid x, vary y
        compute_ranking(0, 1) 
        compute_ranking(0, 2)
        compute_ranking(0, 51)
        compute_ranking(0, 100)
        compute_ranking(0, 101)

        #x = 1, vary y
        compute_ranking(1, 1) #invalid
        compute_ranking(1, 2) 
        compute_ranking(1, 51)
        compute_ranking(1, 100)
        compute_ranking(1, 101) #invalid
        
        #x = nominal
        compute_ranking(12, 9) #invalid
        compute_ranking(12, 2)
        compute_ranking(12, 51) #nominal
        compute_ranking(12, 100)
        compute_ranking(12, 101) #invalid

        #x= 24, vary y
        compute_ranking(24, 1) #invalid
        compute_ranking(24, 2)
        compute_ranking(24, 51)
        compute_ranking(24, 100)
        compute_ranking(24, 101) #invalid

        #invalid x, vary y
        compute_ranking(25, 1) 
        compute_ranking(25, 2)
        compute_ranking(25, 51)
        compute_ranking(25, 100)
        compute_ranking(25, 101)


    def test_score_contributors(self):
        # Question 3: write a test suite for `score_contributors` following 2-way testing. 
        # Refer to the docstring of the `score_contributors` function, which can be found above
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values.

        # Test 1: Scope=repository, Metric =commits, TimeGranularity=day          
        # Test 2: Scope=organization, Metric =pull_requests, TimeGranularity=day  

        # Test 3: Scope=organization, Metric =issues, TimeGranularity=week       
        # Test 4: Scope=repository, Metric =composite, TimeGranularity=week

        # Test 5: Scope=repository, Metric =issues, TimeGranularity=month
        # Test 6: Scope=organization, Metric =composite, TimeGranularity=month

        # Test 7: Scope=organization, Metric =commits, TimeGranularity=quarter
        # Test 8: Scope=repository, Metric =pull_requests, TimeGranularity=quarter

        # Test 9: Scope=repository, Metric =pull_requests, TimeGranularity=year
        # Test 10: Scope=organization, Metric =commits, TimeGranularity=year

        # Test 11: Scope=organization, Metric =composite, TimeGranularity=year
        # Test 12: Scope=organization, Metric =issues, TimeGranularity=year

        # Test 13: Scope=organization, Metric =issues, TimeGranularity=quarter
        # Test 14: Scope=organization, Metric =composite, TimeGranularity=quarter

        # Test 15: Scope=organization, Metric =commits, TimeGranularity=month
        # Test 16: Scope=organization, Metric =pull_requests, TimeGranularity=month

        # Test 17: Scope=organization, Metric =pull_requests, TimeGranularity=week
        # Test 18: Scope=organization, Metric =commits, TimeGranularity=week

        # Test 19: Scope=organization, Metric =composite, TimeGranularity=day
        # Test 20: Scope=organization, Metric =issues, TimeGranularity=day

        #scope - metric : T1 - T8
        #scope - time : T1 - T10
        #metric -time : T1 - T20
        # Total needed: 20

        score_contributors(TimeGranularity.DAY, Scope.REPOSITORY, Metric.COMMITS) #1
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.PULL_REQUESTS) #2

        score_contributors(TimeGranularity.WEEK, Scope.ORGANIZATION, Metric.ISSUES) #3
        score_contributors(TimeGranularity.WEEK, Scope.REPOSITORY, Metric.COMPOSITE) #4

        score_contributors(TimeGranularity.MONTH, Scope.REPOSITORY, Metric.ISSUES) #5
        score_contributors(TimeGranularity.MONTH, Scope.ORGANIZATION, Metric.COMPOSITE) #6

        score_contributors(TimeGranularity.QUARTER, Scope.ORGANIZATION, Metric.COMMITS) #7
        score_contributors(TimeGranularity.QUARTER, Scope.REPOSITORY, Metric.PULL_REQUESTS) #8

        score_contributors(TimeGranularity.YEAR, Scope.REPOSITORY, Metric.PULL_REQUESTS) #9
        score_contributors(TimeGranularity.YEAR, Scope.ORGANIZATION, Metric.COMMITS) #10
        
        score_contributors(TimeGranularity.YEAR, Scope.ORGANIZATION, Metric.COMPOSITE) #11
        score_contributors(TimeGranularity.YEAR, Scope.ORGANIZATION, Metric.ISSUES) #12

        score_contributors(TimeGranularity.QUARTER, Scope.ORGANIZATION, Metric.ISSUES) #13
        score_contributors(TimeGranularity.QUARTER, Scope.ORGANIZATION, Metric.COMPOSITE) #14

        score_contributors(TimeGranularity.MONTH, Scope.ORGANIZATION, Metric.PULL_REQUESTS) #15
        score_contributors(TimeGranularity.MONTH, Scope.ORGANIZATION, Metric.COMMITS) #16

        score_contributors(TimeGranularity.WEEK, Scope.ORGANIZATION, Metric.PULL_REQUESTS) #17
        score_contributors(TimeGranularity.WEEK, Scope.ORGANIZATION, Metric.COMMITS) #18

        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.COMPOSITE) #19
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.ISSUES) #20


    def test_stats_available(self):
        # Question 4: For the function `are_stats_available`, write a decision table. 
        # Question 4a. Write out the table in markdown
        #  ??? TODO
        # | Conditions                     | R1 | R2 | R3 | R4 | 
        # |--------------------------------|----|----|----|----|
        # | repo is empty                  | F  | F  | F  |  T | #ASSUME THAT FUNCTION WILL ALWAYS RETURN FALSE FOR EMPTY REPO R4
        # | repo is public                 | T  | F  | F  |  - | 
        # | user is member                 | -  | F  | T  |  - |

        # | accessible repository          | T  | F  | T  |  - |
        # | NotAccessibleException         | F  | T  | F  | F  |
        # | stats available                | T  | F  | F  |  F |
	
	    # Question 4b. Then, write the test cases 
        # Note: in the test cases, give names to the repos/users to indicate if they are private, public, empty, etc.
        # If you notice any ambiguity, add a comment documenting your assumptions. 
        # After each test case, add a comment to indicate which column of the decision table
        # Example: 
        are_stats_available("public_org/nonempty_repo1", "public_org_developer") # R1
        # ??? TODO 

# for this assignment, you do not have to execute the test cases in this file
# as such, you will not be penalized for test cases that do not compile, as long as the intent of each test case is clear.
# You can also assume that all test cases written will be executed, regardless of whether a test case results in an exception to be thrown
# i.e., you don't have to catch or handle exceptions
# for this part of the assignment, assertions are optional
