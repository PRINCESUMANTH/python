 
number=6
temporary=0
def perfect (number):
  for i in range(1, number):
    if (a%i==0):
      temporary=temporary+i
    if (temporary==a):
      return "is a perfect number"
    else:
      return "is not a perfect number"
print(number, perfect (number):


 
a=100
t=0
for i in range(1,a):
  if (a%i==0):
    t=t+i
if (t==a):
  print(a,"is a perfect number")
else:
  print(a,"is not a perfect number")



 
number=6
def perfect (number):
    temporary=0
    for i in range(1, number):
        if (number%i==0):
            temporary=temporary+i
    if (temporary==number):
        return "is a perfect number"
    else:
        return "is not a perfect number"
print(number,perfect(number))




 
def function (number):
  temp=0
  temp = temp%10
  if (temp>number):
    return temp
    n=number/10
    function (n)
t=[]
final_number=int(input("enter number"))
t=function(6544)
for i in t:
  l[i]=i*3
temporary=0
for i in t:
  temporary=temporary+l[i]
print(temporary)
if (temporary==final_number):
  print(final_number,"is an angstrom number")
else :
  print(final_number,"is not an angstrom number")



 
for i in range(1,10):
    for j in range(1,i):
        print(j,end="")
    print()



 
for i in range(1,10):
    for j in range(i):
        print(i,end="")
    print()



 
#take given number as n to check prime or not
#check by dividing given number with number which are lessthan given number i.e n/2
#for i in range(1,n/2+1)
    #if n%i==0:
        #count = count + 1
#if count == 2:
    #print (prime number)
#else :
    #print( not prime number)


t=int(input("enter a number to chech prime or not "))
count=0
for i in range(1,int(t/2)+1):
    if t%i==0:
        count = count + 1
        print(count)
if count == 1:
    print (t,"is a prime number")
else :
    print(t,"is not prime number")




 
#take given number as n to check prime or not
#check by dividing given number with number which are lessthan given number i.e n/2
#for i in range(1,n/2+1)
    #if n%i==0:
        #count = count + 1
#if count == 2:
    #print (prime number)
#else :
    #print( not prime number)


#t=int(input("enter a number to chech prime or not "))

def prime(number):
    t=number
    count=0
    for i in range(1,int(t/2)+1):
        if t%i==0:
            count = count + 1
       # print(count)
    if count == 1:
            print (t,"is a prime number")
    else :
            print(t,"is not prime number")
    

t=[]
for i in range(1,100):
    prime(i)



 
#take a number from user as n to check the given number is strong number or not.
# divid the number n into individual digits
#find the factors of individual number n0,N1,...
# factor def fact(num):
    #if (num==1):
       # return t
       # break
    #t=(num-1)*fact(num)
#given number n divid into single digits
    #while(number>0):
        #rem=number%10
        #temp=temp+fact(rem)
        #rem=int(number/10)

number1=number=int(input ("Enter a number to check strong number or not \n"))
rem=temp=variable=0
def fact(rem):
    variable=0
    if(rem==1 or rem ==0):
        print(variable)
        return variable
    print (variable)
    variable=(rem)*fact(rem-1)
while (number>0):
    rem=number%10
    temp=temp+fact(rem)
    rem=int(number/10)
"""def fact(rem):
    if(rem==1 or rem ==0):
        print(variable)
        return variable
    print (variable)
    variable=(rem)*fact(rem-1)"""
if(temp==number1):
    print(number1,"is a strong number")
else :
    print(number1,"is not a strong number")






 
for i in range(10):
    if(i==0 or i==9):
        print("*"," "*13,"*"," "*3,"*"*12)
    else :
        print("*"," "*i,"*"," "*(10-i),"*"," "*2,"*"," "*10,"*")

    


#Print NO with stars




 
#size =size of an arry
size=int(input ("Enter length of an array \t"))
#list of array elements
list=[]
list=input("Enter array elements"). split (" ")
k=int(input ("Enter key element"))
print(list)
list2=[int(j) for j in list]
print(list2)
length=len(list)
list1=[]
temp=0    
for i in list2:
    
    if((i+k)==(length-3)):
        temp1=length-3
        i==temp1
        list[temp1+k]=i
    else :
        list[i+k]=i
print(list)







 
#size =size of an arry
size=int(input ("Enter length of an array \t"))
#list of array elements
list=[]
list=input("Enter array elements"). split (" ")
k=int(input ("Enter key element"))
print(list)
list2=[int(j) for j in list]
print(list2)
length=len(list)
list1=[]
temp=temp1=0    
for i in list2:
    
    if((temp+k)>=(length-3)):
        temp1=length-3
        temp==temp1
        list[temp+k]=i
        temp==temp-temp1
    else :
        list[temp+k]=i
    temp+=1
print(list1)





 
#size =size of an arry
size=int(input ("Enter length of an array \t"))
#list of array elements
list=[]
list=input("Enter array elements"). split (" ")
k=int(input ("Enter key element"))
print(list)
list2=[int(j) for j in list]
print(list2)
length=len(list)
list1=[]
temp=temp1=0
for i in list2:
    for j in range(5):
        if (j<=(k-1)):
            list1[j+k]=i
        else :
            if(j>k):
                list1[j-(k-1)]=i
        break
print(list1)
#print(list1)
#print (list2)






 
#size =size of an arry
size=int(input ("Enter length of an array \t"))
#list of array elements
list=[]
list=input("Enter array elements"). split (" ")
k=int(input ("Enter key element"))
print(list)
list2=[int(j) for j in list]
print(list2)
length=len(list)
list1=[]
temp=temp1=0
for i in list2:
    for j in range(5):
        if (j<=(k-1)):
            list1[j+k]=i
        else :
            if(j>k):
                list1[j-(k-1)]=i
        break
print(list1)
#print(list1)
#print (list2)






 
#size =size of an arry
size=int(input ("Enter length of an array \t"))
#list of array elements
list=[]
list=input("Enter array elements"). split (" ")
k=int(input ("Enter key element"))
print(list)
list2=[int(j) for j in list]
print(list2)
length=len(list)
list1=[]
j=temp=t=0
for i in list2:
    if (j+k<=length):
        if (j<=k):
            t=j+k
            list1[t]=i
        else :
            temp=length-(j+k)
            list1[temp]=i
    j+=1
print(list1)
#print(list1)
#print (list2)





 
def calculation(variable):
    rem=number=0
    while (variable>0):
        if (variable>0):
            rem=i%10
            number=int(i/10)
            break
    return number^rem
total=int(input("enter range"))
sum=0
for i in range(total):
    variable=int(input ("Enter value"))
    sum=sum+calculation (variable)
print(sum)




 
def calculation(variable):
    rem=number=0
    while (variable>0):
        if (variable>0):
            rem=variable%10
            number=int(variable/10)
          #  print (rem, number)
            break
    return number**rem
total=int(input("enter range"))
sum1=sum=0
for i in range(total):
    variable=int(input ("Enter value"))
    sum=calculation (variable)
    sum1=sum1+sum
print(sum1)



 
'''def count1(k,r):
    k=k.count("K")
    r=k.count("R")
    k=k+r.count("K")
    r=r+r.count("R")
    return (k,r)
    for i in k:
        if i in k:
            t=t+1
        else :
            j=j+1
    return i,j'''
total=int(input())
for i in range(total-1):
    k,r=input().split (",")
   # t=count1(k,r)
temp=count=0
for i in k:
    if i=="K":
        count=count+1
    else :
        temp=temp+1
for i in r:
    if i =="K":
        count=count+1
    else :
        temp=temp+1
print(count,temp)






 
def calculation(variable):
    rem=number=0
    while (variable>0):
        if (variable>0):
            rem=variable%10
            number=int(variable/10)
          #  print (rem, number)
            break
    return number**rem
total=int(input("enter range"))
sum1=sum=0
for i in range(total):
    variable=int(input ("Enter value"))
    sum=calculation (variable)
    sum1=sum1+sum
print(sum1)











 
'''
total=int(input())
temp=count=0
t=1
while(t<=(total)):
    k=input()
    #r=input ()
    for i in k:
        if i=="K":
           count=count+1
        else :
           temp=temp+1
    t=t+1
    for i in r:
    if i =="K":
        count=count+1
    else :
        temp=temp+1
print(count,temp)
'''
total=int(input())
temp=count=0
t=1
while(t<=(total)):
    k=input()
    #r=input ()
    for i in k:
        if i=="K":
           count=count+1
        else :
           temp=temp+1
    t=t+1
    
'''for i in r:
    if i =="K":
        count=count+1
    else :
        temp=temp+1'''
print(count,temp)





 
x,y,z=10,20,30
if(x>y):
    if(x>z and x>y):
        print("x is greater")
elif(y>z):
        print("y is greater")
else :
    print("z is greater")




 
a=eval(input("enter a values"))
b=int(input("enter b values"))
c=int(input("enter c values"))
if ((a<b) and (b<c) or (a>b) and (b>c)):
    print(b)
elif(a>c) or (c>a):
         if (a>c):
             print(a)
         else:
             print(c)
else:
   print("number is not same to another")







 
n=4
s=0
j=1
while(n>=j):
    if(n%j==0):
        s+=1
    j+=1    
if (s==2):
   print("prime")
else:
   print("not prime")





 
str=input()
sub=input()
count=str.count(sub)
t=str[-1::-1]
print(count,t)










 
t=eval(input())
set=set(t)
tuple=tuple(set)
print(tuple)






 
n =int(input())
dict1={}

for i in range(n):
    dict1['name']=eval((input())
    dict1['rollno']=eval(input())
    dict1['mobile']=eval(input())
print(dict)







 
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)








 
n =int(input())
dict1={}
j=("name","rollno","mobile","address")
for i in range(n):
    for k in j:
        dict1[k]=input(k)
print(dict1)



 
a=['a', 'b', 'c','d']
print(len(a))
print(a[-1::-1])
a.reverse()
print(a)










 
# ptyhon program to interchange frist and last element in a list
list=[1,2,3,4,5,6]
print(list)
print("to interchange frist and last element in a list is:")
total=len(list)
#print(total)
varibale=list[(total-1)]
temp=list[0]
list[0]=varibale
list[total-1]=temp
print(list)









 
#python program to swap two elements in a list
print("swap elemnts at your requried position of list of elements ")
list=[]
list= input("enter list elememts by seperating with commo of each element").split(",")
list=[int(i) for i in list]
frist =int(input("position frist :"))
second=int(input("position second:"))

length=len(list)
temp=variable=0
temp=list[frist-1]
variable=list[second-1]
list[frist-1]=variable
list[second-1]=temp
print(list)








 
#to find maximum of two number of a given list
def maximum(number):
    frist=0
    last=0
    for i in number:
        if i>frist or i>last:
            last=frist
            frist=i
  
    return frist,last
print(maximum((3,6,4,9,8,2,1,5)))







 
#to find maximum of two number of a given list
def maximum(i,number):
    
    frist=i
    last=i
    for i in number:
        if i<frist or i<last:
            last=frist
            frist=i
  
    return frist,last
i=int(input("max"))
print(maximum(i,(3,6,4,9,8,2,1,5)))







 
#python way to check if an element present in list or not
def find1(find,number):
    for i in number:
        if i==find:
            return True 
find=int(input("number"))
print(find1(find,(1,2,5,6,5,8,9,10)))







 
#python way to check if an element present in list or not
def find1(find,number):
    for i in number:
        if i==find:
            return True 
find=int(input("number"))
print(find1(find,(1,2,5,6,5,8,9,10)))


'''
simple way to find if an element present in list or not 

in Operator is used to check if an element present or not 


number=(1,2,5,6,5,8,9,10)
print(find in number)
'''










 
#different ways to delete a list

#3 ways we can delete a list in python they are 1) del 2) remove () 3) pop ()


#del operation is used to delete all the list of elements
t=[1,2,5,6,5,8,9,10]
print(t)
del(t)
#print (t)

# remove function is used to remove only one element in a list

t=[1,2,5,6,5,8,9,10]
print(t)
for i in t:
    print(t)
    t.remove(i)
print(t)

#pop function is used to delete last element and return 
t=[1,2,5,6,5,8,9,10]
print(t)
for i in t:
    print(t.pop())
print(t)













 
#python reversing a list 
#for loop used to reverse a list element

t=[1,2,5,6,5,8,9,10]
c=[]
for i in t[::-1]:
    c.append(i)
print(t)
print(c)

#used slicing to reverse a list element

print(t[::-1])

#reversing a string 

t="sumanth"
for i in t[::-1]:
    print (i)










 
#python clone or copy a list 


t=[1,2,5,6,5,8,9,10]
c=t.copy()
print(c)


#python program to count no of occurrence of an element in a list

for i in t:
    print(t.count(i))









 
#python program sum of number of digits in a list of elements

def sum(number):
    rem=temp=0
    l=[]
    for i in number:
        total=0
        while i>0:
            rem=i%10
            total=total+rem
            i=i//10
        l.append(total)
    return l
s=[244,556,145,856,588,258,416,485]
print(sum(s))
print(s)









 
#python program sum of number of digits in a list of elements

def sum(number):
    rem=temp=count=0
    l=[]
    for i in number:
        total=0
        while i>0:
            rem=i%10
            total=total+rem
            count+=1
            i=i//10
        l.append(total)
    return l,count
s=[244,556,145,856,588,258,416,485]
print(sum(s))
print(s)







 
#python program sum of total individual number of digits in a list of elements

def sum(number):
    rem=temp=count=0
    l=[]
    for i in number:
        total=0
        while i>0:
            rem=i%10
            total=total+rem
            count+=1
            i=i//10
        l.append(total)
    return l,count
s=[244,556,145,856,588,258,416,485]
print(sum(s))
print(s)









 
#python program to find sum and average of a list 
t=[24,56,15,86,58,28,16,85]
total=len(t)
sum=average=0
for i in t:
    sum+=i
average=sum/total
print("sum:",sum)
print ("average:",average)







 
#python program to find sum and average of a list 
t=[24,56,15,86,58,28,16,85]
total=len(t)
sum=average=1
for i in t:
    sum*=i
average=sum/total
print("multiply:",sum)
#print ("average:",average)










 
#python program to find sum and average of a list 
t=[24,56,15,86,58,28,16,85]
total=len(t)
sum=average=1
for i in t:
    sum*=i
average=sum/total
print("multiply:",sum)
#print ("average:",average)









 
#python program to find the smallest number and largest number

#for to find  smallest number in a list
t=[15,55,55,8,888,5,56]
temp=0
for i in t:
    if i>temp:
        temp=i
print(temp)

#for to find largest number in a list

temp=99999999
for i in t:
    if i<temp:
        temp=i
print(temp







 
#python program to print 2 largest number
t=[15,55,55,8,888,5,56]
temp=99999999
for i in t:
    if i<temp:
        temp=i
print(i)










 
#python program to print even and odd number of a given list and even and odd in a range 

even=[]
odd=[]
print("in range")
for i in range(1,10):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

l=[1,2,68,6,4,5,65,45,55,95,94,465,245,55]
print ("in list")
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)










 
#python program to print even and odd number of a given list and even and odd in a range 

even=[]
odd=[]
print("in range")
for i in range(1,10):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)

