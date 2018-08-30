#ques_1.
import re
e=input("enter email address\n")
matcher = re.finditer('^\w[_a-zA-Z0-9.]*(@)(gmail.com|yahoo.com)$',e)
count=0
for m in matcher:
    count += 1
if count>0:
    print('{} is a Valid email address'.format(e))
else:
    print('{} is NOT a Valid email address'.format(e))

#ques_2.
no=input("enter mobile no\n")
matcher = re.finditer('^[+]91[-][6-9][0-9]{9}$',no)
count=0
for m in matcher:
    count += 1
if count>0:
    print('{} is a Valid INDIAN number'.format(no))
else:
    print('{} is NOT a Valid INDIAN number'.format(no))
