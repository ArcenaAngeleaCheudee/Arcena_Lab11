
grdes = []
num = 1

while True:
    stud_grade = input(f"Student grade {num}: ")
    num += 1

    if stud_grade != "done":
        continue
    elif not stud_grade.isdigit():
        print("Invalid character, plese enter real numbers only")
        break
    elif 40 <= int(stud_grade) <= 100:
        continue
    else: 
        int(stud_grade) <= 39 or int(stud_grade) >= 101
        print("Invlid data, please enter real numbers only")
