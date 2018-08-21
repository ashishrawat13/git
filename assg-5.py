#ques_1.
a=int(input("enter the year "))
if a%4==0:
    print("Its a leap year")
else:
    print("Not a leap year")
#ques_2.
a=int(input("enter the length "))
b=int(input("enter the breadth "))
if a==b:
    print("square")
else:
    print("rectangle")

#ques_3.
l=[]
for i in range(0,3):
    x=input()
    l.append(int(x))
l.sort()
print("max",l[-1],"min",l[0])
#ques_4.
age=int(input("Enter age\n"))
sex=input("M or F\n")
mar=input("Y or N\n")
if sex=="F":
    print("Urban area")
elif age>20 and <40:
    print("Anywhere")
elif age>40 and <60:
    print("urban area")
else:
    print("error")
#ques_5.
a=int(input("Enter the quantity "))
if a>1000:
    a=a-(a/100)
else:
    print("Not enough quantity")
print(a)
#LOOPS
#ques_1.
a=[]
for i in range(0,10):
    z=input()
    a.append(int(z))
print(a)
#ques_2
num=int(input())
while num%1==0:
    print("*")
#ques_3.
a=[]
b=[]
c=int(input("NO of elements "))
for i in range(0,c):
    z=int(input())
    a.append(z)
    b.append(z*z)
print(b)
#ques_4.
a=['a',12,3.14,'ac',345];
b=[];
c=[];
d=[];
for i in a:
    if type(i)==int:
        b.append(i)
    elif type(i)==float:
        c.append(i)
    elif type(i)==str:
        d.append(i)
print(a)
print(b)
print(c)
print(d)
#ques_5.
a=[]
for i in range(1,101):
    for z in range(2,i):
        if i%z!=0:
            a.append(i)
        break
print(a)    
#ques_6.
a=int(input())
for i in range(0,a):
    print("\r")
    for j in range(0,i+1):
        print("*",end=" ")
#ques_7.
a=[]
b=int(input("ENTER NO OF ELEMENTS "))
for i in range(0,b):
    z=int(input())
    a.append(z)
c=int(input("ENTER THE NO YOU WANT TO DELETE "))
for t in range(0,b):
     if c==t:
         a.remove(t)
print(a)

         
