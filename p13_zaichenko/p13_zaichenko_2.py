males, females = dict(), dict()

for i in range(1880, 2020):
    with open(f"names/yob{i}.txt", "r") as f:
        male, female = ["", 0], ["", 0]
        for j in f:
            if ',M,' in str(j):
                if int(str(j)[int(j.rfind(","))+1::]) > male[1]:
                    male[1], male[0] = int(str(j)[int(j.rfind(","))+1::]), str(j)[:int(j.find(",")):]
            else:
                if int(str(j)[int(j.rfind(","))+1::]) > female[1]:
                    female[1], female[0] = int(str(j)[int(j.rfind(","))+1::]), str(j)[:int(j.find(",")):]

    males[male[0]] = males.get(male[0], 0) + 1
    females[female[0]] = females.get(female[0], 0) + 1

males = dict(sorted(males.items(), key=lambda item: item[1], reverse= True))
females = dict(sorted(females.items(), key=lambda item: item[1], reverse= True))

for i in males:
    print(i, males[i])
print()
for i in females:
    print(i, females[i])