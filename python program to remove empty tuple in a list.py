#python program to remove empty tuple in a list 



l=[1,(),2,3,4,5,(),6,()]
t=()
for i in l:
    if type(i) is tuple:
        if i is t:
            l.remove(i)
print(l)
