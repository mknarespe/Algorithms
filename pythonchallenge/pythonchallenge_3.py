import re

with open('/files/3.txt') as f:
    lines = f.readlines()

s = ''
for line in lines:
    s += line.rstrip()

x = re.findall("[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]", s)

print(x)

answer = ''
for s in x:
    answer += s[4]

print(answer)