l=[1,2,68,6,4,5,65,45,55,95,94,465,245,55]
print ("in list")
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)



#python program to count even and odd of a given list of elements



l=[1,2,68,6,4,5,65,45,55,95,94,465,245,55]
print ("in count")
counte=counto=0
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
        counte+=1
        
    else:
        odd.append(i)
        counto+=1
print(even,counte)
print(odd,counto)









 
#python program to print positive numbers in a range
positive=[]
negative=[]
for i in range(-10,10):
    if i>0:
        print("positive number",i)
        positive.append(i)
    else :
        if (i<0):
            print ("negative  number",i)
            negative.append(i)
print(positive)
print(negative)

#python program to print given list of elements
l=[2,5,43,8,46,5,58,8,53,-6,-68,-688,-688,-58,-68,-98,-64]
positive=[]
negative=[]
for i in l:
    if i>0:
        print("positive number",i)
        positive.append(i)
    else :
        if (i<0):
            print ("negative  number",i)
            negative.append(i)
print(positive)
print(negative)









 
#python program to print positive numbers in a range
positive=[]
negative=[]
for i in range(-10,10):
    if i>0:
        print("positive number",i)
        positive.append(i)
    else :
        if (i<0):
            print ("negative  number",i)
            negative.append(i)
print(positive)
print(negative)

