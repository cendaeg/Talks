import requests
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/watch?v=SV-cgdobtTA&list=PL37ZVnwpeshG2YXJkun_lyNTtM-Qb3MKa'

data = requests.get(url)
data = data.text
soup = BeautifulSoup(data)

h4 = soup.find_all("h4")
for h in h4:
    print(h.text)
