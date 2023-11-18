def students_credits(*args):
    subjects = {}
    diploma = 240
    sum_credits = 0.0
    result = []

    for current_course in args:
        course, credit, max_points, result_points = current_course.split('-')
        result_credit_percentage = float(result_points) / float(max_points)
        result_credit = float(credit) * result_credit_percentage
        subjects[course] = result_credit
        sum_credits += result_credit

    if sum_credits >= diploma:
        result.append(f"Diyan gets a diploma with {sum_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {float(diploma - sum_credits):.1f} credits more for a diploma.")

    subjects = sorted(subjects.items(), key=lambda x: -x[1])

    for course, credit in subjects:
        result.append(f"{course} - {credit:.1f}")

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
# print(
#     students_credits(
#         "Discrete Maths-40-500-450",
#         "AI Development-20-400-400",
#         "Algorithms Advanced-50-700-630",
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Game Engine Development-70-100-70",
#         "Mobile Development-25-250-225",
#         "QA-20-300-300",
#     )
# )

# print(
#     students_credits(
#         "Python Development-15-200-200",
#         "JavaScript Development-12-500-480",
#         "C++ Development-30-500-405",
#         "Java Development-10-300-150"
#     )
# )
