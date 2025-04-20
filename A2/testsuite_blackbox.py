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

        # Answer:
        # Weak normal criteria: test all valid inputs at the boundary values of the input domains.

        # Test values: number_of_repos = x, number_of_commits = y
        # Nominal: 50, 500
        # Min: 1, 1
        # Min+ : 2, 2 
        # Max- : 99, 998
        # Max: 100, 999

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
        count_active_contributors(50, 999)
    
        

    def test_compute_rankings(self):
        # Question 2: write a test suite for `compute_ranking` using boundary value testing under the strong robust assumption
        # Refer to the docstring of the `compute_ranking` function, which can be found above.
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values.
    #    compute_ranking(1, 2)

        #Answer:
        #Strong robust criteria: test every combination of valid and invalid inputs at the boundary values of the input domains.
        #Test values: number_of_months = x, num_contributors = y
        # Nominal: 12, 51
        # Min: 1, 2
        # Min+ : 2, 3
        # Max- : 23, 99
        # Max: 24, 100

        # invalid min (min-): 0, 1
        # invalid max (max+): 25, 101

        #invalid x (min-), vary y
        compute_ranking(0, 1) 
        compute_ranking(0, 2)
        compute_ranking(0, 3)
        compute_ranking(0, 51)
        compute_ranking(0, 99)
        compute_ranking(0, 100)
        compute_ranking(0, 101)

        #x = 1, vary y
        compute_ranking(1, 1) #invalid (y = min-)
        compute_ranking(1, 2) 
        compute_ranking(1, 3)
        compute_ranking(1, 51)
        compute_ranking(1, 99) 
        compute_ranking(1, 100)
        compute_ranking(1, 101) #invalid (y = max+)
        
        #x = 2, vary y
        compute_ranking(2, 1)   #invalid (y = min-)
        compute_ranking(2, 2) 
        compute_ranking(2, 3)
        compute_ranking(2, 51)
        compute_ranking(2, 99)
        compute_ranking(2, 100)
        compute_ranking(2, 101) #invalid (y = max+)

        #x = nominal
        compute_ranking(12, 1) #invalid (y = min-)
        compute_ranking(12, 2)
        compute_ranking(12, 3)
        compute_ranking(12, 51) #nominal
        compute_ranking(12, 99)   
        compute_ranking(12, 100)
        compute_ranking(12, 101) #invalid (y = max+)

        #x = 23, vary y
        compute_ranking(23, 1) #invalid (y = min-)
        compute_ranking(23, 2)
        compute_ranking(23, 3)
        compute_ranking(23, 51)
        compute_ranking(23, 99)
        compute_ranking(23, 100)
        compute_ranking(23, 101) #invalid (y = max+)

        #x = 24, vary y
        compute_ranking(24, 1) #invalid (y = min-)
        compute_ranking(24, 2)
        compute_ranking(24, 3)
        compute_ranking(24, 51)
        compute_ranking(24, 99)
        compute_ranking(24, 100)
        compute_ranking(24, 101) #invalid (y = max+)

        #invalid x (max+), vary y
        compute_ranking(25, 1) 
        compute_ranking(25, 2)
        compute_ranking(25, 3)
        compute_ranking(25, 51)
        compute_ranking(25, 99)
        compute_ranking(25, 100)
        compute_ranking(25, 101)


    def test_score_contributors(self):
        # Question 3: write a test suite for `score_contributors` following 2-way testing. 
        # Refer to the docstring of the `score_contributors` function, which can be found above
        # In this assignment, we are less interested in the assertions, and more interested in the selection of input values.

        # Answer:
        # (allpairs module was used to calculate 2-way combinations --> each test case contains at most 3 distinct pairs)

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

        # scope x metric : T1 - T8
        # scope x time : T1 - T10
        # metric x time : T1 - T20
        # Total tests needed: 20 

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

        score_contributors(TimeGranularity.MONTH, Scope.ORGANIZATION, Metric.COMMITS) #15
        score_contributors(TimeGranularity.MONTH, Scope.ORGANIZATION, Metric.PULL_REQUESTS) #16
        
        score_contributors(TimeGranularity.WEEK, Scope.ORGANIZATION, Metric.PULL_REQUESTS) #17
        score_contributors(TimeGranularity.WEEK, Scope.ORGANIZATION, Metric.COMMITS) #18

        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.COMPOSITE) #19
        score_contributors(TimeGranularity.DAY, Scope.ORGANIZATION, Metric.ISSUES) #20


    def test_stats_available(self):
        # Question 4: For the function `are_stats_available`, write a decision table. 
        # Question 4a. Write out the table in markdown
        # Answer:
        # Note: the "-" in the table indicates collapsed values where the decision for that condition does not affect the outcome.

        # | Conditions                     | R1 | R2 | R3 | R4 | R5 | R6 |
        # |--------------------------------|----|----|----|----|----|----|
        # | c1: repository exists          | T  | T  |  T | T  | T  | F  |
        # | c1: organization is public     | T  | F  |  F | T  | F  | -  |
        # | c2: user is member of org      | -  | T  |  F | -  | T  | -  |
        # | c3: repository is not empty    | T  | T  |  - | F  | F  | -  |
        # |--------------------------------|----|----|----|----|----|----|
        # | Outcomes                       |    |    |    |    |    |    |
        # |--------------------------------|----|----|----|----|----|----|
        # | o1: return True                | T  | T  |    |    |    |    | 
        # | o2: NotAccessibleException     |    |    | T  |    |    | T  |
        # | o3: return False               |    |    |    | T  | T  |    |

	    # Question 4b. Then, write the test cases 
        # Note: in the test cases, give names to the repos/users to indicate if they are private, public, empty, etc.
        # If you notice any ambiguity, add a comment documenting your assumptions. 
        # After each test case, add a comment to indicate which column of the decision table
        # 
        # Assumption 1 (R6): Input validation for "repo_name" will occur before any other checks are performed, to check if the specified repository name is valid (i.e. exists). 
        #                    If a repository doesn't exist, the function will raise a NotAccessibleException.                   
        # Assumption 2 : Input validation for "user" names will only occur GIVEN that the function has already verified that the specified "repo_name" matches to an existing PRIVATE organization. 
        #               Thus it is assumed that the only "user" input validation that occurs is verifying whether the provided user is a member of a given PRIVATE organization; and the choice of "user" input is more trivial for public organizations.
        #               i.e. No "user" input validation will occur if the "repo_name" matches to an existing public organization, since they are accessible to anyone (e.g. "" is valid user input)     
        # Assumption 3 (R3): "private_org_non_member" refers to any string input value for "user" that is verified to not be a member of the specified private organization, causing the function to raise an exception; 
        #              thus this can refer to both existing and non-existing developer names  

        # Test cases:
        ### repo is accessible AND not empty ###
        are_stats_available("public_org/nonempty_repo1", "public_org_member") # True R1 (value of user is arbirtrary)
        are_stats_available("private_org/nonempty_repo1", "private_org_member") #True R2
        
        ### repo is NOT accessible ###
        are_stats_available("private_org/nonempty_repo1", "private_org_non_member")   #Exception R3

        ### repo is accessible AND empty ###
        are_stats_available("public_org/empty_repo1", "public_org_member") # False R4 (value of user is arbirtrary)
        are_stats_available("private_org/empty_repo1", "private_org_member") #False R5

        ### repo doesn't exist ###
        are_stats_available("invalid_repo", "some_string_input") #Exception R6   (value of user is arbirtrary) 
        
# for this assignment, you do not have to execute the test cases in this file
# as such, you will not be penalized for test cases that do not compile, as long as the intent of each test case is clear.
# You can also assume that all test cases written will be executed, regardless of whether a test case results in an exception to be thrown
# i.e., you don't have to catch or handle exceptions
# for this part of the assignment, assertions are optional
