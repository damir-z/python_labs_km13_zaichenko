item_list = []
while True:
    item = input("Enter element or enter 'STOP' to finish entering: ")
    if item.lower() == 'stop':
        break
    else:
        item_list.append(item)
if len(item_list) != 1:
    print(', '.join(item_list[0:-1]), "and", item_list[-1])
else:
    print(item_list[0])
