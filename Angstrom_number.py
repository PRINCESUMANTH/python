#number, variable are assigned as given numbe
#rem store remainder
#temp store resultant of individual number cude
     
number=variable=int(input("Enter number to chech angstrom number are not "))
rem=0
temp=0
while (number>0):
    rem=number%10
  #  print (rem,"rem")
    temp=temp+rem*rem*rem
   # print(temp,"temp")
    number=int(number/10)
#print(temp, variable)
if (variable==temp):
    print (variable,"is a angstrom number")
else :
    print (variable,"is not a angstrom number")
