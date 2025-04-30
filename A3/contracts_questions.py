from icontract import require, ensure
from typing import Optional, List, Callable, Tuple

# There are 3 "??? TODOs" in total

@require(lambda name: isinstance(name, str) and name.strip(), "Name must be a non-empty string")
@require(lambda commits: commits >= 0, "Commits must be non-negative")
@require(lambda issues: issues >= 0, "Issues must be non-negative")
## Answer
@require(lambda pull_requests: pull_requests >= 0, "Pull requests must be non-negative")
#@require(lambda email: email is None or isinstance(email, str), "Email must be a string or None")
@require(
    lambda commits, pull_requests, issues: (commits + pull_requests + issues) > 0,
    "Contributor must have at least one activity (commits, PRs, or issues)"
)
class Contributor:
    def __init__(
        self,
        name: str,
        commits: int = 0,
        pull_requests: int = 0,
        issues: int = 0,
        email: Optional[str] = None
    ):
        self.name = name
        self.commits = commits
        self.pull_requests = pull_requests
        self.issues = issues
        self.email = email

    def total_activity(self) -> int:
        return self.commits + self.pull_requests + self.issues

    def __repr__(self):
        return (
            f"Contributor(name={self.name!r}, commits={self.commits}, "
            f"PRs={self.pull_requests}, issues={self.issues})"
        )


@require(lambda contributors: len(contributors) > 0, "Contributor list must not be empty")
@require(lambda contributors: all(c.total_activity() > 0 for c in contributors),
         "All contributors must have at least one recorded activity")
@ensure(lambda result: all(score >= 0 for _, score in result),
        "All computed impact scores must be non-negative")
def compute_all_impacts(
    contributors: List[Contributor],
    impact_fn: Callable[[Contributor], float]
) -> List[Tuple[str, float]]:
    return [(c.name, impact_fn(c)) for c in contributors]


@require(lambda threshold: threshold > 0, "Threshold must be positive")
@ensure(lambda result, threshold: all(score >= threshold for _ , score in result),
        "All returned contributors must have scores exceeding the threshold")
def core_contributors(
    contributors: List[Contributor],
    impact_fn: Callable[[Contributor], float],
    threshold: float = 10.0
) -> List[Tuple[str, float]]:
    impacts = compute_all_impacts(contributors, impact_fn)
    return [(name, score) for name, score in impacts if score >= threshold]


contributors = [
    Contributor("Alice", commits=10, pull_requests=5, issues=3),
    Contributor("Bob", commits=50, pull_requests=0, issues=1),
    Contributor("Charlie", commits=2, pull_requests=8, issues=6),
    Contributor("Dana", commits=0, pull_requests=1, issues=33),
   # Contributor("Eliza", commits=0, pull_requests=-1, issues=33),
]

def correct_impact(c):
    return 2 * c.pull_requests + 1.5 * c.issues + c.commits

def wrong_impact(c):
    # return negative value
    return -2 * c.pull_requests + 1.5 * c.issues + c.commits

contributors_impact = compute_all_impacts(contributors, correct_impact)
#contributors_impact = compute_all_impacts(contributors, wrong_impact)
for name, score in contributors_impact:
    print(f"{name}: {score:.1f}")

print("Core contributors:")
core_contributors_impact = core_contributors(contributors, correct_impact)
for name, score in core_contributors_impact:
    print(f"{name}: {score:.1f}")
