import os
import json
import requests
from bs4 import BeautifulSoup


GOOGLE_IMAGE = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=900&'

usr_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Enconding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive',
        }

SAVE_FOLDER = 'images'


def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    download_images()


def download_images():
    data = input("what kind of data do you want? ")
    n_images = int(input("how many images do you want?"))
    print('stat searching your images...')

    searchurl = GOOGLE_IMAGE + 'q=' + data.replace(" ","+")
    print(searchurl)

#    response = requests.get(searchurl, headers=usr_agent)
#    html = response.text
#
#    soup = BeautifulSoup(html, 'html.parser')
#    results = soup.findAll('div', {'class':'v4dQwb'}, limit=n_images)
#    imagelink = []
#    for result in results:
#        text = result.text
#        print(text)
#
if __name__ == '__main__':
    main()
