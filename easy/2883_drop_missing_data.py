"""

2883. Drop Missing Data
Difficulty: Easy
Link: https://leetcode.com/problems/drop-missing-data/

PROBLEM:
DataFrame: students

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

There are some rows having missing values in the name column.

Write a solution to remove the rows with missing values.

The result format is in the following example.

Example:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 217        | None    | 19  |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+

Output:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 32         | Piper   | 5   |
| 779        | Georgia | 20  |
| 849        | Willow  | 14  |
+------------+---------+-----+

APPROACH:
Use dropna().

The subset parameter tells pandas to check missing values only
in the selected column.

students.dropna(subset=["name"]) removes rows where the name column is missing.

Time Complexity: O(n)
Space Complexity: O(result size)

"""

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:

    return students.dropna(subset=["name"])


# --- Tests ---
if __name__ == "__main__":
    students = pd.DataFrame({
        "student_id": [32, 217, 779, 849],
        "name": ["Piper", None, "Georgia", "Willow"],
        "age": [5, 19, 20, 14]
    })

    print(dropMissingData(students))
    #    student_id     name  age
    # 0          32    Piper    5
    # 2         779  Georgia   20
    # 3         849   Willow   14
