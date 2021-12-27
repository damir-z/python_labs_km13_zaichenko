from exp_root.root import root2, root3
from exp_root.exponentiation import exp2, exp3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg


def _input_check(input_text, positive=False, natural=False, is_not_1=False):
    while True:
        try:
            user_input = float(input(input_text))
            if positive and not user_input > 0:
                error = "You have to enter positive number."
            elif natural and int(user_input) != user_input:
                error = "You have to enter natural number."
            elif is_not_1 and user_input == 1:
                error = "You have to enter a number different from 1."
            else:
                return [user_input, int(user_input)][user_input==int(user_input)]

            print("Error.", error, "Try again.\n")
        except ValueError:
            print("Error. You have to enter a number. Try again.\n")


def main():
    functions = {" x²": "square of x", " x³": "cube of x", "²√x": "square root of x",
                 "³√x" : "cube root of x", " x!": "factorial of x", " logₐ(x) ": "log. of x with base a",
                 " ln(x)": "natural log. of x", " lg(x)": "log. of x with base 10", " exit": "close program"}

    while True:

        print("\nSelect function(1-8) or type '9' to exit: \n" + "="*41)
        for i in range(len(functions)):
            print(f" {i+1}.{list(functions.keys())[i].ljust(9)} {list(functions.items())[i][1].rjust(27)}")
        print("="*41+"\n")

        f = _input_check("", natural=True)

        if f in [1, 2]:
            n = _input_check("Enter x: ")
            print(f"The {['square', 'cube'][f==2]} of {n} is {[exp2, exp3][f==2](n)}.")
        elif f in [3, 4]:
            n = _input_check(f"Enter {['', 'a positive '][f == 3]}x: ", positive=[False, True][f == 3])
            print(f"The {['square', 'cube'][f==4]} root of {n} is {[root2, root3][f==4](n)}.")
        elif f == 5:
            n = _input_check("Enter a natural number: ", natural=True, positive=True)
            print(f"The factorial of {n} is {fact(n)}.")
        elif f == 6:
            a = _input_check("Enter the base of a logarithm: ", positive=True, is_not_1=True)
            n = _input_check("Enter x: ", positive=True)
            print(f"The logarithm of {n} with base {a} is {[log(a, n), int(log(a, n))][log(a,n)==int(log(a,n))]}.")
        elif f in [7, 8]:
            n = _input_check("Enter x: ", positive=True)
            print(f"{['lg', 'ln'][f == 7]}({n}) = {[lg, ln][f == 7](n)}")
        elif f == 9:
            break
        else:
            print("Error. You have to enter a number between 1 and 9")
            continue

        if input("\nDo you want to continue working?(y/n): ").lower().strip() != "y":
            break


if __name__ == "__main__":
    main()