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
    

    
    
