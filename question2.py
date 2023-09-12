#O(N)


def friend(listofname):
    newlist = []         #O(1)
    for name in listofname:  #O(1)
        if len(name) == 4 and not name.isdigit():  #O(N)
            newlist.append(name)     #O(1)
    return newlist
            
print(friend(["Ryan", "Kieran", "Jason", "Yous,","1234"]))  