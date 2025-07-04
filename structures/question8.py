names = ["ramesh", "ravi", "ram", "sita", "ben", "micheal"]
dic_name = {}
for items in names:
    if items in dic_name:
        dic_name[items] += 1
    else:
        dic_name[items] = 1


print("Names count:")
for items, count in dic_name.items():
    print(f"{items} : {count}")
