class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        preferences = {0:0, 1:0}
        for student in students:
            preferences[student] += 1
        for sandwich in sandwiches:
            if preferences[sandwich] == 0:
                return preferences[0] + preferences[1]
            preferences[sandwich] -= 1
        return 0