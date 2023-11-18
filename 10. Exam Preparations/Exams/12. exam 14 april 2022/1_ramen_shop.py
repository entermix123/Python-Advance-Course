bowls = list(reversed([int(x) for x in input().split(', ')]))
customers = [int(x) for x in input().split(', ')]

last_customer = 0
last_ramen = 0

while bowls and customers:

    current_bowl = bowls[0]
    current_customer = customers[0]

    if current_customer == current_bowl:
        bowls.pop(0)
        customers.pop(0)

    elif current_bowl > current_customer:
        last_ramen = current_bowl - current_customer
        customers.pop(0)
        bowls.pop(0)
        bowls.insert(0, last_ramen)

    else:
        last_customer = current_customer - current_bowl
        bowls.pop(0)
        customers.pop(0)
        customers.insert(0, last_customer)

if not bowls and not customers:
    print("Great job! You served all the customers.")
elif bowls:
    print("Great job! You served all the customers.")
    print(f"Bowls of ramen left: {', '.join(str(x) for x in list(reversed(bowls)))}")
if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