#python program to print given list of elements
l=[2,5,43,8,46,5,58,8,53,-6,-68,-688,-688,-58,-68,-98,-64]
count=0
coun=0
positive=[]
negative=[]
for i in l:
    if i>0:
        print("positive number",i)
        positive.append(i)
        count+=1
    else :
        if (i<0):
            print ("negative  number",i)
            negative.append(i)
            coun+=1
print(positive)
print (count)
print(negative)
print (coun)








 
#python to remove duplicate in the given list
list=[]
l=[3,4,5,8,6,8,34,8,653,68,855,655]
for i in l:
    if i in list:
         l.remove(i)
    else :
        list.append(i)
print (list)

t=()
print (t is tuple)








 
#python program to remove empty tuple in a list 



l=[1,(),2,3,4,5,(),6,()]
t=()
for i in l:
    if type(i) is tuple:
        if i is t:
            l.remove(i)
print(l)


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








 
#python program to remove empty tuple in a list 



l=[1,(),2,3,4,5,(),6,()]
t=()
for i in l:
    if type(i) is tuple:
        if i is t:
            l.remove(i)
print(l)


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










 
#python program to reverse all the string list

def strlist(list):
    listq=[]
    for i in list:
        listq.append(i[::-1])
    return listq
print(strlist(["Suman","kajal","krishna"]))







 
#python program character position bof kth work of a string list
strlist=input("").split(" ")
kth_position=eval(input())
charlist=[]
for i in strlist:
    charlist.append(list([i]))
