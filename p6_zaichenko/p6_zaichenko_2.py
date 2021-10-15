numbers = {
    '1': ['.', ',', '?', '!', ':'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [' ']
}

while True:
    string = input("Enter message: ").lower()
    result_string = ""
    for i in string:
        for j in numbers:
            try:
                result_string += (numbers[j].index(i) + 1) * j + ' '
            except ValueError:
                continue
    print("Phone variant: '{}'".format(result_string.strip()))
    if input("Enter 'YES' to code another message or else - to exit: ").lower() == "yes":
        continue
    else:
        break
