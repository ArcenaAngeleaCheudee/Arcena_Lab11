grades = []
passed_students = []
num = 1

while True:
    stud_grade = input(f"Student grade {num}: ")
    num += 1
    stud_grade = int(stud_grade)
    if stud_grade >= 40 and stud_grade <= 100:
        continue
    elif not stud_grade.isdigit():
        print("Invalid character, please enter real numbers only")
        break 
    elif int(stud_grade) <= 39 or int(stud_grade) >= 101:
        print("Invalid data, please enter real numbers only")
    else:
        if(stud_grade.lower() == "done"):
            break

grades.append(stud_grade)
grade = int(stud_grade)

if grades:
    average_grade = sum(grades) / len(grade)
    print(f"Average Grade: {average_grade}")
