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
