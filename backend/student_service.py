from firebase_admin import firestore

class StudentData:
    def __init__(self, firestore_instance):
        self.__firestore = firestore_instance

    def get_students(self):
        students = []
        studentsSnapshot = self.__firestore.collection('students').order_by('createdAt').stream()

        for oneStudentData in studentsSnapshot:
            student_data = oneStudentData.to_dict()
            student_data['id'] = oneStudentData.id
            students.append(student_data)

        return students

    def get_one_student(self, student_id):
        try:
            studentSnapshot = self.__firestore.collection('students').document(student_id).get()

            if studentSnapshot.exists:
                    student_data = studentSnapshot.to_dict()
                    student_data['id'] = studentSnapshot.id

                    return student_data
            else:
                return None
            
        except Exception as e:
            error_message = f"Error getting student: {str(e)}"
            return error_message

    def create_student(self, student_data):
        try:
            student_data['createdAt'] = firestore.SERVER_TIMESTAMP

            students_ref = self.__firestore.collection('students')
            new_student_ref = students_ref.add(student_data)

            return new_student_ref.id
        
        except Exception as e:
            error_message = f"Error creating student: {str(e)}"
            return error_message
        
    def update_student(self, student_id, student_data):
        try:
            student_data['createdAt'] = firestore.SERVER_TIMESTAMP

            student_ref = self.__firestore.collection('students').document(student_id)
            student_ref.update(student_data)

            return "Student data updated successfully!"
        
        except Exception as e:
            error_message = f"Error updating student: {str(e)}"
            return error_message
        
    def delete_student(self, student_id):
        try:
            student_ref = self.__firestore.collection('students').document(student_id)
            student_ref.delete()

            return "Student data deleted successfully!"

        except Exception as e:
            error_message = f"Error updating student: {str(e)}"
            return error_message
        