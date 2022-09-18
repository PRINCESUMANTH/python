#python program replace all the character of a list except given character

import random 
strlist = ["sumanth", "ajhsbsb", "skjdjdjhs"]
character="s"
new_list=[]
number=[97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]
for i in strlist:
    for j in i:
        if j != character:
            if j!=chr(random.choice(number)):
                new_list.append(chr(random.choice(number)))
        else:
             new_list.append(j) 
print(strlist)
print (new_list)
