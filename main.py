from flask import Flask, render_template, request, redirect
from backend.firebase_service import FirebaseService
from backend.student_service import StudentData

app = Flask(__name__)

# initialise firebase 
fc = FirebaseService()
firestore_instance = fc.get_firestore()
studentService = StudentData(firestore_instance)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/students")
def student():
    students = studentService.get_students()
    return render_template('students.html', students=students)


@app.route('/students/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('student-create.html')
 
    if request.method == 'POST':
        student_data = {
            'name' : request.form['name'],
            'grade': request.form['grade']
        }

        studentService.create_student(student_data)

        return redirect('/students')
    

@app.route('/students/<string:id>')
def viewOneStudent(id):
    studentData = studentService.get_one_student(id)
    return render_template('student-view.html', student=studentData)


@app.route('/students/<string:id>/update', methods=['POST'])
def update(id):
    student_data = {
        'name' : request.form['name'],
        'grade': request.form['grade']
    }

    studentService.update_student(id,student_data)

    return redirect("/students")

@app.route('/students/<string:id>/delete')
def delete(id):
    studentService.delete_student(id)
    return redirect("/students")