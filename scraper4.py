from bs4 import BeautifulSoup

html = open("newegg.html")

soup = BeautifulSoup(html, 'lxml')

sft_names_links = soup.findAll('a', class_ = 'item-title')
sft_prices = soup.findAll('li', class_ = 'price-current')

#print("$"+sft_prices[1].strong+sft_prices[1].sup)

names = []
prices = []
links = []

for sft_name_link in sft_names_links:
	names.append(sft_name_link.text.strip())
	links.append(sft_name_link['href'])

for sft_price in sft_prices:
	if sft_price.strong is not None:
		prices.append("$"+sft_price.strong.text+sft_price.sup.text)

names.remove("Microsoft Office Home and Business 2019 | 1 device, Windows 10 PC/Mac Key Card");
links.remove("https://www.newegg.com/microsoft-office-home-and-business-2019-1-pc-mac/p/N82E16832011399?Item=N82E16832011399")

names.remove("CyberLink PowerDVD 19 Ultra")
links.remove("https://www.newegg.com/cyberlink-dvd-ej00-rpu0-00-ultra-version/p/N82E16832117102?Item=N82E16832117102")

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