print(charlist[kth_position-1])







 
#python program to find the character position kth work of a string list 
strlist=input("").split(" ")
kth_position=eval(input())
charlist=[]
for i in strlist:
    charlist.append(list([i]))
print(charlist[kth_position-1])








 
#python program to prefix frequency of a string list
str_frequency=["sumanth","summu","sana","nara","suni","suri","subbu"]           
#input (). split (",")
prefix_work="su"
#input()
temp=0
for i in str_frequency:
    if prefix_work in i:
        for j in i:
            if prefix_work in i[0: len(prefix_work)]:
                print(i)
                temp+=1
                break
print("prefix frequency:",temp)









 
#python program extract work with start with k
list=["sumanth","summu","sana","nara","suni","suri","subbu"] 
k="n"  
for i in list:
    if i.startswith(k):
        print(i)






 
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









 
#python program to prefix frequency of a string list
str_frequency=["sumanth","summu","sana","nara","suni","suri","subbu"]           
#input (). split (",")
prefix_work="su"
#input()
temp=0
new_list=[]
for i in str_frequency:
    if prefix_work in i:
      #  for j in i:
        if prefix_work in i[0: len(prefix_work)]:
                new_list.append(i[0:len(prefix_work)]+","+i[len(prefix_work):])
                
                
                print(new_list)
                temp+=1
