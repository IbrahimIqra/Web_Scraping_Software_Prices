from bs4 import BeautifulSoup

html = open("ms_store.html")

soup = BeautifulSoup(html, 'lxml')

sft_names = soup.findAll('h3',class_='c-subheading-6')
sft_prices = soup.findAll('span', itemprop='price')
sft_links = soup.findAll('div',class_='m-channel-placement-item')

names = []
prices = []
links = []

for sft_name in sft_names:
	names.append(sft_name.text.strip())

for sft_price in sft_prices:
	prices.append(sft_price.text)

for sft_link in sft_links:
	link = sft_link.a['href']
	link = "https://www.microsoft.com"+link
	links.append(link)

print(len(names))
print(len(prices))
print(len(links))

for i in range(len(names)):
	print(names[i]+"\n"+prices[i]+"\n"+links[i])
	print()

filename = "web_scrapped2.csv"

f = open(filename, 'w')

headers = "Software, Price, Link\n"

f.write(headers)

for i in range(len(names)):
	name = names[i]
	price = prices[i]
	link = links[i]

	name = name.replace("," , "/")
	#price = price.replace("," , "")

	f.write(name+ "," +price+"," +link+ "\n")

f.close()