class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        freq_students = {}
        res = len(students)
        freq_students = Counter(students)
        print(freq_students)
        for sandwich in sandwiches:
            if freq_students[sandwich] > 0 :
                freq_students[sandwich] -= 1
                res -= 1
            else:
                return res
        return res