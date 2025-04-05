| Conditions                     | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 |
|--------------------------------|----|----|----|----|----|----|----|----|
| c1: organization is public     | T  | T  | F  |  F |  F | T  | T  | F  |
| c2: user is private org member | T  | F  | T  |  F |  F | F  | T  | T  |
| c3: repository is not empty    | T  | T  | T  |  T |  F | F  | F  | F  |
|------------------------------------------------------------------------|
| Outcomes                       |    |    |    |    |    |    |    |    |
|--------------------------------|----|----|----|----|----|----|----|----|
| o1: return True                | T  | T  | T  |    |    |    |    |    |
| o2: NotAccessibleException     |    |    |    | T  | T  |    |    |    |
| o3: return False               |    |    |    |    |    | T  | T  | T  | 


Possible duplicates:
R4 and R5 -> error raised before repo empty check
R6 and R7 -> if organization is public, user being private org member is not checked
R1 and R2 -> same reasoning as above