#print("prefix frequency:",temp)
print(new_list)






 
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






 
#python program to validate the password
def password_validation(string):
    if len(string)>=4:
        print ("len okay") 
        pass
    else :
        return 0
    t=0
    for i in string:
        if i.isupper():
            t=1
    if t==1:
        print ("upper okay") 
        pass
    else :
        return 0
    t=0
    if string[0].isnumeric():
        #t=1
        return 0
        pass

        
    else :
        print ("1numb okay") 
        #return 1
    if len(string)>=4:
        #t=1
        pass
        print ("len okay") 
    else :
        return 0
    t=0
    for i in string:
        if i.isnumeric():
            t=1
    if t==1:
        pass
        print ("isnumb okay") 
    else :
        return 0
    t=0
    for i in string:
        if i==' ' or i=='/':
            t=1
    if t==1:
        return 0
    else:
        print ("space okay") 
        return 1
print(password_validation("Sumanth766"))






 
#python program to find the max number index 


def max_index(arr,n):
    temp=0
    index=0
    for i in range(n):
        if arr[i]>temp:
            temp=arr[i]
            index=i
            #index=findIndexof(i)
    print(temp,index)
arr=(1,2,3,4,5,6)
n=6
max_index(arr,n)






 
#python program to convert number to  alphabet 
def function(arr):
    for i in arr:
         i=int(i)
        # print (i)
         print(chr(i),end="")
t=[]
t=input (). split (" ")
#print (t)
function(t)





 
#python program to print random

import random as r
t=r.randint(2,100)
print (t)

#python program to find area of triangle

a=22
b=10
print((a*b)/2)



 
#Remove words containing list characters
string=[]
list=[]
string=input().split(" ")
list=input().split(" ")
temp=""
for i in list:
 if i in list:
  string.remove(i)
