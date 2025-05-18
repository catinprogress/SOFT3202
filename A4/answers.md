# Software Engineering A4 - Answer Sheet

## Multiple-Choice Questions (20 points)

| Question | Answer |
|----------|--------|
| 1        | D      |
| 2        | A      |
| 3        | C      |
| 4        | B      |
| 5        | A      |
| 6        | A      |
| 7        | D      |
| 8        | C      |
| 9        | D      |
| 10       | B      |
| 11       | B      |
| 12       | A      |
| 13       | A      |
| 14       | D      |
| 15       | A      |
| 16       | A      |
| 17       | D      |
| 18       | D      |
| 19       | B      |
| 20       | B      |

## Question 21. Design patterns (10 marks)

### a. Identify the design pattern. An advantage and disadvantage. (5 marks)
Answer: Interpeter
    Expression: Abstract Expression
    Number/Variable: Terminal Expression
    Multiply: Non-terminal Expression
    context variable: Context
    expr variable: Clien

- Advantage: Gives user the ability to represent textual inputs (e.g. config files) and evaluate expressions with a defined grammar.
- Disadvantage: Inefficient for complex grammars or complicated and deeply nested/recursive expressions

### b. Adding addition operation (5 marks)
Answer: 
To support an addition operation, a new Non-Terminal Expression class called Addition would be created to represent expressions that contain a "+" symbol. This class would have similar implementation as the Multiply class, but it would return the sum of its left and right Expression nodes by replacing the "*" symbol in the return value with "+". No other changes would be required to the already existing classes and methods.


## Question 22. Decision tables (5 marks)

| Conditions                            | R1  | R2  | R3  | R4  | 
|---------------------------------------|-----|-----|-----|-----|
| length * width * height < 1000        | -   | T   |  F  |  F  |
| 1000 <= length * width * height < 5000| -   | F   |  T  |  F  |
| length * width * height >= 5000       | -   | F   |  F  |  T  |
| max(length, width, height) > 500      | T   | F   |  F  |  F  |
|     *Outputs*                         |     |     |     |     |
| Small Package                         |     |  T  |     |     |
| Medium Package                        |     |     |  T  |     |
| Large Package                         |     |     |     |  T  |
| Oversized                             | T   |     |     |     |

## Question 23. Whitebox testing techniques (20 marks)

### a. Statement coverage (4 marks)
```
Lines: 1,2,3,4,5,6,11,12,13,14,15
```

### b. Branch coverage (5 marks)

| Line | Condition                            | True Taken? (Yes/No) | False Taken? (Yes/No) |
|------|------------------------------------- |----------------------|-----------------------|
| 4    | for score in scores                  |     Yes              |    Yes                |
| 5    | if score >= 90                       |     Yes              |    No                 |
| 7    | if score >= 80                       |     No               |    No                 |
| 11   | if grade == 'A' or grade == 'B'      |     Yes              |    No                 |
| 14   | if total > 0 or passed/total >= 0.6  |     Yes              |    No                 |

### c. Test suite for maximum statement coverage (5 marks)

| Test input | Statements covered                         |
|------------|--------------------------------------------|
| [0]        | 1, 2, 3, 4, 5, 7, 10, 11, 13, 14, 15       |
| [90, 80]   | 1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15 |


### d. Bug detection limitation. Which criterion would be more effective. (6 marks)
Branch coverage would not be sufficient to reveal the bug in the code as it only guarantees that each branch outcome is executed, however the bug is a logical/dependency error between the predicates within the line 14 branch. Since the second predicate outcome is logically subsumed by the first predicate but an "or" relation is used instead of "and", this means that the branch is always True unless the 'scores' input is an empty list, in which case a ZeroDivisionError would occur.

To detect this bug, a more effective coverage criteria would be Predicate coverage, as this tests the logical combinations between conditions, thus ensuring that the 'passed/total >= 0' decision results in False at least once, which is required to show that the function returns an incorrect result. An example test case that would reveal this logical error is 'assert analyze_scores[0, 0, 90] == "Majority failed"', as the function would still return 'Majority passed' due to the incorrect relational operator used. 

## Question 24. Fault-based testing (18 marks)

### a. Mutation operator for Mutant A (1 mark)
Answer: Relational operator replacement

### b. Mutation operator for Mutant B (1 mark)
Answer: Arithmetic operator replacement

### c. Mutation operator for Mutant C (1 mark)
Answer: Constant replacement

### d. Killing conditions (6 marks)

| Mutant |                  Killing condition/input description                         | Killed by the test case? (Yes/No) |
|--------|----------------------------------------------------------------------------- |------------------------------------|
| A      |  A list with at least two elements that is in either a strictly increasing   | No
|        |  or decreasing order                                                         |
| B      |  A list with at least two elements that is in strictly increasing order      | No                                 |
| C      |  A list with exactly two elements                                            | Yes                                |


### e. Test case to kill Mutant A (2 marks)
```python

assert is_increasing([1, 2]) is True

```

### f. Mutant subsumption (7 marks)

| Mutant |                     Killing condition/input description                                                    |
|--------|------------------------------------------------------------------------------------------------------------|
| D      | A list that has at least one element less than its predecessor and has no two consecutive elements equal   |
| E      | A list that has at least two elements and is in strictly increasing order                                  |
| F      | A list that has at least two elements and is not in strictly increasing order                              |

| Mutant x | Mutant y | Does x subsume y? (Yes/No) |
|----------|----------|----------------------------|
|    D     |    E     | No                         |
|    D     |    F     | Yes                        |
|    E     |    D     | No                         |
|    E     |    F     | No                         |
|    F     |    D     | No                         |
|    F     |    E     | No                         |


## Question 25. Contracts (7 marks)

### a. Postcondition as @ensure contract (2 marks)
```python
@ensure(lambda xs, result: len(result) <= len(xs) , "Return value length must be less than or equal to input length")
```

### b. Precondition violations (5 marks)

| Test case                          | Violates Precondition? (Yes/No) |
|------------------------------------|---------------------------------|
| remove_duplicates([2, 3, 4])       | No                              |
| remove_duplicates([2, "3", 4])     | Yes                             |
| remove_duplicates(["2", "3", "4"]) | No                              |
| remove_duplicates((2, 3, 4))       | No                              |
| remove_duplicates([2.0, 3, 4])     | Yes                             |
| remove_duplicates([None])          | No                              |


## Question 26 (5 marks) (ONLY FOR COMP9202 STUDENTS)

Answer: