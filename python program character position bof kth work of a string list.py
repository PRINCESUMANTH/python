#python program character position bof kth work of a string list
strlist=input("").split(" ")
kth_position=eval(input())
charlist=[]
for i in strlist:
    charlist.append(list([i]))
print(charlist[kth_position-1])
