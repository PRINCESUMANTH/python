
#python program for insertion sort

n=5
list=[3,2,5,4,1,9,8,7]
list1=list.sort()
temp=0
def fun(list,n):
    for i in range(n-1):
        for j in range (1,n):
            if list[i]>list[i+1]:
                temp=list[i+1]
                list[i+1]=list[i]
                list[i]=temp
            else :
                if list1==list:
                    return list
                else :
                    fun(list,n)
                
print (list )
