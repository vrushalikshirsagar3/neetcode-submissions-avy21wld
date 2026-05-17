class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_students = {}
        res = len(students)
        for student in students:
            freq_students[student] = 1 + freq_students.get(student, 0)
        for sandwich in sandwiches:
            if sandwich in freq_students.keys() and freq_students[sandwich] > 0 :
                freq_students[sandwich] -= 1
                res -= 1
            else:
                return res
        return res