#Largest of three Numbers
a=int(input())
b=int(input())
c=int(input())
if (a>b) and (a>c):
    print("a is greater")
elif (b>a)and(b>c):
    print("b is greater")
else:
    print("c is greater")