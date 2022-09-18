#Armstrong number
#Armstrong number means sum of indivisal number cube of a number is equal the number
number=input("Enter a number to check Armstrong or not : ")
if number.isdigit() and int(number)>0:
    sum=0
    for i in number:
        sum+=int(i)**len(number)
    if sum==int(number):
        print(number,"is a armstrong number")
    else:
         print(number,"is not a armstrong number")
else:
    print("Enter only positive integer greater than zero")
    
    
    
n = int(input('enter the number:'))
y = n
r1 = 0
s = len(str(n))
while n >0:
	r = n %10
	r1 = r1 + r**s
	n = n //10
if r1 == y:
	print('armstrong number')
else:
	print('not a armstrong number')
