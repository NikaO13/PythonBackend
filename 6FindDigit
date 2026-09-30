def FindDigit(n):
    length, count, start = 1, 9, 1

    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (n - 1) // length
    return str(number)[(n - 1) % length]

print(FindDigit(int(input())))
