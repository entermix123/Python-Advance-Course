textiles = [int(x) for x in input().split()]                        # make list of user input
medicaments = list(reversed([int(x) for x in input().split()]))     # make reversed list to take fist element also

meds = {                # create dictionary with possible items to be made
    'MedKit': 100,
    'Bandage': 40,
    'Patch': 30,
}

created = {             # create dictionary for created medaicaments
    'MedKit': 0,
    'Bandage': 0,
    'Patch': 0,
}

while textiles and medicaments:

    current_textile = textiles.pop(0)       # take first textile
    current_med = medicaments.pop(0)        # take last medicament ( medicament are reversed )
    current_value = current_textile + current_med   # make sum

    for key, value in meds.items():
        if current_value >= meds['MedKit']:     # if enough for MedKit
            created['MedKit'] += 1              # add point to MedKit
            current_value -= value              # subtract the price for MedKit to the sum
            if not current_value:               # if there is not remind value
                break                           # break
            medicaments[0] += current_value     # if any remind value, add them to next medicine element
            break                               # break
        elif current_value == value:            # if price is equal to any other medicine item
            created[key] += 1                   # add point ot created key
            break                               # break
    else:                                       # if sum is not enough for MedKit and not equal to any other medicine
        medicaments.insert(0, current_med + 10) # add 10 points to current medicine value and insert it for the next try

# sort descending by value and ascending by key
created = sorted(created.items(), key=lambda x: (-x[1], x[0]))
# created is list of tuples

# print results
if not textiles and not medicaments:
    print(f"Textiles and medicaments are both empty.")
elif not textiles:
    print(f"Textiles are empty.")
elif not medicaments:
    print(f"Medicaments are empty.")

for key, value in created:              # iterate true the list of tuples
    if value != 0:                      # do not print not made medicament items
        print(f'{key} - {value}')       # print result

# print results
if medicaments:
    print(f'Medicaments left: {", ".join(str(x) for x in medicaments)}')
if textiles:
    print(f'Textiles left: {", ".join(str(x) for x in textiles)}')