print(string)
print(string,list)







 
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







 
#Python  program for convert charachers of a matrix to single string
matrix=[[1,2,3,4,5],[6,7,8,9]]
string=""
for i in matrix:
 i=str(i)
 for j in i:
  string=string+j
print(string)






 
#python program filter the list contains the given substring


string=[]
string=input().split(" ")
substring=input()
filter_string=[]
for i in string:
 if i in substring:
  filter_string.append(i)
print(filter_string)






 
#python program to print string by removing substring word in a string

substring=[]
string=[]
string=input(). split (" ")
substring=input(). split (" ")
for i in string:
    for j in substring:
        if i in j:
            string.remove(i)
print (string)










 
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





 
#test if substring occurs in specific position or not 

string=[]
substring=[]
index=int(input("index"))
string=input("string: "). split (" ")
substring=input("substring ")
if string[index]==substring:
    print ("found")
else :
    print("not found")






 
#count strings with substring string list
count =0
string=[]
string=input("string: "). split (" ")
substring=input ()
for i in string:
    if i in substring:
        count+=1
print(count)





 
#Group sublist by another list

list=[]
sublist=[]
sublist=input ().split(" ")
for i in sublist:
    list.append(i)
print(list







 
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









 
#python program to print reverse of a word and frist letter is captial
word=[]
word=input().split (" ")
word1=""
for i in word:
    i=i[::-1]
    word1=word1+i+" "
word1=word1.title()
print(word1)






   
#Remove words containing list characters
string=[]
list=[]
string=input().split(" ")
list=input().split(" ")
temp=""
for i in list:
 if i in list:
  string.remove(i)
print(string)
print(string,list)




   
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







   
#Python  program for convert charachers of a matrix to single string
matrix=[[1,2,3,4,5],[6,7,8,9]]
string=""
for i in matrix:
 i=str(i)
 for j in i:
  string=string+j
print(string)







   
#python program to print string by removing substring word in a string

substring=[]
string=[]
string=input(). split (" ")
substring=input(). split (" ")
for i in string:
    for j in substring:
        if i in j:
            string.remove(i)
print (string)








   
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






   
#test if substring occurs in specific position or not 

string=[]
substring=[]
index=int(input("index"))
string=input("string: "). split (" ")
substring=input("substring ")
if string[index]==substring:
    print ("found")
else :
    print("not found")







   
#count strings with substring string list
count =0
string=[]
string=input("string: "). split (" ")
substring=input ()
for i in string:
    if i in substring:
        count+=1
print(count)







   
#Group sublist by another list

list=[]
sublist=[]
sublist=input ().split(" ")
for i in sublist:
    list.append(i)
print(list











   
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







   
#python program to print reverse of a word and frist letter is captial
word=[]
word=input().split (" ")
word1=""
for i in word:
    i=i[::-1]
    word1=word1+i+" "
word1=word1.title()
print(word1)






Problem Statement
You are given an array of integers 'ARR' of length 'N' and an integer Target. Your task is to return all pairs of elements such that they add up to Target.
Note:
We cannot use the element at a given index twice.
Follow Up:
Try to do this problem in O(N) time complexity. 
Input Format:
The first line of input contains an integer ‘T’ denoting the number of test cases to run. Then the test case follows.

The first line of each test case contains two single space-separated integers ‘N’ and ‘Target’ denoting the number of elements in an array and the Target, respectively.

The second line of each test case contains ‘N’ single space-separated integers, denoting the elements of the array.
Output Format :
For each test case, print a single line containing space-separated integers denoting all pairs of elements such that they add up to the target. A pair (a, b) and (b, a) is the same, so you can print it in any order.

Each pair must be printed in a new line. If no valid pair exists, print a pair of (-1, -1). Refer to sample input/output for more clarity.
Note:
You do not need to print anything; it has already been taken care of. Just implement the given function.
Constraints:
1 <= T <= 100
1 <= N <= 5000
-10 ^ 9 <= TARGET <=10 ^ 9
-10 ^ 9 <= ARR[i] <=10 ^ 9

Where 'T' denotes the number of test cases, 'N' represents the size of the array, 'TARGET' represents the sum required, and 'ARR[i]' represents array elements.

Time Limit: 1 sec.
Sample Input 1 :
2
4 9
2 7 11 13
5 1
1 -1 -1 2 2
Sample Output 1:
2 7
-1 2
-1 2
Explanation For Sample 1:
For the first test case, we can see that the sum of  2 and 7 is equal to 9 and it is the only valid pair.

For the second test case, there are two valid pairs (-1,2) and (-1,2), which add up to 1.
Sample Input 2 :
1
4 16
2 7 11 13
Sample Output 2 :
-1 -1
Previous
Next
1



def twoSum(arr, target, n):
    # Write your code here.
    list=[]
    for i in range(n):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                list.append((arr[i],arr[j]))
    return list

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    print(ans)
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))
t=int(input())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)










