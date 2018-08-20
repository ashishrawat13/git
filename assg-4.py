#ques_1.
a=[4,5,7,8,9]
a.reverse()
print(a)
#ques_2.
b=input()
z=''
for i in range(0,len(b)):
    if b[i].isupper()==True:
        z=z+b[i]
print(z)
#ques_3.
a=[]
a=input()
b=[]
for i in a:
    b.append(int(i))
print(b)
#ques_4.
a=input()
c=a.split(",")
b=a[::-1]
#d=''.join(b)
print(a)
print(b)
if(a==b):
    print("true")
else:
     print("false")
#ques_5.
import copy as c
l=[1,2,[4,5],6]
l1=c.deepcopy(l)
l[2][1]=8
print(l)
print(l1)
#a shallow copy doesnt create a copy of nested objects,instead it just copies the refrence of nested objects.this means,a copy process does not create copies nested object itself
# deep copy creates a new object and recursively adds the copies of nested objects present in the original elements
