def match(current_seat, available_seats, char1, matches):
    current_seat = str(current_seat)
    incoming_users1.remove(incoming_users1[0])
    incoming_users2.remove(incoming_users2[0])
    for value in available_seats[char1]:
        if current_seat == value:
            available_seats[char1].remove(value)
    matches.append(current_seat + char1)
    return available_seats, matches


user_seats = [user for user in input().split(', ')]

seats = {}

for i in user_seats:
    current_letter = i[-1]
    if len(i) == 3:
        current_num = i[0:2]
    else:
        current_num = i[0]

    if current_letter not in seats:
        seats[current_letter] = [current_num]
    else:
        seats[current_letter].append(current_num)

incoming_users1 = [x for x in input().split(', ')]
incoming_users2 = list(reversed([x for x in input().split(', ')]))

# input
# 17K, 20B, 3C, 15D, 31Z, 28F
# 20, 35, 15, 3, 2, 10
# 1, 15, 64, 53, 45, 46

matches = []
seat_matches = 0    # max 3
rotations = 0       # max 10

while seat_matches < 3 and rotations < 10:

    seat_1 = incoming_users1[0]
    seat_2 = incoming_users2[0]
    char = chr(int(seat_1) + int(seat_2))
    rotations += 1

    if char in seats:
        if seat_1 in seats[char]:
            seats, matches = match(seat_1, seats, char, matches)
            seat_matches += 1
        elif seat_2 in seats[char]:
            seats, matches = match(seat_2, seats, char, matches)
            seat_matches += 1
        elif (str(seat_1) + char) in matches or (str(seat_2) + char) in matches:
            incoming_users1.remove(seat_1)
            incoming_users2.remove(seat_2)
        else:
            num = incoming_users1.pop(0)
            incoming_users1.append(num)
            num2 = incoming_users2.pop(0)
            incoming_users2.append(num2)
    else:
        num = incoming_users1.pop(0)
        incoming_users1.append(num)
        num2 = incoming_users2.pop(0)
        incoming_users2.append(num2)


print(f'Seat matches: {", ".join(matches)}\nRotations count: {rotations}')
