import datetime
import unittest
from typing import Tuple, List, Dict, Union
from collections import defaultdict
import statistics

from enum import Enum

### Part 2 of the assignment ###
# Look for the triple question marks. They indicate the locations in this file where there are questions awaiting your answers.
# First, look for Question 1, then continue to Question 2, then Question 3.


class Metric(Enum):
    COMMITS = "commits"
    PULL_REQUESTS = "pull_requests"
    ISSUES = "issues"
    # note that in testsuite_whitebox.py, we removed the `composite` enum. This is deliberate.
    

def compute_composite_score(dev_metrics: Dict[str, Dict[Metric, float]], aggregate_by: str) -> Dict[str, float]:
    """
    Compute a composite score for each developer based on their metrics.
    
    Args:
        dev_metrics: Dictionary mapping developer IDs to their metrics.
            Format: {"dev_id": {Metric.COMMITS: value, Metric.ISSUES: value}}
        aggregate_by: Method to aggregate metrics. Options: "sum", "average", "weighted"
    """
    if len(dev_metrics) == 0:
        raise ValueError("expected a non-empty dev_metrics")
    composite_scores = {}
    
    for dev_id, metrics in dev_metrics.items():
        if aggregate_by == "sum":
            score = sum(metrics.values())
        
        elif aggregate_by == "average":
            if len(metrics) > 0:
                score = sum(metrics.values()) / len(metrics)
            else:
                score = 0
        
        elif aggregate_by == "weighted":
            weights = {
                Metric.COMMITS: 0.5,
                Metric.ISSUES: 0.3,
                Metric.PULL_REQUESTS: 0.2
            }
            
            score = 0.0
            for metric, value in metrics.items():
                if metric in weights:
                    score += value * weights[metric]
        
        else:
            # default to `sum`
            score = sum(metrics.keys())  # does this look right?
            
        composite_scores[dev_id] = score
    
    return composite_scores


from collections import defaultdict
from enum import Enum

# for this assignment, 
# the functions `count_contributions_by_metric`, `get_all_developers`, `get_all_repositories`, `fetch_commits`, `fetch_issues`, `fetch_prs`
# are dummy implementations that mock the real implementation of these functions. They return hardcoded values.
# When writing the test cases, pay attention to the values returned from these functions.
# You should construct test cases based on the return values of these functions.

def count_contributions_by_metric(developers, repos):
    """
    Counts the developers contributions across all repositories for specified metrics.
    
    Returns:
        dict: Dictionary with metric names as keys and counts as values.
            Example: {'commits': 15, 'issues': 3}
    """
    # this is merely a dummy implementation for ease of testing
    if len(repos) == 0:
      return {}
    contributions_by_developer = {}
    for dev in developers:
        contributions = defaultdict(int)
        contributions["commits"] = 15
        contributions["pull_requests"] = 4
        contributions["issues"] = 3

        
        contributions_by_developer[dev] = contributions
    
    return contributions_by_developer


def get_all_developers(org):
    # this is merely a dummy implementation for ease of testing
    if org == "ourorg":
      return ["Alice", "Bobby", "Charlie", "Doug", "Eliza"]
    elif org == "anotherorg":
      return ["Fabrice"]
    else:
      return []

def get_all_repositories(org):
    # this is merely a dummy implementation for ease of testing
    if org == "ourorg":
      return ["ourorg/repo1", "ourorg/repo2", "ourorg/repo3"]
    elif org == "anotherorg":
      return ["anotherorg/repo1"]
    else:
      return []


def fetch_commits(repo, developer):
    # this is merely a dummy implementation for ease of testing
    return 3

def fetch_issues(repo, developer):
    # this is merely a dummy implementation for ease of testing
    return 2

def fetch_prs(repo, developer):
    # this is merely a dummy implementation for ease of testing
    return 1


