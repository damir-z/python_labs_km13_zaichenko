import numpy as np

years = np.arange(1900, 2020 + 1, 1)


def intercalary_years(years_list):
    "function that returns all intercalary years from list"
    return list(filter(lambda x: not (x % 4 and x % 100) and x % 100 or not x % 400, years_list))


def days_amount(f, month, year):
    if month in [1, 3, 5, 7, 8, 10, 12, 14]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return [28, 29][year in f(years)]


months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

while True:
    while True:
        try:
            year = int(input("Enter a year: "))
            if 1900 <= year <= 2021:
                break
            else:
                print("Error. Year must be a number between 1900 and 2021. Try again!")
        except ValueError:
            print("Error. Year must be an integer number. Try again!")
    while True:
        try:
            month = int(input("Enter a number of month: "))
            print("\nIt's {} of {} and the amount of days is {}.".format(months[month - 1], year, days_amount(intercalary_years, month, year)))
            break
        except ValueError:
            print("Error. Number of month must be an integer number. Try again!")
        except IndexError:
            print("Error. Number of month must be a number between 1 and 12. Try again!")
    if input("\nDo you want to continue?(y/n): ").lower() != 'y':
        break
