#ques_1.
a=int(input())
def area(a):
    ar=12.56*a*a
    print(ar)
area(a)
#ques_2.
def perf(n):
    j=0
    for i in range(1,n):
     if n%i=0:
         j=j+1
    if n==j:
        print(n)
for n in range (1,1000):
    perf(n)
#ques_3.
a=int(input())
def mult(a):
    for i in range (1,11):
     print(a,"X",i,a*i,"")
mult(a)
#ques_4.
a=int(input())
b=int(input())
def pow(a,b):
    if b==1:
        return a
    else:
        return(a*pow(a,b-1))
print(pow(a,b))


    
