while True:
    while True:
        minutes = input("Enter minutes count: ")
        try:
            minutes = float(minutes)
            if minutes < 0:
                print("Error. Count of minutes can't be negative!")
                continue
            elif 0 <= minutes <= 50:
                price = 100
            elif 50 < minutes <= 100:
                price = 150
            elif minutes > 100:
                price = 150 + (minutes - 100)*2
            print("Total price of used minutes is {}.".format(price))
            break
        except:
            print("Error. Enter a digits, not a letters!")
    if input('Enter "STOP" to exit or else to continue: ').lower() == 'stop': # block, that allows user to finish programm
        print("Program finished!")
        break

