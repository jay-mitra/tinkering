#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup as Soup

url = "https://en.wikipedia.org/wiki/List_of_craters_on_the_Moon"
# use requests to get the url
response = requests.get(url)
# get the content from the response
content = response.content
# parse the content with soup
soup = Soup(content, 'lxml')

# look at the web page source and find out the container for the information we want
# each crater is stored in a div that has the class 'gallerybox'
# tell soup to get the div gallerybox
all_gallerybox = soup.find_all("li", "gallerybox")
# print (all_gallerybox[0])

# crater name and crater diameter are inside a div that has the class 'gallerytext'
# tell soup to get the div gallerytext from div gallerybox
all_gallerytext = soup.find_all("div", "gallerytext")
# print (all_gallerytext[0])

# crater name is the string of an anchor tag that is inside a div that has a class 'gallerytext'
# tell soup to get the anchor tag from div gallerytext
crater_names = []
for line in all_gallerytext:
    name = line.find("a")
    if name is not None:
        crater_names.extend(name)
print ("crater_names")
print (crater_names[0])

# crater diameter is the string of a span tag that is inside a div that has class 'gallerytext'
# tell soup to get the span tag from div gallerytext
crater_diameters = []
for line in all_gallerytext:
    span = line.find("span")
    if span is not None:
        crater_diameters.append(span.string)
print ("crater_diameters")
print (crater_diameters[0])

# crater thumbnail is inside of the div that has the class 'thumb'
# tell soup to get the div thumb from div gallerybox
all_thumbnails = []
for line in all_gallerybox:
    thumb = line.find("div", attrs={'class': 'thumb'})
    if thumb is not None:
        all_thumbnails.append(thumb)
print ("all_thumbnails")
print (all_thumbnails[0])

# crater thumbnail source is the 'src' key inside the 'attrs' dictionary of the img tag from div thumb
# tell soup to get the img tag from div thumb
thumbnails = []
for thumb in all_thumbnails:
    image = thumb.find("img")
    link = image.get("src")
    if link is not None:
        thumbnails.append(link)
print ("thumbnails")
print (thumbnails[0])

#store name = diameter or name = thumbnail in a dictionary
dict_craters = {}
counter = 0
for crater in crater_names:
    dict_craters[crater] = crater_diameters[counter]
    counter += 1

# print dictionary key/value to a file as two columns separated by a comma
with open("output.txt", "w") as outfile:
    for crater, diameter in dict_craters.items():
        outfile.writelines("{},{}".format(crater, diameter))
        outfile.write("\n")
