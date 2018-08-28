#ques_1.
f = open('ad.txt','r')

data = f.read()

print(data)

f.close()

#ques_2.
word=input("Enter word to be searched:")
k = 0
with open('as.txt', 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            if(i==word):
                k=k+1
print("Occurrences of the word:")
print(k)
#ques_3.
with open("as.txt") as f:
    with open("ad.txt", "w") as f1:
        for line in f:
            f1.write(line)
#ques_4.
f = open('wow1.txt', 'r+')
F = open('wow2.txt', 'r+')
g = open('wow3.txt', 'w')
l = f.readlines()
l1 = F.readlines()
l2 = list()
print(l)
print(l1)
if len(l) > len(l1):
    for i in range(0, len(l1)):
        l2.append(l[i] + l1[i])
    for i in range(len(l), len(l)):
        l2.append(l[i])
else:
    for i in range(0, len(l)):
        l2.append(l[i] + l1[i])
    for i in range(len(l), len(l1)):
        l2.append(l1[i])
for i in range(0, len(l2)):
    l2[i] = l2[i].replace(' ')
    g.writelines(l2[i] + '\n')
f.close()
F.close()
g.close()
#ques_5.
f=open('a1.txt')
g=open('a3.txt','w')
lines=f.readlines()
for i in range(0,len(lines)):
    lines[i]=int(lines[i])
lines=sorted(lines)
print(lines)
for i in range(0,len(lines)):
    lines[i]=str(lines[i])
    g.writelines(lines[i]+'\n')
g.close()
    

