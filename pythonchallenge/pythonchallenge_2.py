import string

with open('/pythonchallenge/files/2.txt') as f:
    lines = f.readlines()

s = ''
for line in lines:
    s += line.rstrip()

for char in string.punctuation:
    s = s.replace(char, '')

print(s)
