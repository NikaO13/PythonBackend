string = input().lower()

foundChars = {}

for char in string:
    if char in foundChars:
        foundChars[char] += 1
    else:
        foundChars[char] = 1

foundChars = sorted(foundChars.items(), key=lambda x: x[1], reverse=True)

for i in range(3):
    print(foundChars[i][0], foundChars[i][1])

