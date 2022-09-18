#Replace substring from string list
string=[]
#substring=[]
temp=0
string=input("string: ").split (" ")
substring, replace=input("substring: ").split (" ")
length=len(string)
for i in string:
    if temp==length:
        break
    temp+=1
  #  for j in substring:
    if i==substring:
        string[temp-1]=replace
print(string)
