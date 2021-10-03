def input_type_check(input_text, type): # input check function
    while True:
        user_input = input("Enter {}: ".format(input_text))
        if type == "digit" and user_input.isdigit() == True:
            return user_input
        elif type == "digit" and user_input.isdigit() == False:
            print("Error. Letters can't be in {}!".format(input_text))
        elif type == "alpha" and user_input.isalpha() == True:
            return user_input
        elif type == "alpha" and user_input.isalpha() == False:
            print("Error. Digits can't be in {}!".format(input_text))

while True:
    name, surname = input_type_check("name", "alpha"), input_type_check("surname", "alpha") # input block
    phone_number = input_type_check("phone number", "digit")
    street = input_type_check("street", "alpha")
    house = input_type_check("house", "digit")
    flat = input_type_check("flat", "digit")
    city = input_type_check("city", "alpha")
    index = input_type_check("index", "digit")
    country = input_type_check("country", "alpha")

    print(name.title(), surname.title()) # output block
    print(phone_number)
    print('Str. {} {}, ap.{}, {}'.format(street.title(), house, flat, city.title()))
    print(index)
    print(country)

    if input('Enter "STOP" to exit or else to continue: ').lower() == 'stop': # block, that allows user to finish programm
        print("Program finished!")
        break