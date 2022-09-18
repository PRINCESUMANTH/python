#python to remove duplicate in a list of elements



l=[1,24, 54,54,2,1,58, 9,9,5,1,6,88,9, 5,4,11,2, 3,1,1,5,3,8,8,6,51,4, 5,32,36, 51,51,4,1]
t=[]
v=set(l )
print (v)
for i in l:
    if i in t:
       l.remove(i)
    else:
       t.append(i)
print(l)
