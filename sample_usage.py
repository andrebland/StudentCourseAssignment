from Course import Course
from Student import Student
from StudentCourseAssignment import StudentCourseAssignment

test = StudentCourseAssignment()
andre = Student("andre", 12)
beza = Student("beza", 12)
jane = Student("jane", 12)
john = Student("john", 12)
calc = Course("calc", 22901, 221201, {"day" : "M", "start" : 4, "end" : 5}, 4)
trig = Course("trig", 22901, 221201, {"day" : "M", "start" : 4, "end" : 5}, 4)
phys = Course("phys", 22901, 221201, {"day" : "W", "start" : 4, "end" : 5}, 4)


#create students and courses
print(test.createStudent(jane))
print(test.createStudent(john))
print(test.createStudent(andre))
print(test.createStudent(beza))
print(test.createCourse(calc))
print(test.createCourse(trig))
print(test.createCourse(phys))

#update functions
andre.name = "andre bland"
print(test.updateStudent(andre))
calc.name = "calc2"
print(test.updateCourse(calc))

#add students to course
print(test.addStudentToCourse(andre, calc))
print(test.addStudentToCourse(andre, phys))
print(test.addStudentToCourse(beza, calc))
print(test.addStudentToCourse(jane, calc))
print(test.addStudentToCourse(john, calc))

#set grades
print(test.setStudentGradeForCourse(andre, calc, 5))
print(test.setStudentGradeForCourse(andre, phys, 5))
print(test.setStudentGradeForCourse(beza, calc, 5))
print(test.setStudentGradeForCourse(jane, calc, 3))
print(test.setStudentGradeForCourse(john, calc, 2))

print("students taking calc2")
for student in test.getStudentsOfCourse(calc):
    print(student.name)

print("coureses andre is taking")
for course in test.getCoursesOfStudent(andre):
    print(course.name)

print("andres calc2 grade")
print(test.getStudentGrade(andre, calc))

print("andres GPA")
print(test.getStudentGradePointAverage(andre))

print("calc2 average")
print(test.calculateCourseAverage(calc))

print("try adding andre to time conflicted course")
print(test.addStudentToCourse(andre, trig))

print("remove andre from calc2")
print(test.removeStudentfromCourse(andre, calc))
print("students taking calc2 after removing andre")
for student in test.getStudentsOfCourse(calc):
    print(student.name)
print("courses andre is taking after removing calc2")
for course in test.getCoursesOfStudent(andre):
    print(course.name)