from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

n = int(16044/2)

for i in range(0, 1000):
    url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={n}"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    x = re.findall("next nothing is [0-9]+", text)
    k = str(x[0])
    y = re.findall("[0-9]+", k)
    n = y[0]

    print(text)
    print(n)
