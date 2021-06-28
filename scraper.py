from bs4 import BeautifulSoup

html = open("product_category.html")

soup = BeautifulSoup(html, 'lxml')

sft_prices = soup.findAll('span', class_='price-label 999')
sft_names_links = soup.findAll('h2',class_='product-name')

prices = []
links = []
names = []

for sft_price in sft_prices:
	#tmep = sft_price
	prices.append(sft_price.span.text)

for sft_name_link in sft_names_links:
	names.append(sft_name_link.text.strip())
	links.append(sft_name_link.a['href'])

links.remove('https://ryanscomputers.com/panda-internet-security-1user-with-speaker.html')
names.remove("Panda Internet Security 1User with Speaker");

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