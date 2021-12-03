with open("gadsby.txt", "r") as f:
    text = f.read()
letters_list = list(map(str.lower, list(filter(str.isalpha, text))))
alphabet = list("abcdefghijklmnopqrstuvwxyz")
amounts = list(map(lambda x: round(100 * letters_list.count(x) / len(letters_list), 3), alphabet))

result = dict()
for i in sorted(amounts, reverse=True):
    result[i] = dict(zip(amounts, alphabet))[i]

print("Sorted by percent:\n")
for i in result:
    print(f"{result[i]} : {i}%")
print("\nFive of the most frequent:\n")
for i in range(1,6):
    print(f"{result[sorted(result)[-i]]} : {sorted(result)[-i]}%")
print("\nFive of the most rare:\n")
for i in range(0,5):
    print(f"{result[sorted(result)[i]]} : {sorted(result)[i]}%")