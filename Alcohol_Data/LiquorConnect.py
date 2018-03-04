from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import TimeoutException
import time
import json
import csv

def get_ids(skus, link, num):

    driver = webdriver.Chrome()
    filters = "#k=#s=" + str(num)
    driver.get(link + filters)
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    # gets the total count of the items in the category
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, """// *[ @ id = "ResultCount"]""")))
    count = driver.find_element_by_xpath("""// *[ @ id = "ResultCount"]""").text.strip().split()[1].replace(',', '')

    sku_drivers = driver.find_elements_by_class_name("productItem")

    for j in sku_drivers:
        id = j.get_attribute("id")
        skus.append(id)

    driver.quit()

    return count

def make_csv(skus):
    with open("alcohol_data.csv", "w", newline='') as csvfile:
        fieldnames = ["ID", "Name", "Maker", "Category", "Sub_Category", "Sub_Sub_Category", "Sub_Sub_Sub_Category"
            , "Cost", "Volume(ml)", "Alcohol_By_Volume", "Aroma", "Color", "Deposit", "Origin", "Region"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        retry_skus = []
        for i in range(len(skus)):
            time.sleep(1)
            try:
                url = "http://www.liquorconnect.com/Products/_vti_bin/iomer.LC.WcfServices/Products.svc/GetProduct?sku=" + skus[i]
                r1 = requests.get(url)
                data = json.loads(r1.content)

                # name of the alcohol
                name = data["Product"]["Title"]
                if(name != "" and name != None):
                    name = name.strip()
                # producer
                maker = data["Product"]["AgentName"]
                if(maker != "" and maker != None):
                    maker = maker.strip()
                # alcohol category
                cat = data["Product"]["WineCategory"]
                if(cat != "" and cat != None):
                    cat = cat.strip()
                sub_cat = data["Product"]["WineType"]
                if(sub_cat != "" and sub_cat != None):
                    sub_cat = sub_cat.strip()
                sub_sub_cat = data["Product"]["WineSubtype"]
                if(sub_sub_cat != "" and sub_sub_cat != None):
                    sub_sub_cat = sub_sub_cat.strip()
                sub_sub_sub_cat = data["Product"]["WineSubSubType"]
                if(sub_sub_sub_cat != "" and sub_sub_sub_cat != None):
                    sub_sub_sub_cat = sub_sub_sub_cat.strip()
                # cost per unit
                cost = data["Product"]["UnitCost"]
                # amount per bottle
                units = float(data["Product"]["UnitsPerPack"])
                volume = int(data["Product"]["UnitSize"])
                if(units != 0 and units != None):
                    volume /= units
                # alcohol by voluume
                abv = data["Product"]["AlcoholByVolume"]
                # aroma
                aroma = data["Product"]["Aroma"]
                if(aroma != "" and aroma != None):
                    aroma = aroma.strip()
                # color
                color = data["Product"]["Colour"]
                if(color != "" and color != None):
                    color = color.strip()
                # i.e. CA refund amount
                deposit = data["Product"]["Deposit"]
                # location of origin
                origin = data["Product"]["Origin"]
                if(origin != "" and origin != None):
                    origin = origin.strip()
                region = data["Product"]["Region"]
                if(region != "" and region != None):
                    region = region.strip()

                # write all the above keys to the csv
                writer.writerow({"ID" : skus[i], "Name" : name, "Maker" : maker, "Category" : cat, "Sub_Category" : sub_cat,
                                 "Sub_Sub_Category" : sub_sub_cat, "Sub_Sub_Sub_Category" : sub_sub_sub_cat, "Cost" : cost,
                                 "Volume(ml)" : volume, "Alcohol_By_Volume" : abv, "Aroma" : aroma, "Color" : color,
                                 "Deposit" : deposit, "Origin" : origin, "Region" : region})
            except:
                print(f"Error: Unable to get data for {skus[i]}.")
                retry_skus.append(skus[i])

        # uncomment to see all the available keys
        # for key,value in data.items():
        #
        #     if (type(value) == dict):
        #         print(f"\tStart {value}'s dict: ")
        #         for key1, value1 in value.items():
        #             print(f"{key1}: {value1}")
        #         print(f"\tEnd of {value}'s dict\n")
        #     else:
        #         print(f"{key}: {value}")

def retry_csv(retry_skus):
    with open("alcohol_data.csv", "a", newline='') as csvfile:
        fieldnames = ["ID", "Name", "Maker", "Category", "Sub_Category", "Sub_Sub_Category", "Sub_Sub_Sub_Category"
            , "Cost", "Volume(ml)", "Alcohol_By_Volume", "Aroma", "Color", "Deposit", "Origin", "Region"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        retry_skus = []
        for i in range(len(retry_skus)):
            time.sleep(1)
            try:
                url = "http://www.liquorconnect.com/Products/_vti_bin/iomer.LC.WcfServices/Products.svc/GetProduct?sku=" + retry_skus[i]
                r1 = requests.get(url)
                data = json.loads(r1.content)

                # name of the alcohol
                name = data["Product"]["Title"]
                if(name != "" and name != None):
                    name = name.strip()
                # producer
                maker = data["Product"]["AgentName"]
                if(maker != "" and maker != None):
                    maker = maker.strip()
                # alcohol category
                cat = data["Product"]["WineCategory"]
                if(cat != "" and cat != None):
                    cat = cat.strip()
                sub_cat = data["Product"]["WineType"]
                if(sub_cat != "" and sub_cat != None):
                    sub_cat = sub_cat.strip()
                sub_sub_cat = data["Product"]["WineSubtype"]
                if(sub_sub_cat != "" and sub_sub_cat != None):
                    sub_sub_cat = sub_sub_cat.strip()
                sub_sub_sub_cat = data["Product"]["WineSubSubType"]
                if(sub_sub_sub_cat != "" and sub_sub_sub_cat != None):
                    sub_sub_sub_cat = sub_sub_sub_cat.strip()
                # cost per unit
                cost = data["Product"]["UnitCost"]
                # amount per bottle
                units = float(data["Product"]["UnitsPerPack"])
                volume = int(data["Product"]["UnitSize"])
                if(units != 0 and units != None):
                    volume /= units
                # alcohol by voluume
                abv = data["Product"]["AlcoholByVolume"]
                # aroma
                aroma = data["Product"]["Aroma"]
                if(aroma != "" and aroma != None):
                    aroma = aroma.strip()
                # color
                color = data["Product"]["Colour"]
                if(color != "" and color != None):
                    color = color.strip()
                # i.e. CA refund amount
                deposit = data["Product"]["Deposit"]
                # location of origin
                origin = data["Product"]["Origin"]
                if(origin != "" and origin != None):
                    origin = origin.strip()
                region = data["Product"]["Region"]
                if(region != "" and region != None):
                    region = region.strip()

                # write all the above keys to the csv
                writer.writerow({"ID" : retry_skus[i], "Name" : name, "Maker" : maker, "Category" : cat, "Sub_Category" : sub_cat,
                                 "Sub_Sub_Category" : sub_sub_cat, "Sub_Sub_Sub_Category" : sub_sub_sub_cat, "Cost" : cost,
                                 "Volume(ml)" : volume, "Alcohol_By_Volume" : abv, "Aroma" : aroma, "Color" : color,
                                 "Deposit" : deposit, "Origin" : origin, "Region" : region})
            except:
                print(f"Error: Unable to get data for {retry_skus[i]}.")




def main():

    # the main page of the site
    r = requests.get("http://www.liquorconnect.com/Pages/default.aspx")
    soup = BeautifulSoup(r.content, "lxml")

    skus = []
    # gets all the category hyperlinks
    cats = soup.find_all("div", id="Value")
    for i in range(1, len(cats)-1):
        cat_link = "http://www.liquorconnect.com" + cats[i].find('a').get("href")
        print(cat_link)

        # runs through all of the pages per category and gets all the skus/ids
        count = int(get_ids(skus, cat_link, 1))
        for j in range(19, 36, 18):
            time.sleep(2)
            get_ids(skus, cat_link, j)

    # makes the csv
    make_csv(skus)

if __name__ == "__main__":
    main()