def count_contributions_by_repo(org, metrics, developer):
    """
    Counts the number of contributions made by a specific developer for each specified metric
    across all provided repositories.
    
    Args:
        org (str)
        metrics (list) 
        developer (str)
    
    Returns:
        dict: A dictionary mapping repository identifiers to metric counts for the specified developer.
    """
    # initialization     
    all_developers  = get_all_developers(org)     # note that for the assignment, 
    repos           = get_all_repositories(org)   # we do not have to cover the statements and branches in the functions called
    
    # check that developer belongs to the org
    if developer not in all_developers:
        raise ValueError(f"the provided developer {developer} is not in the org {org}")

    contributions_count = {}
    
    for repo in repos:
        contributions_count[repo] = {}
        
        if Metric.COMMITS in metrics:
            commits = fetch_commits(repo, developer)
            contributions_count[repo]['commits'] = commits

        if Metric.ISSUES in metrics:
            issues = fetch_issues(repo, developer)
            contributions_count[repo] = {'issues' : issues} # weird: does this look like a bug?
         
    return contributions_count


def count_active_contributors(org, minimum_value_for_metrics):
    """
    Counts the number of contributors who have either more commits more than the specified number of repositories
    
    Args:
        metric : 
        minimum_value_for_metrics: python dictionary mapping from a string key to an integer
    
    Returns:
        int: The count of active contributors who either exceeds the specified number of issues OR exceeds the specified number of commits.

    """
    ### ??? TODO: As part of Question 3b, fix the bug in this function after writing a test case for Question 3a

    # validate input parameters
    if any(metric not in ["commits", "pull_requests", "issues"] for metric in minimum_value_for_metrics.keys()):
        raise ValueError("Expected a valid metric: commits, pull_requests, or issues")


    for metric, minimum_val in minimum_value_for_metrics.items():
        if minimum_val < 0 or minimum_val >= 10_000:
            raise ValueError("unlikely values for the metrics")
    
    all_developers  = get_all_developers(org)
    repos           = get_all_repositories(org)
    
    # initialization 
    is_developer_active = False
    active_count        = 0
    
    contributions = count_contributions_by_metric(all_developers, repos)

    for developer, dev_contributions in contributions.items():

        if dev_contributions['commits'] > minimum_value_for_metrics['commits']:
            is_developer_active = True
            print(f"{developer} commits: {dev_contributions['commits']}")
        elif dev_contributions['pull_requests'] > minimum_value_for_metrics['pull_requests']:
            is_developer_active = True
        elif dev_contributions['issues'] > minimum_value_for_metrics['issues']:
            is_developer_active = True          
        else:
            # developer is not active
            is_developer_active = False

        if is_developer_active:
            active_count += 1

    return active_count


