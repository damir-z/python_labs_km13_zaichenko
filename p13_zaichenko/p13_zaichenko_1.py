with open("gadsby.txt", "r") as f:
    text = f.read()
letters_list = list(map(str.lower, list(filter(str.isalpha, text))))
alphabet = list("abcdefghijklmnopqrstuvwxyz")
amounts = list(map(lambda x: round(100 * letters_list.count(x) / len(letters_list), 3), alphabet))
sorted_amounts = list(reversed(sorted(amounts)))

print("Sorted by amounts:\n")
for i in range(len(sorted_amounts)):
    print(f"{alphabet[amounts.index(sorted_amounts[i])]}: {sorted_amounts[i]}%")
print("\nMust frequent five ones:\n")
for i in range(5):
    print(f"{alphabet[amounts.index(sorted_amounts[i])]}: {sorted_amounts[i]}%")
print("\nMust rare five ones:\n")
for i in range(5, 0, -1):
    print(f"{alphabet[amounts.index(sorted_amounts[-i])]}: {sorted_amounts[-i]}%")