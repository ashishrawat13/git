#ques_1.
a=3
if a<4:
    try:
        a=a/(a-3)
    except ZeroDivisionError as message:
     print('Exception:', message)
print(a)
#ques_2.
l=[1,2,3]
try:
 print(l[3])
except IndexError as msg:
     print(msg)
#ques_3.
# ANS->  the output will be exception but during runtime error will occur in last line due to raise statement
#ques_4.
#output of this code will be
# ANS-> -5.0 (return float value because of else)
#       a/b result in 0  (error occurs because of zerodivision)
#ques_5.
#import error
try:
    from .arawat import*
except ImportError as mset:
    print(mset)

#value error
try:
    a=int(input())
except ValueError as msg:
    print(msg)
else:
    print(a)
#index error
l=[18,23,31]
try:
 a=int(input("Enter the number to check in list"))
 for i in l:
     a==l[i]
except ValueError as ms:
    print(ms)
except IndexError as msg:
     print(msg)
