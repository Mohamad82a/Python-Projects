
def view_students(students):
    if not students:
         print('No students Found')
    else:
        print(students)
        




def add_student(students, student_id, first_name, last_name, age, courses, grades):
    
    
    student = {
        
        "Student_ID" : student_id,
        "Fisrt_Name" : first_name,
        "Last_Name" : last_name,
        "Age" : age,
        "Enrolled_Courses" : courses,
        "Grades" : grades       
        
    }
    students.append(student)
    
    
    
def create_student(students, student_id, first_name, last_name, age, courses, grades):
    return {
        
        "Student_ID" : student_id,
        "Fisrt_Name" : first_name,
        "Last_Name" : last_name,
        "Age" : age,
        "Enrolled_Courses" : courses,
        "Grades" : grades       
        
    }
    
    
def update_student(students, student_id):
    for student in students:
        student.update(update_student)



def average_calculator(grades):
    average_grade = sum(grades.values()) / len(grades)
    return average_grade

    
def delete_student(students, student_id):
    for student in students:
        if student['Student_ID'] == student_id:
            students.remove(student)