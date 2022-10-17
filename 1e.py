import time
list0 = ["1792 53160", "3 34"]
list1 = []
list2 = []
for item in list1:
    for subitem in item.split():
        if (subitem.isdigit()):
            list1.append(subitem)
            x = [int(a) for a in list(list2)]
time.sleep(3)
            
print(x)
y= str(x).strip("[").strip("]").strip(" ").strip(",")
print(y)

# list1.append(z)
# print(list1)



           



