def gather_credits(credit_needed, *args):
    sum_credit = 0
    done = {}

    for x in args:
        course_name = x[0]
        course_credit = int(x[1])

        if course_name in done:
            done[course_name] += 1
            continue

        done[course_name] = 1
        sum_credit += course_credit

        if sum_credit >= credit_needed:
            result = [f"Enrollment finished! Maximum credits: {sum_credit}.\n", f'Courses: ']

            done = sorted(done.items(), key=lambda j: j[0])
            courses_done = []
            for key, value in done:
                courses_done.append(key)

            result.append(', '.join(courses_done))

            return ''.join(result)

    return f"You need to enroll in more courses! You have to gather {credit_needed - sum_credit} credits more."


# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))

# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))


print(gather_credits(
    60,
    ("Basics", 17),
    ("Fundamentals", 17),
    ("Advanced", 1),
    ("Web", 10),
    ("Advanced", 10),
    ("Maafaka", 20),
))
