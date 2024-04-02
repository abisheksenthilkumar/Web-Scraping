import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Specifications = []
Ratings = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=" + str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    if box:
        names = box.find_all("div", class_="_4rR01T")
        for i in names:
            name = i.text
            Product_name.append(name)

        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        for i in prices:
            name = i.text
            if name.startswith('â‚'):
                name = 'Rs. ' + name[1:]  # Replace â‚¹ with Rs.
            Prices.append(name)

        spec = box.find_all("ul", class_="_1xgFaf")
        for i in spec:
            name = i.text
            Specifications.append(name)

        ratings = box.find_all("div", class_="_3LWZlK")
        for i in ratings:
            name = i.text
            Ratings.append(name)

print("Length of Product_name:", len(Product_name))
print("Length of Prices:", len(Prices))
print("Length of Specifications:", len(Specifications))
print("Length of Ratings:", len(Ratings))

df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Specifications": Specifications, "Ratings": Ratings})
print(df)

df.to_csv("C:/Users/abish/Desktop/flipkart_laptops.csv", encoding='utf-8-sig', index=False)
