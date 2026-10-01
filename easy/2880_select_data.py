"""

2880. Select Data
Difficulty: Easy
Link: https://leetcode.com/problems/select-data/

PROBLEM:
DataFrame: students

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.

Example:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+

Output:
+---------+-----+
| name    | age |
+---------+-----+
| Ulysses | 13  |
+---------+-----+

APPROACH:
Use boolean indexing with .loc[].

We need:
1. Select rows where student_id equals 101.
2. Select only the columns name and age.

students["student_id"] == 101 creates a boolean mask.
.loc[mask, ["name", "age"]] returns the matching rows and selected columns.

Time Complexity: O(n)
Space Complexity: O(result size)

"""

import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:

    return students.loc[
        students["student_id"] == 101,
        ["name", "age"]
    ]


# --- Tests ---
if __name__ == "__main__":
    students = pd.DataFrame({
        "student_id": [101, 53, 128, 3],
        "name": ["Ulysses", "William", "Henry", "Henry"],
        "age": [13, 10, 6, 11]
    })

    print(selectData(students))
    #       name  age
    # 0  Ulysses   13
