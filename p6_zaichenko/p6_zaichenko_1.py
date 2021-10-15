while True:
    first_set = set(filter(str.isalpha, input("Enter first string: ").lower()))
    second_set = set(filter(str.isalpha, input("Enter second string: ").lower()))

    if first_set == set() or second_set == set():
        print("You haven't entered any letters!")
    else:
        print("Set of letters of first string: {}\nSet of letters of second string: {}".format(first_set, second_set))
        print("You {} form the second string from the first one.".format(["can't", "can"][second_set.issubset(first_set)]))

        if input("Enter 'YES' to code another message or else - to exit: ").lower() == "yes":
            continue
        else:
            break