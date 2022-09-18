
#python program to print reverse of a word and frist letter is captial
word=[]
word=input().split (" ")
word1=""
for i in word:
    i=i[::-1]
    word1=word1+i+" "
word1=word1.title()
print(word1)