#python program for tic tac Toe game
sucess=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
temp=0
for i in range(3):
    for j in range (3):
        temp+=1
        print (temp," | ",end="")
    print ()
    print ("-"*14)
print ("SELECT NUMBER TO PLAY THE GAME ")
list=[[" "," "," "],[" "," "," "],[" "," "," "]]
for i in range(3):
    for j in range (3):
        print (list[i][j]," | ",end="")
    print ()
    print ("-"*14)
    
while (True):
    l=int(input("CHOICE :"))
     
    list.append(l)
    temp=0
    
    for i in range(3):
        for j in range (3):
            temp+=1
            if temp==l:
                list[i][j]="X"
                print (list[i][j],"| ",end="")
            else :
                print (list[i][j],"| ",end="")        
        print ()
        print ("-"*10)
        for i in sucess:
            if l in i:
                list=i
        for i in list:
            print (i not in list)












for i in range(1,201):
  if i>1:
    for j in range(2,i):
      if i%j==0:
        break
    else:
       print(i)









 
#print all prime numbers
for j in range (2,201):
    for i in range(2,j):
        if j%i==0:
            break
    else:
        print (j)








 
#print all prime numbers
count=0
for j in range (2,201):
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        print(j)  
        count=0








 
I#print all prime numbers

for j in range (2,201):
    count=0 
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        print(j) 
    count=0











 
a=[3, 2, 5, 10, 7]
n=5
max=0

for i in range (0,n):
    total=a[i]
    k=i+2
    for j in range (k,n,2):
        total=total+a[j]
    if max<total:
        max=total
print (max)









 
a=[3, 2, 7, 10]
#a=[5, 5, 10, 100, 10, 5]
#a=[3, 2, 5, 10, 7]
n=4
max=0
for i in range (0,n):
    total=a[i]
    k=i+2
    for j in range (k,n,2):
        total=total+a[j]
    if max<total:
        max=total
print (max)








 
#a=[3, 2, 7, 10]
#a=[5, 5, 10, 100, 10, 5]
#a=[3, 2, 5, 10, 7]
n=6
max=0
for i in range (0,n):
    total=a[i]
    k=i+2
    for j in range (k,n):
        total=total+a[j]
        if max<total:
            max=total
            j=j+2
print (max)









 
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.


class Solution(object):
    def isValid(self, s):
        count=0
        if len(s)%2==0 or len(s)==1:
            pass
        else:
            return False
        for i in range (len(s)):
            
            if s[i]=="(":
                if s[i+1]==")":
                    count=1
                else:
                    count=0
            if s[i]=="{":
                if s[i+1]=="}":

                    count=1

                else:

                    count=0
            if s[i]=="[":

                if s[i+1]=="]":

                    count=1

                else:

                    count=0
            if count==1:
                return True 
            else :
                return False
t=Solution ()
print (t.isValid("(]"))








 
#print all prime numbers

for j in range (2,201):
    count=0 
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        print(j,"is a prime") 
        count=0
    else:
     print(j,"not a prime")







 
for i in range (2,101):
 for j in range (2,i):
  if i%j==0:
   print(i,"not a prime")
   break
 else:
  print(i, "is a prime")








a="234"#"8765498"
if a.isdecimal():
    print("correct gentleman")
if a.isdigit():
    print("correct gentleman")
if a.isdecimal():
    print("correct gentleman")
else:
    print("you done! a small mistake gentleman")









 
import numpy as np
n=np.array([1,2,3,4,5])
print(n)
a=numpy.array([1,2,3,4,5])
print(a)








 
import numpy as np
n=np.array([1,2,3,4,5])
print(n)

a=[1,2,3,4,5]
square=[print(x**2) for x in a if type(x)==int]
print (square)
print(print (help(type(print()))))



'''

a=numpy.array([1,2,3,4,5])
print(a)

'''






















































































































































































































































