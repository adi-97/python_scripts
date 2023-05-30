#usr/bin/python3
"""
This code snippet is used to scrap data from pharmeasy webpages using beautifulsoup
"""
import requests
import warnings
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
lst=[]
for i in range(1,150000):
    URL = "https://pharmeasy.in/online-medicine-order/"+str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="__next")
    results=results.find_all("div", class_="MedicineOverviewSection_medicineUnitContainer__F6ZV_")
    dict1={}
    for i in results:
        dict1['name']=i.find("h1",class_="MedicineOverviewSection_medicineName__dHDQi")
        dict1['brand_name']=i.find("div",class_="MedicineOverviewSection_brandName__rJFzE")
        dict1['packaging']=i.find("div",class_="MedicineOverviewSection_measurementUnit__7m5C3")
        dict1['mrp']=i.find("div",class_="PriceInfo_originalMrp__z1_NV")
        dict1['discounted_price']=i.find("div",class_="PriceInfo_ourPrice__jFYXr")
    for key in dict1.keys():
        if dict1[key]!=None:
            dict1[key]=dict1[key].text
    dict1["URL"]=URL
    lst.append(dict1)
    
    pd.DataFrame(lst).to_csv("pharmeasy.csv",index=False)
    sleep(3)
