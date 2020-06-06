from urllib.request import urlopen 

html = urlopen("https://recursospython.com/guias-y-manuales/argumentos-args-kwargs/")

print(html.read())
