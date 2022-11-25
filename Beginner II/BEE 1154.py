age = total = count = 0
while age >= 0:
    total += age
    count += 1
    age = int(input())

print(f"{total / (count - 1):.2f}")
