from collections import deque

food_quantity = int(input())
is_complete = True
orders = deque(map(int, input().split()))
print(max(orders))

n = len(orders)                         # how many orders
for order in range(n):                  # cycle true orders
    if orders[0] <= food_quantity:      # if quantity is more than the order
        food_quantity -= orders[0]      # subtract order form the quantity
        orders.popleft()                # delete order from the deque
    else:                               # if order si bigger than quantity
        is_complete = False             # orders not complete flag
        break                           # exit cycle
if is_complete:                         # if all orders are complete
    print(f'Orders complete')           # print result
else:
    left_orders = [str(x) for x in orders]          # make left orders of the deque to string values
    print(f"Orders left: {' '.join(left_orders)}")  # print left orders