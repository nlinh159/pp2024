class Person:
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    def get_id(self):
        return self._person_id

    def get_name(self):
        return self._name

    def list_info(self):
        print(f"[{self._person_id}] {self._name}")

    def input_info(self):
        self._person_id = input("Enter ID: ")
        self._name = input("Enter name: ")


class Student(Person):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self._dob = dob
        self._marks = {}

    def get_dob(self):
        return self._dob

    def get_marks(self):
        return self._marks

    def add_mark(self, course_id, mark):
        self._marks[course_id] = mark

class Course(Person):
    def __init__(self, course_id, name):
        super().__init__(course_id, name)