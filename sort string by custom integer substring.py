#sort string by custom integer substring

sort_string=[]
string=[]
substring=[]
integer=eval(input("int : "))
string=input("string: "). split (" ")
for i in range(1,integer+1):
    t=input("substring: {}".format(i))
    substring.append(t)
for j in string:
    if j in substring:
        sort_string.append(j)
print(sort_string)
