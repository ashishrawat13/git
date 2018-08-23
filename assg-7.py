#ques_1.
age=int(input("enter age to find "))
l={'ashish':20,'arunesh':21,'bidesh':19,'ashwani':22}
for k,j in l.items():
    if j==age:
     print(k)
#ques_2.
students = {'ashwani': {'english': 20, 'maths': 40, 'science': 60},
          'vishwajeet': {'english': 30, 'maths': 50, 'science': 70},
         'arsh': {'english': 89, 'maths': 78, 'science': 88},
         'rawat': {'english': 45, 'maths': 55, 'science': 75}}
name=input('enter name \n')
for n,s in students.items():
        if name==n:
            print("\nName",n)
            for marks in s:
                print(marks+':',s[marks])

