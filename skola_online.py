"""
Skola online
"""
class Student:
    """
    class student
    """
    def __init__(self, student_name):
        """
        Constructor of Student
        """
        self._student_name = student_name
        self._clazz = None
    @property
    def student_name(self):
        """
        property student name
        """
        return self._student_name

    def set_class(self, clazz):
        """
        set class
        """
        self._clazz = clazz
class Clazz:
    """
    class clazz
    """
    def __init__(self, clazz_name):
        """
        Constructor of Clazz
        """
        self._clazz_name = clazz_name
        self._students = []

    def add_student(self, student):
        """
        add student
        """
        self._students.append(student)

    def remove_student(self, student):
        """
        remove student
        """
        self._students.remove(student)

class Subject:
    """
    class subject
    """
    def __init__(self, subject_name):
        """
        Constructor of Subject
        """
        self._subject_name = subject_name
        self._grades = {}

    def add_grade(self, student, grade):
        """
        add grade
        """
        self._grades[student] = grade

    def get_total_grade(self):
        """
        get total grade
        """
        if not self._grades:
            return 0
        return sum(self._grades.values()) / len(self._grades)

students = []
clazzes = []
subjects = []

def create_student(name):
    """
    create student
    """
    student = Student(name)
    students.append(student)
    return student

def remove_student(student):
    """
    remove student
    """
    if student in students:
        students.remove(student)
    else:
        print("Student not found.")

def edit_student(student, name):
    """
    edit student
    """
    student._name = name

def create_clazz(clazz_name):
    """
    create clazz
    """
    clazz = Clazz(clazz_name)
    clazzes.append(clazz)
    return clazz

def remove_clazz(clazz):
    """
    remove clazz
    """
    if clazz in clazzes:
        clazzes.remove(clazz)
    else:
        print("Class not found.")

def create_subject(predmet_name):
    """
    create subject
    """
    subject = Subject(predmet_name)
    subjects.append(subject)
    return subject

def remove_subject(subject):
    """
    remove subject
    """
    if subject in subjects:
        subjects.remove(subject)
    else:
        print("Subject not found.")
        subjects.remove(subject)

def display_total_grades(subject):
    """
    display total grades
    """
    for student, grade in subject._grades.items():
        print(f"{student._student_name}: {grade}")
    total_grade = subject.get_total_grade()
    print(f"Total grade in {subject._subject_name}: {total_grade}")

if __name__ == "__main__":
    while True:
        print()
        print("School Online Menu:")
        print("1. Create student")
        print("2. Delete student")
        print("3. Edit student")
        print("4. Create class")
        print("5. Delete class")
        print("6. Create subject")
        print("7. Delete subject")
        print("8. Add grade")
        print("9. Display total grades for subject")
        print("10. Exit")

        choice = input("Choose an option (1-10): ")

        if choice == "1":
            name = input("Enter the name of the student: ")
            create_student(name)

        elif choice == "2":
            name = input("Enter the name of the student to delete: ")
            for student in students:
                if student._student_name == name:
                    remove_student(student)
                    break
            else:
                print("Student not found.")

        elif choice == "3":
            name = input("Enter the name of the student to edit: ")
            for student in students:
                if student._student_name == name:
                    new_name = input("Enter the new name of the student: ")
                    edit_student(student, new_name)
                    break
            else:
                print("Student not found.")

        elif choice == "4":
            clazz_name = input("Enter the name of the class: ")
            create_clazz(clazz_name)

        elif choice == "5":
            clazz_name = input("Enter the name of the class to delete: ")
            for clazz in clazzes:
                if clazz.clazz_name == clazz_name:
                    remove_clazz(clazz)
                    break
            else:
                print("Class not found.")

        elif choice == "6":
            subject_name = input("Enter the name of the subject: ")
            create_subject(subject_name)

        elif choice == "7":
            subject_name = input("Enter the name of the subject to delete: ")
            for subject in subjects:
                if subject._subject_name == subject_name:
                    remove_subject(subject)
                    break
            else:
                print("Subject not found.")

        elif choice == "8":
            student_name = input("Enter the name of the student: ")
            subject_name = input("Enter the name of the subject: ")
            grade = int(input("Enter the grade: "))
            for student in students:
                if student._student_name == student_name:
                    for subject in subjects:
                        if subject._subject_name == subject_name:
                            subject.add_grade(student, grade)
                            break
                    else:
                        print("Subject not found.")
                    break
            else:
                print("Student not found.")

        elif choice == "9":
            subject_name = input("Enter the name of the subject: ")
            for subject in subjects:
                if subject._subject_name == subject_name:
                    display_total_grades(subject)
                    break
            else:
                print("Subject not found.")

        elif choice == "10":
            break

        else:
            print("Invalid choice. Enter a number from 1 to 10.")
