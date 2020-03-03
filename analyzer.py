from urllib.request import urlopen
from urllib.error import HTTPError

from bs4 import BeautifulSoup

url = input("Which page will you like to check? Enter URL:")

try:
    html = urlopen(url)
except HTTPError as e:
    print(e)

data = BeautifulSoup(html, "html.parser")

url = ["title_tag", "meta_description", "canonical_tag"]
for element in url:
    print("Page is SEO friendly")
else:
    print("Page is not SEO friendly")
