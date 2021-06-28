from bs4 import BeautifulSoup

html = open("makeuseof.html")

soup = BeautifulSoup(html, 'lxml')

sft_names_links = soup.findAll('h2')
sft_prices = soup.findAll('strong')

names = []
prices = []
links = []

for sft_price in sft_prices:
	prices.append(sft_price.text)

for sft_name_link in sft_names_links:
	names.append(sft_name_link.a.text.strip())
	links.append(sft_name_link.a['href'])

print(len(names))
print(len(prices))
print(len(links))

for i in range(len(names)):
	print(names[i]+"\n"+prices[i]+"\n"+links[i])
	print()

filename = "web_scrapped2.csv"

f = open(filename, 'a')

#headers = "Software, Price, Link\n"

#f.write(headers)

for i in range(len(names)):
	name = names[i]
	price = prices[i]
	link = links[i]

	name = name.replace("," , "/")
	price = price.replace("," , "")

	f.write(name+ "," +price+"," +link+ "\n")

f.close()