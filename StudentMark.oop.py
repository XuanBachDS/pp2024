class Course:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    
    def getName(self):
        return self.__name
    
    def getID(self):
        return self.__id
    
    def Print(self):
        print(self.__id + '|' + self.__name)
    
class Student(Course):
    def __init__(self, name, id, dob):
        super().__init__(name, id)
        self.__DateofBirth = dob
        self.__PointDic = {}

    def getPoint(self):
        return self.__PointDic
    
    def getDob(self):
        return self.__DateofBirth
    
    def Print(self):
        print(self.getID() + '|' + self.getName() + '|' + self.getDob())
    
    def PointUpdate(self, CourseID, CoursePoint):
        self.__PointDic.update({CourseID : CoursePoint})
        
class Manager:
    def __init__(self):
        self.__StudentList = []
        self.__CourseList = []
    
    def init_Course(self, name, id ):
        C1 = Course(name,id)
        self.__CourseList.append(C1)
    
    def fix(self):
        for e in self.__StudentList:
            for x in self.__CourseList:
                e.PointUpdate(x.getName(), 0.0)
    
    def init_Student(self, name, id, DateOfBirth):
        S1 = Student(name, id, DateOfBirth)
        self.__StudentList.append(S1)
    
    def AddStudent(self):
        i = int(input('Enter Number of the Student: '))
        for x in range(i):
            self.init_Student(input('Name: '), input('ID: '), input('Date of Birth: '))
        self.fix()
    
    def AddCourse(self):
        i = int(input('Enter Number of the Course: '))
        for x in range(i):
            self.init_Course(input('Name: '), input('ID: '))
    
    def listCourse(self):
        for element in self.__CourseList:
            element.Print()
            
    def ListStudent(self):
        for element in self.__StudentList:
            element.Print()
    
    def UpdateScore(self):
        self.listCourse()
        str_input = input('Enter Course ID: ')
        
        for element in self.__CourseList:
            if element.getID() == str_input:
                for std in self.__StudentList:
                    f_input = input('Enter Mark for ' + std.getName() + ': ')
                    std.PointUpdate(element.getName(), f_input)
    
    def ListMark(self):
        for course in self.__CourseList:
            print(course.getName(), end="|")
        print()
        for student in self.__StudentList:
            temp = student.getPoint()
            for course in self.__CourseList:
                print(temp.get(course.getName(), 0.0), end="|")
            print()
                    
MasterManager = Manager()
MasterManager.AddCourse()
MasterManager.AddStudent()
MasterManager.UpdateScore()
MasterManager.ListMark()
