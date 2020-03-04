import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'lxml')

result = soup.find_all("li", "gallerybox")

result_list = []
for line in result:
    tag = line.find("div", "gallerytext")
    if tag is not None:
        print (tag.text.strip())
