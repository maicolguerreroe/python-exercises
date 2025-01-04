def odd_numbers(limit):
    for number in range(1, limit + 1):
        if number % 2 != 0:
            yield number


for i in odd_numbers(10):
    print(i)
