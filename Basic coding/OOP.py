class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_student = max_students
        self.student_list=[]
    def add_student(self,student):
        if len(self.student_list) < self.max_student:
            self.student_list.append(student)
            return True
        return False
    def get_avarage_grade(self):
        value=0
        for s in self.student_list:
            value+= s.get_grade()
        return value/len(self.student_list)


s1 = Student("Tim",19 , 95)
s2 = Student("Bill",19,85)
s3 = Student("Dill",20,97)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)

print(course.get_avarage_grade())