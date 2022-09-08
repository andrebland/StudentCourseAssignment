from flask import Flask, json, request, jsonify
from requests import Response
from AbstractBusinessController import AbstractBusinessController
from BusinessController import BusinessController
from DatabaseController import DatabaseController

#TODO implement better error handling

class DataService:
  def __init__(self, businessController :AbstractBusinessController, api :Flask):
    self.businessController = businessController
    self.api = api


#init
dbController = DatabaseController()
businessController = BusinessController(dbController)
api = Flask("StudentCourseAssignment")
dataservice = DataService(businessController, api)
#

#POST METHODS
@dataservice.api.route('/api/create_student', methods=['POST'])
def create_student():
  dataservice.businessController.createStudent(json.loads(request.json))
  return "success", 200

@dataservice.api.route('/api/create_course', methods=['POST'])
def create_course():
  dataservice.businessController.createCourse(json.loads(request.json))
  return "success", 200
#

#PUT METHODS
@dataservice.api.route('/api/update_student', methods=['PUT'])
def update_student():
  id = int(request.args['id'])
  print(dataservice.businessController.updateStudent(id, json.loads(request.json)))
  return "success", 200

@dataservice.api.route('/api/update_course', methods=['PUT'])
def update_course():
  id = int(request.args['id'])
  dataservice.businessController.updateCourse(id, json.loads(request.json))
  return "success", 200

@dataservice.api.route('/api/course_add_student', methods=['PUT'])
def add_student_to_course():
  student_id = int(request.args['student_id'])
  course_id = int(request.args['course_id'])
  ret = dataservice.businessController.addStudentToCourse(student_id, course_id)
  if ret is None:
    return "failure", 400

  return "success", 200

@dataservice.api.route('/api/course_remove_student', methods=['PUT'])
def course_remove_student():
  student_id = int(request.args['student_id'])
  course_id = int(request.args['course_id'])
  print(dataservice.businessController.removeStudentfromCourse(student_id, course_id))
  return "success", 200

@dataservice.api.route('/api/student_set_grade', methods=['PUT'])
def set_student_grade():
  student_id = int(request.args['student_id'])
  course_id = int(request.args['course_id'])
  grade = int(request.args['grade'])
  dataservice.businessController.setStudentGradeForCourse(student_id, course_id, grade)
  return "success", 200
#


#GET METHODS
@dataservice.api.route('/api/student_get_grade', methods=['GET'])
def get_student_grade():
  student_id = int(request.args['student_id'])
  course_id = int(request.args['course_id'])
  return jsonify(dataservice.businessController.getStudentGrade(student_id, course_id)), 200

@dataservice.api.route('/api/student_get_gpa', methods=['GET'])
def get_student_gpa():
  student_id = int(request.args['student_id'])
  return jsonify(dataservice.businessController.getStudentGradePointAverage(student_id)), 200

@dataservice.api.route('/api/students_in_course', methods=['GET'])
def get_students_in_course():
  course_id = int(request.args['course_id'])
  return jsonify(dataservice.businessController.getStudentsOfCourse(course_id)), 200

@dataservice.api.route('/api/student_get_courses', methods=['GET'])
def get_student_courses():
  student_id = int(request.args['student_id'])
  return jsonify(dataservice.businessController.getCoursesOfStudent(student_id)), 200

@dataservice.api.route('/api/course_get_gpa', methods=['GET'])
def course_get_gpa():
  course_id = int(request.args['course_id'])
  return jsonify(dataservice.businessController.calculateCourseAverage(course_id)), 200
#


if __name__ == '__main__':
    dataservice.api.run(host='localhost', port=1024)