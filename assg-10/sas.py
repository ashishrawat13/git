f = open('wow1.txt', 'r+')
F = open('wow2.txt', 'r+')
g = open('wow3.txt', 'w')
lines = f.readlines()
lines1 = F.readlines()
lines2 = list()
print(lines)
print(lines1)
if len(lines) > len(lines1):
    for i in range(0, len(lines1)):
        lines2.append(lines[i] + lines1[i])
    for i in range(len(lines1), len(lines)):
        lines2.append(lines[i])
else:
    for i in range(0, len(lines)):
        lines2.append(lines[i] + lines1[i])
    for i in range(len(lines), len(lines1)):
        lines2.append(lines1[i])
for i in range(0, len(lines2)):
    lines2[i] = lines2[i].replace('\n', ' ')
    g.writelines(lines2[i] + '\n')

f.close()
F.close()
g.close()
