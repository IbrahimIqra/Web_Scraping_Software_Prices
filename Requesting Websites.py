from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

soft_url = "https://ryanscomputers.com/software.html"

#uReq is urlopen
soft_html = uReq(soft_url)
raw_html = soft_html.read()
soft_html.close()

page_soup = soup(raw_html, "html.parser")

page_soup.prettify()

contaiers = page_soup.findAll("div",{"class":"post-body"})

print(page_soup)