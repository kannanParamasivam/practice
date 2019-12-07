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
                    d = floor((self.students[0] - 0)/2)

                    if d > distance:
                        distance = d
                        student = self.students[i] + distance

                d = floor((self.students[i] - self.students[i-1])/2) # calculate the distance

                if d > distance: # when distance is going to be more, place the student
                    distance = d
                    student = self.students[i-1] + distance

                if i == len(self.students) - 1 and self.students[i] != self.capacity - 1:
                    d = floor((self.capacity - 1) - (self.students[i]) / 2)
                    if d > distance:
                        distance = d
                        student = self.students[i] + distance
                    
            bisect.insort(self.students, student)
            return student


    def leave(self, p: int) -> None:
        if p in self.students:
            self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:

# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.

ops = ["seat", "seat", "seat", "seat", "leave", "seat"]
exam_room = ExamRoom(10)

for op in ops:
    if op is "seat":
        print(exam_room.seat())
    elif op is "leave":
        print(exam_room.leave(4))
