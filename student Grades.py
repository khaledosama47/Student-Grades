def add_student(filename):
    name = input("Enter student name: ")
    while True:
        try:
            grade = float(input("Enter student grade: "))
            if 0 <= grade <= 100:
                break
            else:
                print("Grade should be between 0 and 100.")
        except ValueError:
            print("Invalid grade. Please enter a number.")

    with open(filename, 'a') as file:
        file.write(f"{name},{grade}\n")
    print(f"Student {name} added successfully.")

def view_students(filename):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    name, grade = student.strip().split(',')
                    print(f"Name: {name}, Grade: {grade}")
    except FileNotFoundError:
        print("No student records found.")

def search_student(filename):
    name = input("Enter student name: ")
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
            for student in students:
                student_name, grade = student.strip().split(',')
                if student_name.lower() == name.lower():
                    print(f"Grade of {name}: {grade}")
                    return
            print(f"Student {name} not found.")
    except FileNotFoundError:
        print("No student records found.")

def find_highest_lowest(filename):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
            if not students:
                print("No students found.")
            else:
                grades = [float(student.strip().split(',')[1]) for student in students]
                highest_grade = max(grades)
                lowest_grade = min(grades)
                print(f"Highest Grade: {highest_grade}")
                print(f"Lowest Grade: {lowest_grade}")
    except FileNotFoundError:
        print("No student records found.")

def calculate_average(filename):
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
            if not students:
                print("No students found.")
            else:
                grades = [float(student.strip().split(',')[1]) for student in students]
                average_grade = sum(grades) / len(grades)
                print(f"Average Grade: {average_grade:.2f}")
    except FileNotFoundError:
        print("No student records found.")

def remove_student(filename):
    name = input("Enter student name: ")
    try:
        with open(filename, 'r') as file:
            students = file.readlines()
        with open(filename, 'w') as file:
            student_found = False
            for student in students:
                student_name, grade = student.strip().split(',')
                if student_name.lower() != name.lower():
                    file.write(f"{student_name},{grade}\n")
                else:
                    student_found = True
            if student_found:
                print(f"Student {name} removed successfully.")
            else:
                print(f"Student {name} not found.")
    except FileNotFoundError:
        print("No student records found.")

def main():
    filename = 'student_grades.txt'
    while True:
        print("\nStudent Grade Manager")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Find Highest and Lowest Grades")
        print("5. Calculate Average Grade")
        print("6. Remove Student")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(filename)
        elif choice == '2':
            view_students(filename)
        elif choice == '3':
            search_student(filename)
        elif choice == '4':
            find_highest_lowest(filename)
        elif choice == '5':
            calculate_average(filename)
        elif choice == '6':
            remove_student(filename)
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
    
#البرنامج ده  عباره عن تحكم في درجات الطلاب
#البرنامج بيستخدم ملف نصي اسمه student_grades.txt عشان نحفظ فيه درجات الطلاب
#البرنامج فيه قايمه بتظهرللمستخدم  فيها كتير زي إضافه  طالب وعرض الطلاب وعرض الطالب
#والبرنامج هيفضل يشتغل لحد أما المستخدم يختار الخروخ
# والبرنامج ده  نفس فكره المكتبه  كان بيضيف بيانات وبيعرض وبيحزف  بس احنا هتا استخدمنا ملف نصي.