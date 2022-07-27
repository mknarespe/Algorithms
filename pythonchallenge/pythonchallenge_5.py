
from urllib.request import urlopen
import pickle

with urlopen('http://www.pythonchallenge.com/pc/def/banner.p') as f:
    data = pickle.load(f)
for i in data:
    for j in i:
        print(j[0] * j[1], end='')
    print('')
