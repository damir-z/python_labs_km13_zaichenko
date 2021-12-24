while True:
    try:
        n = float(input("Enter number of pages: "))
        if n > 1280 or n <= 0:
            print("Incorrect input. Enter a number smaller than 1280 and bigger than 0.\n")
        elif n % 16 != 0:
            print("Incorrect input. Number must be a multiply of 16.\n")
        else:
            break
    except ValueError:
        print("Incorrect input. Please, enter a number.\n")

def split(active=False):
    def wrap(func):
        def wrapper(n):
            if active:
                splitted_list = []
                num_lst = [*func(n)]
                for lst in num_lst:
                    splitted_page = []
                    for i in range(1, 5):
                        splitted_page.append(tuple(lst[(i - 1) * 4:(i * 4)]))
                    splitted_list.append(splitted_page)
                return splitted_list
            else:
                return func(n)
        return wrapper
    return wrap

@split(True)
def numeration(n):
    book_nums = []
    for i in range(1, int(n/16)+1):
        sheet_nums = []
        for j in range(4):
            sheet_nums += [(16*i)-(2*j), (16*(i-1))+1+(j*2), (16*(i-1))+2+(j*2), (16*i)-(2*j)-1]
        book_nums.append(sheet_nums)
    return book_nums

@split(True)
def gen_numeration(n):
    for i in range(1, int(n/16)+1):
        sheet_nums = []
        for j in range(4):
            sheet_nums += [(16*i)-(2*j), (16*(i-1))+1+(j*2), (16*(i-1))+2+(j*2), (16*i)-(2*j)-1]
        yield sheet_nums

print(f"\nTotal amount of notebooks in a book : {int(n/16)}.\n\nPages numbers (using function):")
for i in numeration(n):
    print(i)
print("\nPages numbers (using generator):")
for i in gen_numeration(n):
    print(i)