from datetime import datetime
class Person:
    def __init__(self, person_id, name):
        self._person_id = person_id
        self._name = name

    def get_id(self):
        return self._person_id

    def get_name(self):
        return self._name
    
    def list_info(self, person_type):
        if person_type in ["student", "course"]:
            print(f"[{self._person_id}] {self._name}")

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

class MarkMana(Person):
    def __init__(self):
        self._people = {} 
    def add_something(self, person_type):
        print()
        # innitialize information of student and course
        id = input(f"Input {person_type} ID: ")
        name = input(f"Input {person_type} name: ")
        dob = None

        if person_type == "student":
            while True:
                dob = input(f"Input {person_type} DoB (mm-dd-yyyy): ")
                try:
                    dob = datetime.strptime(dob, "%m-%d-%Y")
                    break
                except ValueError:
                    print("Wrong date format! Please re-enter the DoB.")
        if person_type == "student":
            person = Student(id, name, dob)

        elif person_type == "course":
            person = Course(id, name)

        self._people[id] = person
        return person

    def list_things(self, person_type):
        print(f"\nList of {person_type}s:")
        for person_id, person in self._people.items():
            if isinstance(person, Student) and person_type == "student":
                person.list_info(person_type)
            elif isinstance(person, Course) and person_type == "course":
                person.list_info(person_type)
                
    def input_marks(self):
        while True:
            print()
            c_id = input("Enter the course ID: ")
            if c_id not in self._people or not isinstance(self._people[c_id], Course):
                print("There is no course with this ID!")
                continue
            else:
                break
        
        while True:
            s_id = input("Choose student to input marks. Enter the student ID: ")
            if s_id not in self._people or not isinstance(self._people[s_id], Student):
                print("This ID is strange! Please re-enter the student ID.")
                continue
            else:
                break
        while True:
            print()
            try:
                mark = float(input(f"Enter marks of {self._people[s_id].get_name()} in {self._people[c_id].get_name()}: "))
                break
            except ValueError:
                print("Mark must be a number! Please re-enter the mark.")
            
        self._people[s_id].add_mark(c_id, mark)
        
    def show_marks(self):
        print()
        s_id = input("Enter the student ID: ")
        if s_id not in self._people or not isinstance(self._people[s_id], Student):
            print("No student has this ID.")
        else:
            student = self._people[s_id]
            c_id = input("Enter the course ID: ")
            if c_id not in self._people or not isinstance(self._people[c_id], Course):
                print("No course has this ID.")
            else:   
                course = self._people[c_id]
    
                if c_id in student.get_marks():
                    print(f"\nMarks of {student.get_name()} in {course.get_name()}: {student.get_marks()[c_id]}")
                else:
                    print(f"No marks found for {student.get_name()} in {course.get_name()}")
            
    def run(self):
        print("Practical 2 - Student mark management OOP")

        num_students = int(input("Number of students in class: "))
        for i in range(num_students):
            student = self.add_something("student")
        self.list_things("student")

        print()
        num_courses = int(input("Number of courses: "))
        for i in range(num_courses):
            course = self.add_something("course")
        self.list_things("course")

        while True:
            print("\nWhat do you want to do?")
            print("1. Input marks for student in a course")
            print("2. Show student marks for a course")
            print("Exit: press any button")
            print()

            choice = input("Enter your choice: ")
            if choice == "1":
                self.input_marks()
            elif choice == "2":
                self.show_marks()
            else:
                print("Exited. Thank you and have a nice day!")
                break

mark_system = MarkMana()
mark_system.run()