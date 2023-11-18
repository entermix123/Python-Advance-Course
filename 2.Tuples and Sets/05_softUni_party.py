guests = int(input())

db_guests = set()
db_arrived = set()

for _ in range(guests):
    user = input()
    db_guests.add(user)

user = input()
while user != 'END':
    db_arrived.add(user)
    user = input()

missing_guests = db_guests.difference(db_arrived)
print(len(missing_guests))

# for guest in sorted(missing_guests):
#     print(guest)

miss_vips = set(guest for guest in missing_guests if guest[0].isdigit())
miss_regs = missing_guests - miss_vips      # missing_guests.difference(miss_vips)

for vip in sorted(miss_vips):
    print(vip)

for reg in sorted(miss_regs):
    print(reg)
