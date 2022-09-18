#python program to reverse all the string list

def strlist(list):
    listq=[]
    for i in list:
        listq.append(i[::-1])
    return listq
print(strlist(["Suman","kajal","krishna"]))
