| Conditions                     | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 |
|--------------------------------|----|----|----|----|----|----|----|----|----|
| c1: repository exists          | T  | T  | T  |  T |  T | T  | T  | T  | F  |
| c1: organization is public     | T  | T  | F  |  F |  F | T  | T  | F  | -  |
| c2: user is member of org      | T  | F  | T  |  F |  F | F  | T  | T  | -  |
| c3: repository is not empty    | T  | T  | T  |  T |  F | F  | F  | F  | -  |
|--------------------------------|----|----|----|----|----|----|----|----|----|
| Outcomes                       |    |    |    |    |    |    |    |    |    |
|--------------------------------|----|----|----|----|----|----|----|----|----|
| o1: return True                | T  | T  | T  |    |    |    |    |    |    | 
| o2: NotAccessibleException     |    |    |    | T  | T  |    |    |    | T  |
| o3: return False               |    |    |    |    |    | T  | T  | T  |    |




