import re
import time
import fileinput
#import zipfile

#archive = zipfile.ZipFile('archive.zip', 'r')
males, females = dict(), dict()

for i in range(1880, 2019):
    """If you want to work not with a folder, but directly with an archive,
    uncomment strings 4, 8, 15, and comment string 16 (Getting the results will take longer.)"""

    #with archive.open(f"yob{i}.txt", "r") as f:
    with open(f"names/yob{i}.txt", "r") as f:
        male, female = ["", 0], ["", 0]
        for j in f:
            if re.search(r"[FM](?=,)", str(j))[0] == "M":
                if int(re.search(r"\d{1,}", str(j))[0]) > male[1]:
                    male[1], male[0] = int(re.search(r"\d{1,}", str(j))[0]), re.search(r"\w{1,}(?=,[FM])", str(j))[0]
            else:
                if int(re.search(r"\d{1,}", str(j))[0]) > female[1]:
                    female[1], female[0] = int(re.search(r"\d{1,}", str(j))[0]), re.search(r"\w{1,}(?=,[FM])", str(j))[0]

    if male[0] in males:
        males[male[0]] += 1
    else:
        males[male[0]] = 1

    if female[0] in females:
        females[female[0]] += 1
    else:
        females[female[0]] = 1

males = dict(sorted(males.items(), key=lambda item: item[1], reverse= True))
females = dict(sorted(females.items(), key=lambda item: item[1], reverse= True))

for i in males:
    print(i, males[i])
print()
for i in females:
    print(i, females[i])