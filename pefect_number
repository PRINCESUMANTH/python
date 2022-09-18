#perfect number
#perfect number means sum of factors of a number is equal to that number
number=input("Enter a number to check perfect or not : ")
if number.isdigit() and int(number)>0:
    number=int(number)
    sum=0
    for i in range(1,number):
        if number%i==0:
            sum+=i
    if sum==number:
        print(number,"is a perfect number")
    else:
         print(number,"is not a perfect number")
else:
    print("Enter only positive integer greater than zero")
