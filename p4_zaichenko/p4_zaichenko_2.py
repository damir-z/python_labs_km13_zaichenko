import math
e_types = ['micro', 'very minor', 'minor', 'light', 'moderate', 'strong', 'major', 'great', 'meteoric']
while True:
    while True:
        points = input("Enter earthquake points: ")
        try:
            points = float(points)
            if points <= 0:
                print("There was a no earthquake!")
            elif 0 < points < 2:
                print("There was a micro earthquake!")
            elif 8 <= points < 10:
                print("There was a great earthquake!")
            elif points >= 10:
                print("There was a meteoric earthquake!")
            else:
                print("There was a {} earthquake!".format(e_types[math.floor(points)-1]))
            break
        except ValueError:
            print("Enter digits, not letters!")
    if input('Enter "STOP" to exit or else to continue: ').lower() == 'stop':
        print("Program finished!")
        break