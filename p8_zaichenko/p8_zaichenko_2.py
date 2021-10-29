from math import sqrt

def type_check(input_text):
    while True:
        try:
            input_result = float(input(input_text))
            return input_result
        except ValueError as ve:
            print("Error. " + str(ve).capitalize() + ". Try again. ")

while True:
    a, b, c = type_check("\nEnter a: "), type_check("Enter b: "), type_check("Enter c: ")
    print("\n({})x^2 + ({})x + {} = 0 \n".format(a, b, c))
    try:
        if a == 0:
            if b == 0:
                raise ZeroDivisionError(
                    ["Equation doesn't have any solutions", "Equation has infinite solutions."][c == 0])
            else:
                print("Answer: x = {}".format([-c / b, 0][c == 0]))
        if a != 0:
            d = sqrt(b ** 2 - 4 * a * c)
            print(["x1 = {} \nx2 = {} ".format(((-b + d) / 2 * a), ((-b - d) / 2 * a)), "x = {} ".format(-b / 2 * a)][
                      d == 0])
    except ValueError as ve:
        print(str(ve).capitalize() + ". You tried to get square root of negative number.")
    except ZeroDivisionError as zde:
        print(zde)

    if input("\nDo you want to continue?(y/n): ").lower() != 'y':
        break
