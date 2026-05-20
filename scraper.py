import requests
import json
import time
import pandas as pd
import os
import re
import math

query = input("Enter a product to search.").lower()
page = 1
link = "https://www.daraz.com.np/catalog/"

products = []
product_no = 9999

def get_page(query, page, retries = 3):

    params = {
    "ajax": "true",
    "isFirstRequest": "true",
    "page": page,
    "q": query
    }

    for r in range(retries):
        try:
            response = requests.get(link, params=params, timeout = 10)
            response.raise_for_status()
            return response
        except Exception as e:
            print(f"Failed {r} attempt in page {page} due to Error: {e}")
        time.sleep(3)
    return None



while True:

    response = get_page(query, page)
    if response is None:
        print(f"No response on page {page}.")
    data = response.json()

    if "captcha" in str(data).lower() or not data.get("mods"):
        print(f"Captcha or bad response on page {page}, stopping.")
        break
    if data is None:
        break
    
    if page == 1:
        try:
            product_no_string = data["mods"]["resultTips"]["tips"]
            product_no = int(re.findall(r'\d+', product_no_string)[0])
            print(f"Total number of items: {product_no}")
        except KeyError:
            print("No items available.") 

    try:
        items = data["mods"]["listItems"]
    except:
        print(f"JS error encountered on page {page}.")
        break
    for item in items:
        products.append({"Name":item["name"], "Price":item["price"], "Rating":item["ratingScore"], "Seller":item["sellerName"], "Link": item["itemUrl"]})
    print(f"Page number : {page}")
    
    if page == math.ceil(product_no/40):
        break
    else:
        page += 1

    time.sleep(5)

df = pd.DataFrame(products)
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce').round(1)
file_path = "results.xlsx"
mode = 'a' if os.path.exists(file_path) else 'w'
if_sheet_exists = 'replace' if mode == 'a' else None

with pd.ExcelWriter(file_path, mode=mode, if_sheet_exists=if_sheet_exists) as writer:
    df.to_excel(writer, sheet_name=f"{query}_result", index=False)

print(f"Executed succesfully. {product_no} products found.")