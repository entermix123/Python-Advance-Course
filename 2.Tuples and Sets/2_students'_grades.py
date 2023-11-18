students = int(input())
db = {}
for _ in range(students):
    line = input().split()
    student = line[0]
    grade = float(line[1])
    if student not in db:
        db[student] = [float(grade)]
    else:
        db[student].append(float(grade))



for name, grades in db.items():
    avg_grade = sum(grades)/len(grades)                                 # make average grade for every student
    grades_list = " ".join(str(f'{grade:.2f}') for grade in grades)     # make list of wanted values for grades
    print(f"{name} -> {grades_list} (avg: {avg_grade:.2f})")
