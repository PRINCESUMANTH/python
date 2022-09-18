#pytho program to split string list of k character

v=int(input())
strlist = ["sumanth", "ajhsbsb", "skjdjdjh"]
newstrlist = []
k = []
count = 0
t = 0
value = ''
value1= []
temp = 0
new_k = []
for i in strlist:
    for j in i:
        k.append(j)
print(k)
# print(newstrlist)

for i in k:
    value = value + i
    temp += 1
    if temp==v:
        value1.append(value + ",")
       # print(value)
        value=''
        temp=0
print(value1)
