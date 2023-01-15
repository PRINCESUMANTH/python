# python program for tic tac Toe game
print("WLECOME TO TIC TAC TOE GAME")
name=input("ENTER YOUR NAME: ")
sucess = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]#WINNING OUTCOMES
temp = 0
#DECLARING THE TEMPLET OF THE TIC TAC TOE GAME
for i in range(3):
    for j in range(3):
        temp += 1
        print(temp, " | ", end="")
    print()
    print("-" * 14)
print("SELECT NUMBER TO PLAY THE GAME ")
list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]#DELCARING EMPTY LIST
for i in range(3):
    for j in range(3):
        print(list[i][j], " | ", end="")
    print()
    print("-" * 14)
check=[]
person1_list=[]
person2_list=[]
s=0
checklist=[]
u1=[]
c1=[]



while (True):
    if s==1:
        break

    l = int(input("CHOICE :"))

    #CHECKING THE ELEMENT ALREADY HAVE OR NOT
    if l in check:
        print("!ALERT PLEASE ENTER CORRECT ONE")
        continue
    else:
        check.append(l)
        person1_list.append(l)

    #ADDING USER INPUT
    temp = 0
    for i in range(3):
        for j in range(3):
            temp += 1
            if temp == l:
                list[i][j] = "X"

    #COMPUTER INPUT .....WHICH SELECT AN ELEMANT RANDOMLY
    temp=0
    for i in sucess:
        for j in i:
            if j==l:
                checklist+=i
    for i in checklist:
        if i not in check:
            if i!=l:
                aponent=i
                check.append(aponent)
                person2_list.append(aponent)
                break
    #ADDING COMPUTER INPUT TO THE TIC TAC TOE GAME
    temp = 0
    for i in range(3):
        for j in range(3):
            temp += 1
            if temp == aponent:
                list[i][j] = "O"

    #DISPLAY THE TIC TAC TOE GAME
    temp=0
    for i in range(3):
        for j in range(3):
            print(list[i][j], "| ", end="")
        print()
        print("-" * 10)

    #TAKING DECISION BASED ON THE GIVEN INPUT VALUE OF USER AND COMPUTER
    person1_list.sort()
    person2_list.sort()
    if len(person2_list)>=3:
        #CALCULATING USER CORRECT STEPS FOR SUCESS
        for i in sucess:
            if person1_list==i :
                print(name, "YOU WON THE MATCH")
                s=1
                break
            else:
                if len(person1_list)>3:
                    for j in i:
                        if j in person1_list:
                            u1.append(j)
                    for i in sucess:
                        if i==u1.sort():
                            print(name, "WON THE MATCH.....BETTER LUCK NEXT TIME")
                            s = 1
                            break
            #CALCULATING COMPUTER CORRECT STPES FOR SUCESS
            if person2_list==i :
                print("COMPUTER WON THE MATCH")
                s = 1
            else:
                if len(person2_list)>3:
                    for j in i:
                        if j in person2_list:
                            c1.append(j)
                    for i in sucess:
                        if i == c1.sort():
                            print("COMPUTER WON THE MATCH")
                            s = 1
                            break
    #DECLATING DRAW MATCH
    if len(check)==9:
        print('MATCH DRAW')
        s=1
