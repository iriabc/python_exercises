number = int(raw_input("Please tell me a number: "))

divisors = []

for num in range(1, number, 1):
    if number % num == 0:
        divisors.append(num)

print divisors


