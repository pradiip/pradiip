x1,x2,x3=input().split()
x1,x2,x3=int(x1),int(x2),int(x3)
if(x1>x2 and x1>x3):
  print(x1)
elif(x2>x3):
  print(x2)
else:
  print(x3)
