import numpy as np


def type_check(input_text):
    """
    Function that checks the type of entered variable
    """
    while True:
        user_input = input("{}".format(input_text))
        try:
            user_input = int(user_input)
            if user_input <= 0:
                print("Помилка. Невiрний тип даних. Число має бути додатнiм!")
                continue
            break
        except ValueError:
            print("Помилка. Невiрний тип даних. Необхiдно ввести ціле число! \n")
    return user_input


def random_matrix(dim):
    """
    The function generates dim x dim array of integers
    between 0 and 10.
    """
    matrix = np.random.randint(10, size=(dim, dim))
    return matrix


def all_perms(elements):
    """
    Function that creates list of all possible permutations of numbers in range from one to n
    """
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def items_calculating(matrix):
    """
    Function that creates list with all items of determinant
    """
    items_list = []
    for j in list(all_perms(list(range(len(matrix))))):
        a = 1
        count_of_recursions = 0
        for i in range(len(j)):
            a *= matrix[i][j[i]]
            for k in range(len(j)):
                if k > i and j[k] < j[i]:
                    count_of_recursions += 1
        if count_of_recursions % 2 == 0:
            items_list.append(a)
        else:
            items_list.append(-a)
    return items_list


def items_sum(items_list):
    """
    Function that calculates sum of determinant's items
    """
    return sum(items_list)


def determinant(matrix):
    """
    Function that calculates a determinant of matrix
    """
    return items_sum(items_calculating(matrix))


while True:
    a = random_matrix(type_check("Input dimension of a matrix: "))
    print("\nMatrix = \n\n" + " " + str(a)[1:-1])
    print("\ndet = " + str(determinant(a)))
    if input("\nБажаєте завершити?(y/n): ").lower() == "y":
        break
