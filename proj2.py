#proj2.py

import requests
from bs4 import BeautifulSoup

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

base_url = 'http://www.nytimes.com'
r = requests.get(base_url, headers = {'User-Agent': 'SI_CLASS'})
soup = BeautifulSoup(r.text, 'html.parser')  # returns as html

for story_heading in soup.find_all(class_="story-heading", limit=10):  #for item in list of 10
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url = 'https://www.michigandaily.com/'
r = requests.get(base_url,  headers = {'User-Agent': 'SI_CLASS'})
soup = BeautifulSoup(r.text, 'html.parser')  # returns as html

for tag in soup.find_all("div", class_="panel-pane pane-mostread"):
    for mostread in tag.find_all('li'):
        print(mostread.a.text.replace("\n", " ").strip())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url,  headers = {'User-Agent': 'SI_CLASS'})
soup = BeautifulSoup(r.text, 'html.parser')

for i in soup.find_all("img"):   # find_all returns a list
    if i.get('alt'):
        print(i.get("alt"))
    else:
        print("No alternative text provided!")


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
base_url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4"
params = {'page': 0}
r = requests.get(base_url, params = params,  headers = {'User-Agent': 'SI_CLASS'})  # headers fixes something about bots I don't understand
soup = BeautifulSoup(r.text, 'html.parser')

# create list of hrefs to prof pages
proflist = []   # list of links formatted \node\###

for page in range(6):  # only because I know that there are 6 pages to page thru
    r = requests.get(base_url, params = params,  headers = {'User-Agent': 'SI_CLASS'})  # headers fixes something about bots I don't understand
    soup = BeautifulSoup(r.text, 'html.parser')
    for tag in soup.find_all("div", class_ = "field field-name-contact-details field-type-ds field-label-hidden"):
        for prof in tag.find_all("a"):
            proflist.append(prof.attrs['href'])
    params['page'] += 1
# extract emails from individual prof pages
base_url = "https://www.si.umich.edu"
# https://www.si.umich.edu/node/9899

acc = 1
for prof in proflist:
    r = requests.get(base_url + prof, headers = {'User-Agent': 'SI_CLASS'})  # headers fixes something about bots I don't understand
    soup = BeautifulSoup(r.text, 'html.parser')
    for tag in soup.find_all("div", class_ = "field field-name-field-person-email field-type-email field-label-inline clearfix"):
        for tag in tag.find_all("a"):
            print(str(acc) + " " + tag.text)
    acc += 1

### Help understanding attributes in BeautifulSoup
# data = '''<div class="image">
#         <a href="http://www.example.com/eg1">Content1<img
#         src="http://image.example.com/img1.jpg" /></a>
#         </div>
#         <div class="image">
#         <a href="http://www.example.com/eg2">Content2<img
#         src="http://image.example.com/img2.jpg" /> </a>
#         </div>'''
#
# soup = BeautifulSoup(data, "html.parser")
#
# for div in soup.findAll('div', attrs={'class':'image'}):
#     print (div.find('a')['href'])
#     print (div.find('a').contents[0])
#     print (div.find('img')['src'])
#     print('\n nextdiv: \n')

# Expected output:
# http://www.example.com/eg1
# Content1
# http://image.example.com/img1.jpg
#  nextdiv:
# http://www.example.com/eg2
# Content2
# http://image.example.com/img2.jpg
#
