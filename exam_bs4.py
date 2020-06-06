#we are importing some libraries, and from them taking some constructors 

from urllib.request import urlopen 
from bs4 import BeautifulSoup
#we store the request into "html" variable
html = urlopen("https://recursospython.com/guias-y-manuales/argumentos-args-kwargs/")
#in our variable "bsObj" we are using BS to parse the output
bsObj = BeautifulSoup(html.read())
#we print only "h1" of our output of the request to the server
print(bsObj.h1)

print(bsObj.body)