class TestScoreContributors(unittest.TestCase):
    def test_composite_score(self):
        # Question 1:
        # Inspect the following test case for compute_composite_score
        with self.assertRaises(ValueError):
            compute_composite_score({}, "sum")

        # Sample developer metrics
        dev_metrics1 = {
            "dev1": {Metric.COMMITS: 10, Metric.ISSUES: 5},
            "dev2": {Metric.COMMITS: 7, Metric.ISSUES: 12},
            "dev3": {Metric.COMMITS: 15, Metric.ISSUES: 3},
            "dev4": {} 
        }

        expected = {
            "dev1": 15.0,
            "dev2": 19.0,
            "dev3": 18.0,
            "dev4": 0.0
        }
        result = compute_composite_score(dev_metrics1, "sum")
        self.assertEqual(result, expected)
        # Please write your answer to the following question as code comments prefixed with Answer:.
        # Question 1a: What is the statement coverage achieved by `test_composite_score` in testing `compute_composite_score`?  
        # 42%
        #       
        # Are these tests adequate (is there a bug that results in a TypeError missed by the test suite)? 
        # Which coverage criteria would be useful for writing a test case allowing a developer to observe the bug?
        #
        # Answer: 
        # Statement coverage = 42%, branch coverage = 1/6 = 16.67%
        # The tests are not adequate, as they do not cover all branches (conditions) in the function.
        # The test suite misses the bug in the else block: score = sum(metrics.keys()), where the .keys() method should be replaced with .values() in order to correctly extract the numeric metric values that need to be summed.
        # A more useful coverage criteria to reveal this bug would be 100% branch coverage, in order to test all possible decision outcomes of the function.
        # Note that because all non-nested branches are predicate conditions that check the value of the same string literal, branch coverage is sufficient to reveal the bug that occurs in the default case.

        # Question 1b: Complete the test test suite to achieve 100% coverage
        # For this assignment, you do not have to fix the bug in `compute_composite_score`
        # When you write a test case that reveals the buggy behavior, ignore the exception
        # by using a try-except, or using self.assertRaises

        #Answer
        result1 = compute_composite_score(dev_metrics1, "sum")
        self.assertEqual(result1, expected)
        
        result2 = compute_composite_score(dev_metrics1, "average")
        expected2 = {
            "dev1": statistics.mean([10, 5]),
            "dev2": statistics.mean([7, 12]),
            "dev3": statistics.mean([15, 3]),
            "dev4": 0.0  # empty list, should return 0.0
        }
        self.assertEqual(result2, expected2)

        result3 = compute_composite_score(dev_metrics1, "weighted")
        expected3 = {
            "dev1": 10*0.5 + 5*0.3,
            "dev2": 7*0.5 + 12*0.3,
            "dev3": 15*0.5 + 3*0.3,
            "dev4": 0.0  
        }
        self.assertEqual(result3, expected3)    

        with self.assertRaises(TypeError):
            compute_composite_score(dev_metrics1, "unknown")


    def test_count_contributions_by_repos(self):
        # Question 2:
        # Look at the following test suite for count_contributions_by_repos
        count_contributions_by_repo("ourorg", [], "Alice")
        with self.assertRaises(ValueError): #developer not in org
            count_contributions_by_repo("emptyorg", [Metric.COMMITS, Metric.ISSUES], "Alice")
   
        with self.assertRaises(ValueError): 
            count_contributions_by_repo("emptyorg", [Metric.COMMITS, Metric.ISSUES], None)
            

        actual = count_contributions_by_repo("ourorg", [Metric.COMMITS], "Alice") #commits in metrics true, issues in metrics false
        self.assertEqual(actual['ourorg/repo1']['commits'], 3)
        self.assertEqual(actual['ourorg/repo2']['commits'], 3)
        self.assertEqual(actual['ourorg/repo3']['commits'], 3)

        actual = count_contributions_by_repo("ourorg", [Metric.ISSUES], "Alice") #commits in metrics false, issues in metrics true
        self.assertEqual(actual['ourorg/repo1']['issues'], 2)
        self.assertEqual(actual['ourorg/repo2']['issues'], 2)
        self.assertEqual(actual['ourorg/repo3']['issues'], 2)

        # Please write your answer to the following question as code comments prefixed with Answer:.
	    # Question 2a: What is the statement and branch coverage achieved by `test_count_contributions_by_repos` on `count_contributions_by_repos`?
        #  Note: ignore the coverage of the functions called by `count_contributions_by_repos`. We care only about the coverage of `count_contributions_by_repos`
        # 
        #   Are these tests adequate (Is there a bug that results in incorrect return values)? 
        #   Which additional coverage criteria would be useful for writing a test case allowing a developer to observe the bug?
        # Answer: 
        # Statement coverage = 100% , branch coverage = 100%
        # This test case is not adequate as it does not reveal the bug contributions_count[repo] = {'issues' : issues}, which would overwrite any existing commit counts that are calculated in the previous decision block.
        # It does not cover the case where the user has both COMMITS and ISSUES in metrics, as each branch outcome is tested independently from another. 
        # A more useful coverage criteria to reveal this bug would be 100% Intraprocedural Acyclic Path coverage, as this would ensure the interactions of different combinations of branch outcomes are tested.

        # Question 2b:
        # Your task is to complete the test suite
        # For this assignment, you do not have to fix the bug in `count_contributions_by_repos`
        # When you write a test case that reveals the buggy behavior, ignore the exception
        # by using a try-except, or using self.assertRaises
   

      ##  Answer:
        #Paths to cover = 5
        #Path 1: raise Value Error
        with self.assertRaises(ValueError): #developer not in org
            count_contributions_by_repo("emptyorg", [Metric.COMMITS, Metric.ISSUES], "Alice")

        #Path 2: COMMITS false, ISSUES false
        path2 = count_contributions_by_repo("ourorg", [], "Alice") #commits in metrics true, issues in metrics false
        self.assertEqual(path2['ourorg/repo1'], {})
        self.assertEqual(path2['ourorg/repo2'], {})
        self.assertEqual(path2['ourorg/repo3'], {})

        #Path 3: COMMITS true, ISSUES false
        path3 = count_contributions_by_repo("ourorg", [Metric.COMMITS], "Alice")
        self.assertEqual(path3['ourorg/repo1']['commits'], 3)
        self.assertEqual(path3['ourorg/repo2']['commits'], 3)
        self.assertEqual(path3['ourorg/repo3']['commits'], 3)

        #Path 4: COMMITS false, ISSUES true
        path4 = count_contributions_by_repo("ourorg", [Metric.ISSUES], "Alice") #commits in metrics false, issues in metrics true
        self.assertEqual(path4['ourorg/repo1']['issues'], 2)
        self.assertEqual(path4['ourorg/repo2']['issues'], 2)
        self.assertEqual(path4['ourorg/repo3']['issues'], 2)

        #Path 5: COMMITS true, ISSUES true -> reveal bug (KeyError)
        path5 = count_contributions_by_repo("ourorg", [Metric.COMMITS, Metric.ISSUES], "Alice")
        self.assertEqual(path5['ourorg/repo1']['issues'], 2)
        self.assertEqual(path5['ourorg/repo2']['issues'], 2)
        self.assertEqual(path5['ourorg/repo3']['issues'], 2)

        with self.assertRaises(KeyError):
            self.assertNotEqual(path5['ourorg/repo1']['commits'], 3)

        with self.assertRaises(KeyError):
            self.assertNotEqual(path5['ourorg/repo2']['commits'], 3)

        with self.assertRaises(KeyError):
            self.assertNotEqual(path5['ourorg/repo2']['commits'], 3)
          
        
    def test_bug1_in_count_active_contributors(self):
        # Question 3:
        # You have received the following bug report:
        #
        #                             Issue #1
        #                               Title: 
        # count_active_contributors does not return the right number of active contributors
        #
        #                            Description:
        # The tool seems to be undercounting the number of active contributors. 
        # In particular, it seems to be ignoring contributors who have a high number of commits 
        # but do not post any issues on the issue tracker.
        # 
        # ======================================================================================
        #
        # In this assignment, your task is write a test case that reveals the bug:
        # here are the existing test cases
        # self.assertEqual(count_active_contributors("ourorg", {"commits": 1, "pull_requests": 1, "issues":1}), 5)
        # self.assertEqual(count_active_contributors("ourorg", {"commits": 50, "pull_requests": 50, "issues":50}), 0)

        # Question 3a
        # Answer:

        #All developers have at least 10 commits and 1 issue, so they are all active contributors
        self.assertEqual(count_active_contributors("ourorg", {"commits": 10, "pull_requests": 1, "issues":1}), 5)
        
        #Reveal the bug: since all developers have at least 10 commits, then the result should be still be 5, i.e. equal to the previous testcase.
        self.assertEqual(count_active_contributors("ourorg", {"commits": 10, "pull_requests": 1, "issues":50}), count_active_contributors("ourorg", {"commits": 10, "pull_requests": 1, "issues":1}), "Expected 5, but got a different number of active contributors")

        # Question 3b: fix the bug in count_active_contributors
        # Answer: by changing the separate if statements for each branch into one if/elif/else block, this ensures that the method returns the correct count value,
        # as it removes the hidden dependency/logic error between the first and last condition branches in the original code, which could lead to some contributors being missed in the final calculation.
        # This change means that a developer only needs to fulfil one of conditions (as specified in the documented requirements) in order to be considered as an active contributor.

        # After the test cases, please write the answer to the following question as code comments prefixed with "Answer:"
        # Question 3c: What is one coverage criteria that would have guaranteed that the buggy behavior was observed during testing
        # Answer: 
        # Intraprocedural Acyclic Path coverage would have guaranteed that the buggy behaviou was observed during testing as it 
        # requires the tester to test every single path that the function can take from start to end. 
        # This involves evaluating the interactions between different decision branches in the functions, which is important in this situation
        # as the bug is a logic error that depends on the interacting outcomes of 2 different branch conditions in the for loop.
        # That is, in order to reveal the bug, the tester must test the path where the developer has a high number of commits but no issues, which would require the first branch in the for loop to result to True, and the if/else branch to result to False.
        

if __name__ == '__main__':
    unittest.main()


# for this assignment, assertions are optional

