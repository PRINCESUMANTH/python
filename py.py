a=100
t=0
for i in range(1,a):
  if (a%i==0):
    t=t+i
if (t==a):
  print(a,"is a perfect number")
else:
  print(a,"is not a perfect number")