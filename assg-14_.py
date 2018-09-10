#LIST COMPREHENSION & GENERATOR EXPRESSION

#Q.1- Write a python program to print the cube of each value of a list using list comprehension.
l=[2,3,4]
d=[o**3 for o in l]
print(d)

#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
p=[j for j in range (2,101) if all(j%i!=0 for i in range (2,j))]
print(p)
#Q.3- Write the main differences between List Comprehension and Generator Expression.
'''
A List Comprehension executes immediately and returns a list.
A Generator Expression returns and object that can be iterated over.
The comparision is not perfect though, because in an object returned by the generator expression, we cannot access an element by index.
The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets []
while the Generator expression is enclosed in plain parentheses ().
Generator takes less memory
'''
#LAMBDA & MAP

#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit=list(map(lambda x: 9/5*x+32,Celsius))
print(Fahrenheit)
   
#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
l1=[1,2,3,4,5]
d=list(map(lambda x : x*x,l1))
print(d)

#FILTER & REDUCE


#Q.1- Filter out all the primes from a list.
l2=[2,3,4,5,6,7,8,9,10,11,12,13,14,15]
di=list(filter(lambda x : all(x%i != 0 for i in range (2,x)),l2))
print(di)


#Q.2- Write a python program to multiply all the elements of a list using reduce.
from functools import reduce
l3=[1,3,5,7]
b=reduce(lambda x,y: x*y,l3)
print(b)
