# input functions
# input the number of student(s)
def student_number():
    return int(input("Number of students in class: "))

# input the student info
def student_info():
    print("\nInput student information")
    id = input("Input student ID: ")
    name = input("Input student name: ")
    dob = input("Input student Date of Birth (DoB): ")
    return {"id": id, "name": name, "dob": dob, "marks": {}}

# input number of course(s)
def course_number():
    return int(input("Number of courses: "))

# input course info
def course_info():
    print("\nInput course information")
    id = input("Input course ID: ")
    name = input("Input course name: ")
    return {"id": id, "name": name}

# inpur marks of the student in courses
def input_marks(s, c):
    
    # check course ID
    while True:
        c_id = input("Enter the course ID: ")
        if c_id not in c:
            print("There is no course with this ID!")
            continue
        else:
            break
        
    # check student ID   
    while True:
        s_id = input("Choose student to input marks. Enter the student ID: ")
        if s_id not in s:
            print("This ID is strange!")
            continue
        else:
            break
        
    # show result after input mark successfully, store value in the dictionary    
    mark = float(input(f"Enter marks of {s[s_id]['name']} in {c[c_id]['name']}: "))
    s[s_id]['marks'][c_id] = mark

# listing functions
# list of course
def list_courses(c):
    print("\nList of courses:")
    for c_id, c_info in c.items():
        print(f"[{c_id}] {c_info['name']}")

# list of students
def list_students(s):
    print("\nList of students:")
    for s_id, s_info in s.items():
        print(f"[{s_id}] {s_info['name']} ({s_info['dob']})")

# show mark of the student in a course
def show_marks(s, c):
    s_id = input("Enter the student ID: ")
    c_id = input("Enter the course ID: ")
    
    if s_id in s and c_id in c:
        if c_id in s[s_id]['marks']:
            print(f"\nMarks of {s[s_id]['name']} in {c[c_id]['name']}: {s[s_id]['marks'][c_id]}")
        else:
            print(f"No marks found for {s[s_id]['name']} in {c[c_id]['name']}.")
    elif s_id not in s:
        print("No student has this ID.")
    elif c_id not in c:
        print("No course has this ID.")       

# main fuction   
def main():
    print("Practical 1 - Student mark management")

    students = {}
    courses = {}
    
    # input number of students, information of each, show student list
    numStudents = student_number()
    for i in range(numStudents):
        infoStudent = student_info()
        students[infoStudent["id"]] = infoStudent    
    list_students(students)
    
    
    # input number of courses, information of each, show course list
    numCourses = course_number()
    for i in range(numCourses):
        infoCourse = course_info()
        courses[infoCourse["id"]] = infoCourse
    list_courses(courses)
    
    # choose to input mark or show mark of a student
    while True:
        print("\nWhat do you want to do?")
        print("1. Input marks for student in a course")
        print("2. Show student marks for a course")
        print("Exit: press any button")
        
        choice = input("\nEnter your choice: ")
        if choice == "1":
            input_marks(students, courses)
        elif choice == "2":
            show_marks(students, courses)
        else:
            print("Program executed succesfully. Thank you and have a nice day!")
            break

# call main function
if __name__ == "__main__":
    main()