#to display the number in place of alphabet
while (1):
    number=input("\nEnter a number"). split(" ")
    i=len(number)
    if (i==4):
        for i in number:
            print(ord(i)," ",end="")
        break
    else :
        print ()
        print ("you enter more than 4 letters please enter 4 letters")
        
