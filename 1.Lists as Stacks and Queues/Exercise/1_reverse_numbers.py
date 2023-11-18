user = input().split()

for _ in range(len(user)):
    print(user.pop() + " ", end="")
