from bs4 import BeautifulSoup as bs
import requests

search = input("Enter the topic to be searched: ")
words_limit = int(input("Total no. of words: "))

url = "https://en.wikipedia.org/wiki/" + search
data = requests.get(url)
soup = bs(data.text, 'html.parser')

pre_len = 0
length = 0

for para in soup.find_all('p'):
    pre_len = length
    s = para.text
    length = length + len(s.split())
    print(length)
    if length > words_limit:
        req_len = words_limit - pre_len
        print(" ".join(s.split()[:req_len]))
        break
    print(s)
