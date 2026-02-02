class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show_details(self):
        print(f"Student name {self.name} and id is {self.id}")

class Course:
    def __init__(self,course_id,course_name):
        self.course_id=course_id
        self.course_name=course_name
    def show_course(self):
        print(f"course id is {self.course_id} and name is { self.course_name}")

class Result:
    def __init__(self,student,course,marks):
        self.student=student
        self.course=course
        self.marks=marks
    def grade(self):
        if self.marks>=90:
           return "A"
        elif self.marks>=80:
            return "A-"
        elif self.marks>=70:
           return "B+"
        elif self.marks>=60:
            return "B"
        elif self.marks>=50:
           return "C"
        else:
            return "F"

    def show_result(self):
        self.student.show_details()
        self.course.show_course()
        print(f"Marks: {self.marks}")
        print(f"Grade:{self.grade()}")
        print("-" * 30)

# NOW CHWCK THE RESULTS
s1=Student("Ali",1)
s2=Student("Saim",2)

c1=Course("MA101","Calculus")
c2=Course('PF101','Programming')

r1=Result(s1,c1,98)
r2=Result(s2,c2,70)

r1.show_result()
r2.show_result()

           

    

    