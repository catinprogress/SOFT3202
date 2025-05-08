from typing import List, Dict, Tuple, TypedDict, Optional
from collections import defaultdict

# A TypedDict type represents dictionary objects with a specific set of string keys, and with specific value types for each valid key
class GitHubRepo(TypedDict):
    name: str
    stars: int
    forks: int
    contributors: List[str]


# 1a. Fill in the ???, i.e., what's the return type of summarize_repos?
def summarize_repos(repos: List[GitHubRepo]) -> Dict[str, int]:
    total_stars: int = 0
    total_forks: int = 0
    total_contributors: int = 0
    unique_contributors: set[str] = set()

    for repo in repos:
        total_stars += repo["stars"]
        total_forks += repo["forks"]
        unique_contributors.update(repo["contributors"])

    total_contributors = len(unique_contributors)
    return {
        "total_repos": len(repos),
        "total_stars": total_stars,
        "total_forks": total_forks,
        "unique_contributors": total_contributors,
    }


# 1b. Fill in the two ???s
def top_contributors_by_avg_stars(
    repos: List[GitHubRepo],
    include_only: Optional[set[str]] = None
) -> List[Tuple[str, int, float]]:
    """
    Returns contributors and their average stars per repo,
    optionally filtering to a specified set of contributor names.

    Args:
        repos: A list of GitHubRepo entries.
        include_only: An optional set of contributor names to include.

    Returns:
        A list of (contributor_name, total_repos, average_stars) tuples,
        sorted by average_stars in descending order.
    """
    stars_by_contributor: Dict[str, List[int]] = {}

    for repo in repos:
        for contributor in repo["contributors"]:
            if include_only is not None and contributor not in include_only:
                continue
            if contributor not in stars_by_contributor:
                stars_by_contributor[contributor] = []
            stars_by_contributor[contributor].append(repo["stars"])

    result: List[Tuple[str, int, float]] = [
        (name, len(stars), sum(stars) / len(stars))
        for name, stars in stars_by_contributor.items()
    ]

    return sorted(result, key=lambda tup: tup[2], reverse=True)
    

import os
os.system('mypy function_types_questions.py')