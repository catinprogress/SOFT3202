import unittest
from typing import List, Dict, Tuple


# def rank_contributors(repos: List[Dict[str, List[str]]]) -> List[Tuple[str, int]]:
#     counts: Dict[str, int] = {} 
#     for repo in repos:
#         for contributor in repo.get("contributors", []): 
#             counts[contributor] = counts.get(contributor, 0) + 1 

#     return sorted(counts.items(), key=lambda item: -item[1]) 


class TestRankContributors(unittest.TestCase):
    def test_rank_contributors(self):
        repos = []
        expected = []
        assert rank_contributors(repos) == expected

        repos = [{"contributors": []}]
        expected = []
        assert rank_contributors(repos) == expected

        repos = [{"contributors": ["alice", "bob"]}] #
        expected = [('alice', 1), ('bob', 1)]
        assert rank_contributors(repos) == expected
        
		# ## Kill Mutant B, C and E
        # ## Note -> this test case is sufficient to kill mutants A and D as well
        repos = [{"contributors": ["alice", "bob"]}, {"contributors": ["alice"]}]
        expected = [('alice', 2), ('bob', 1)]
        assert rank_contributors(repos) == expected
        

# Question 2a: which of the following mutants would be killed by the above test suite
# list your answer as a comma-separated string, e.g. "A, B, C" to indicate that Mutants A, B, C are killed.
# You may find it helpful to comment the original function, and uncomment each mutant, then run the test suite
# Answer: A, D

		# Question 2b: complete the test suite `test_rank_contributors` to kill the remaining mutants. 
		# Answer: 
        # Mutant B killing condition: contributors with unequal number of contributions
        # Mutant C killing condition: list containing more than 1 repo to iterate through
        # Mutant E killing condition: at least 1 contributor has a count not equal to 1

# --- Mutants Definition ---
# Comment out the original function above and uncomment ONE mutant at a time to test


 # Mutant A:

# def rank_contributors(repos: List[Dict[str, List[str]]]) -> List[Tuple[str, int]]:
#     counts: Dict[str, int] = {}

#     for repo in repos:
#         for contributor in repo.get("contributors", []):
#             counts[contributor] = counts.get(contributor, 0) + 2  # MUTATION: changed "+ 1" to "+ 2"

#     return sorted(counts.items(), key=lambda item: -item[1])


# Mutant B:

# def rank_contributors(repos: List[Dict[str, List[str]]]) -> List[Tuple[str, int]]:
#     counts: Dict[str, int] = {}

#     for repo in repos:
#         for contributor in repo.get("contributors", []):
#             counts[contributor] = counts.get(contributor, 0) + 1

#     return sorted(counts.items(), key=lambda item: item[1])        # MUTATION: removed minus sign


# Mutant C

# def rank_contributors(repos: List[Dict[str, List[str]]]) -> List[Tuple[str, int]]:
#     counts: Dict[str, int] = {}

#     for repo in repos:
#         for contributor in repo.get("contributors", []):  
#             counts[contributor] = counts.get(contributor, 0) + 1  
#         break                                                        #  MUTATION: made the loop a one iteration loop: added a "break"

#     return sorted(counts.items(), key=lambda item: -item[1])


# Mutant D

# def rank_contributors(repos: List[Dict[str, List[str]]]) -> List[Tuple[str, int]]:
#     counts: Dict[str, int] = {}

#     for repo in repos:
#         for contributor in repo.get("alice", []):                     # MUTATION: replaced constant "contributors" with "alice"
#             counts[contributor] = counts.get(contributor, 0) + 1

#     return sorted(counts.items(), key=lambda item: -item[1])

# Mutant E

# def rank_contributors(repos: List[Dict[str, List[str]]]) -> List[Tuple[str, int]]:
#     counts: Dict[str, int] = {}

#     for repo in repos:
#         for contributor in repo.get("contributors", []):                     
#             counts[contributor] = 1                                    # MUTATION: deleted counts.get(contributor, 0)

#     return sorted(counts.items(), key=lambda item: -item[1])


# Question 2b: complete the test suite `test_rank_contributors` to kill the remaining mutants. Search for the ??? above

# --- Optional: Add if __name__ == '__main__': block for direct execution ---
# if __name__ == '__main__':
#      unittest.main()

# OR:
# 
# execute `unittest` in a terminal: python -m unittest mutation_questions.py
