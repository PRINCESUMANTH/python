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
