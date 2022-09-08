from Course import Course
from Student import Student
from StudentCourseAssignment import StudentCourseAssignment

test = StudentCourseAssignment()
andre = Student("andre", 12)
beza = Student("beza", 12)
calc = Course("calc", "12", "12", {"day" : "M", "start" : 4, "end" : 5}, 4)
trig = Course("trig", "12", "12", {"day" : "M", "start" : 4, "end" : 5}, 4)

print(test.createStudent(andre))
print(test.createStudent(beza))
print(test.createCourse(calc))
print(test.createCourse(trig))
andre.name = "andre bland"
print(test.updateStudent(andre))
calc.name = "calc2"
print(test.updateCourse(calc))
print(test.addStudentToCourse(andre, calc))
print(test.addStudentToCourse(beza, calc))
print(test.setStudentGradeForCourse(andre, calc, 5))
print(test.setStudentGradeForCourse(beza, calc, 4))

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

print(test.removeStudentfromCourse(andre, calc))