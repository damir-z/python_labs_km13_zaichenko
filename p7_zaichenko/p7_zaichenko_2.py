def ten_to_sixteen(number):
    codes = ["A", "B", "C", "D", "E", "F"]
    result = ""
    while number >= 16:
        if number%16 < 10:
            result = str(number%16) + result
        else:
            result = str(codes[(number % 16)-10]) + result
        number //= 16
    if number>9:
        result = str(codes[number-10]) + result
    else:
        result = str(number) + result
    result = [result, "0"+result][len(result)-2]
    return result

while True:
    x = 1
    result = ""
    while True:
        rgb = input("Введiть значення кольору у системi RGB через пробiл: ").split(" ")
        try:
            rgb = list(map(int, rgb))
            if len(rgb) == 3:
                k = 0
                for i in rgb:
                    if 0 <= i < 256:
                        k += 1
                    else:
                        print(
                            "Помилка. Неправильно введенi данi. Числа мають приймати значення вiд 0 до 256. Спробуйте ще раз!")
                        continue
                if k == 3:
                    break
            else:
                print("Помилка. Неправильно введенi данi. Значень у системi RGB повинно бути три. Спробуйте ще раз!")
                continue
        except:
            print("Помилка. Неправильно введенi данi. Спробуйте ще раз")

    for i in rgb:
        result += ten_to_sixteen(i)

    print("\nШiстнадцяткове представлення кольору: #" + result)
    if input("\nБажаєте продовжити роботу? (y/n): ").lower() != 'y':
            break