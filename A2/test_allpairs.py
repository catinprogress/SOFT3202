from allpairspy import AllPairs

scope = ["repository", "organization"]
metric = ["commits", "pull_requests", "issues", "composite"]
timegranularity = ["day", "week", "month", "quarter", "year"]

# using allpairspy to generate 2-way (pairwise) test cases
pairwise_test_cases = list(AllPairs([scope, metric, timegranularity]))

for i, case in enumerate(pairwise_test_cases, start=1):
    print(f"Test {i}: Scope={case[0]}, Metric ={case[1]}, TimeGranularity={case[2]}")

print(f"\nTotal needed: {len(pairwise_test_cases)}")