# def age_assignment(*names, **ages):
#     result = {}
#     for name in names:
#         if name[0] in ages:
#             result[name] = ages[name[0]]
#     result = sorted(result.items(), key=lambda k: k[0])
#     return '\n'.join(f'{t} is {h} years old.' for t, h in result)

def age_assignment(*names, **ages):
    result = []

    for letter, age in ages.items():
        person_name = ''

        for name in names:
            if name.startswith(letter):     # check if starting letter is in ages keys
                person_name = name          # add name to person name
                break                       # break the cycle

        result.append(f'{person_name} is {age} years old.')

    return '\n'.join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
