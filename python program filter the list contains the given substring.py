#python program filter the list contains the given substring


string=[]
string=input().split(" ")
substring=input()
filter_string=[]
for i in string:
 if i in substring:
  filter_string.append(i)
print(filter_string)
