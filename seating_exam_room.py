import bisect
from math import floor

class ExamRoom:

    def __init__(self, N: int):
        self.capacity = N
        self.students = []

    def seat(self) -> int:

        if not self.students:  # No students

            bisect.insort(self.students, 0)
            return 0

        elif len(self.students) == 1:  # second student

            bisect.insort(self.students, self.capacity - 1)
            return self.capacity-1

        else:  # More than two students

            student, distance = 0, 0

            for i in range(1, len(self.students)):
                
                if self.students[0] != 0:
                    d = (self.students[0] - 0)

                    if d > distance:
                        distance = d
                        student = 0

                d = floor((self.students[i] - self.students[i-1])/2) # calculate the distance

                if d > distance: # when distance is going to be more, place the student
                    distance = d
                    student = self.students[i-1] + distance

                if i == len(self.students) - 1 and self.students[i] != self.capacity - 1:
                    d = floor((self.capacity - 1) - (self.students[i]))
                    if d > distance:
                        distance = d
                        student = self.capacity - 1
                    
            bisect.insort(self.students, student)
            return student


    def leave(self, p: int) -> None:
        if p in self.students:
            self.students.remove(p)


# [null,0,9,4,null,null,0,4,2,6,1,3,5,7,8,null]

ops = ["seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave"]

exam_room = ExamRoom(10)

for op in ops:
    if op is "seat":
        print(exam_room.seat())
    elif op is "leave":
        print(exam_room.leave(9))
