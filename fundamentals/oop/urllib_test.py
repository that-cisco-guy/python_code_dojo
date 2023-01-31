import urllib.request
response = urllib.request.urlopen ('http://codingdojo.com')
html = response.read()
print(html)