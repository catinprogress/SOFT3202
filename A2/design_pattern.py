from typing import Dict, List, Tuple
from abc import ABC, abstractmethod
from enum import Enum

### Part 3 of the assignment ###
# Question 1: What is the design pattern implemented by the RankContributors and ScoringMethod class?
# Answer: ??? TODO

class Metric(Enum):
    COMMITS = "commits"
    PULL_REQUESTS = "pull_requests"
    ISSUES = "issues"
    # note that in design_pattern.py, we removed the `composite` enum. This is deliberate.
    


class ScoringMethod(ABC):
    @abstractmethod
    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        pass


class SumScoringMethod(ScoringMethod):
    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        return sum(metrics.values())


class AverageScoringMethod(ScoringMethod):
    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        if len(metrics) == 0:
            return 0.0
        return sum(metrics.values()) / len(metrics)


class WeightedScoringMethod(ScoringMethod):
    def __init__(self):
        self.weights = {
            Metric.COMMITS: 0.5,
            Metric.ISSUES: 0.3,
            Metric.PULL_REQUESTS: 0.2
        }

    def compute_score(self, metrics: Dict[Metric, float]) -> float:
        return sum(
            value * self.weights.get(metric, 0.0)
            for metric, value in metrics.items()
        )


class RankContributors:
    def __init__(self, scoring_method: ScoringMethod):
        self.scoring_method = scoring_method

    def rank(self, dev_metrics: Dict[str, Dict[Metric, float]]) -> List[Tuple[str, float]]:
        if not dev_metrics:
            raise ValueError("expected a non-empty dev_metrics")

        scored = [
            (dev_id, self.scoring_method.compute_score(metrics)) #for each dev, compute the score of their metric values by using a specific scoring algorithm/strategy
            for dev_id, metrics in dev_metrics.items() #items = the scores of each metric for a given developer
        ]

        return sorted(scored, key=lambda x: x[1], reverse=True) #sort in descending order by score (x[1])

        
dev_metrics = {
    "dev1": {Metric.COMMITS: 10, Metric.ISSUES: 5},
    "dev2": {Metric.COMMITS: 7, Metric.ISSUES: 12},
    "dev3": {Metric.COMMITS: 15, Metric.ISSUES: 3},
    "dev4": {}
}

ranker = RankContributors(SumScoringMethod())
print("Sum:", ranker.rank(dev_metrics))

##### Answer the question at the top of this file #####