#Hold space between potensial words
potensial=[]
potensial1=[]
potensial=input().split(" ")
substring=""
for i in potensial:
 for j in i:
  if  j.isupper():
   substring=substring+ " "+j
  else :
   substring=substring+j
 potensial1.append(substring)
 substring=""
print(potensial1)
