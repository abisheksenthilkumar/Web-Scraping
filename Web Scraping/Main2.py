import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Specifications = []
Ratings = []

for i in range(2, 12):
    url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

    if box:
        names = box.find_all("div", class_="_4rR01T")
        prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
        spec = box.find_all("ul", class_="_1xgFaf")
        ratings = box.find_all("div", class_="_3LWZlK")

        # Ensure all arrays have the same length
        min_length = min(len(names), len(prices), len(spec), len(ratings))

        # Append only up to the minimum length
        Product_name.extend([name.text.strip() for name in names[:min_length]])
        Prices.extend([price.text.strip() for price in prices[:min_length]])
        Specifications.extend([s.text.strip() for s in spec[:min_length]])
        Ratings.extend([rating.text.strip() if rating else "-" for rating in ratings[:min_length]])

print("Length of Product_name:", len(Product_name))
print("Length of Prices:", len(Prices))
print("Length of Specifications:", len(Specifications))
print("Length of Ratings:", len(Ratings))

# Create DataFrame
df = pd.DataFrame({"Product Name": Product_name, "Prices": Prices, "Specifications": Specifications, "Ratings": Ratings})
print(df)

# Save to CSV
df.to_csv("C:/Users/abish/Desktop/flipkart_laptops.csv", index=False)
