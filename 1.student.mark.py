students = []
courses = []

def input_student_info():
    num_students = int(input("Please input the number of students: "))
    
    for _ in range(num_students):
        student = {}
        student['id'] = input("Input student ID: ")
        student['name'] = input("Input student name: ")
        student['dob'] = input("Input student date of birth: ")
        student['courses'] = []
        
        num_courses = int(input("Enter the number of courses for this student: "))
        for _ in range(num_courses):
            course = {}
            course['id'] = input("Input course ID: ")
            course['name'] = input("Input course name: ")
            student['courses'].append(course)
        
        students.append(student)

def input_student_marks():
    course_id = input("Input the course ID: ")
    for student in students:
        for course in student['courses']:
            if course['id'] == course_id:
                marks = float(input("Input mark for {}: ".format(student['name'])))
                course['marks'] = marks

def list_courses():
    print("Courses:")
    for course in courses:
        print("ID: {}, Name: {}".format(course['id'], course['name']))

def list_students():
    print("Students:")
    for student in students:
        print("ID: {}, Name: {}".format(student['id'], student['name']))

def show_student_marks():
    course_id = input("Enter the course ID: ")
    
    print("Student marks for course {}:".format(course_id))
    for student in students:
        for course in student['courses']:
            if course['id'] == course_id:
                print("Student: {}, Marks: {}".format(student['name'], course.get('marks', 'Not Available')))

while True:
    print("1. Input student information")
    print("2. Input student marks")
    print("3. List courses")
    print("4. List students")
    print("5. Show student marks for a course")
    print("0. Exit")
    
    choice = input("Enter your choice (0-5): ")
    
    if choice == '1':
        input_student_info()
    elif choice == '2':
        input_student_marks()
    elif choice == '3':
        list_courses()
    elif choice == '4':
        list_students()
    elif choice == '5':
        show_student_marks()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")