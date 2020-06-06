from urllib.request import urlopen 
from urllib.error import HTTPError
from bs4 import BeautifulSoup

##we are going through exceptions with "try" and "except", we should be careful with the exceptions
##then we'll return the variable in each function
def getBody(url):
    try:
        html = urlopen(url)
    except httperror as e:
        return none

    try: 
        bsobj = BeautifulSoup(html.read())

        body_html = bsobj.body 
    except AttributError as e:
        return none
    return body_html
## the same function as the last one, but in this case we return the title of our website

def getTitle(url):
    try:
        html = urlopen(url)
    except httperror as e:
        return none

    try: 
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributError as e:
        return none
    return title 

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
body = getBody("http://www.pythonscraping.com/pages/page1.html")

if title == None: 
    print("Title not found")
else:
    print(title)
    
if body == None:
    print("Body with issues ")
else: 
    print(body)






