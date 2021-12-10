import csv

with open("powerwolf.csv", "w+") as file:

    writer = csv.DictWriter(file, fieldnames=("Song", "Year"))
    writer.writeheader()

    writer.writerow({'Song': "We drink your blood", "Year": 2011})
    writer.writerow({'Song': "Army of the night", "Year": 2015})
    writer.writerow({'Song': "Blessed & Possessed", "Year": 2015})
    writer.writerow({'Song': "The Sacrament of Sin", "Year": 2018})
    writer.writerow({'Song': "Call of the Wild", "Year": 2021})
    writer.writerow({'Song': "Blood of the Saints", "Year": 2011})

with open("powerwolf.csv", "r") as file:
    reader = csv.DictReader(file)
    print(*reader.fieldnames, sep = " "*21)
    print("*"*29)
    for row in reader:
        song_name = '"{}"'.format(row['Song'])
        print(f'{song_name.ljust(22)} : {row["Year"]}')