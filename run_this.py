import requests
from time import sleep
import pandas as pd

with open("api_key.txt","r") as f:
    api_key=f.read()









def ListingToFacebookCsv(shop_string,api_key,brand_string,output_path="facebook_listing.csv",sku_base="duck",condition="new"):

    got_all=False
    per_call=100
    page=1
    
    column_names=["id","title","description","availability","condition","price","link","image_link","brand","additional_image_link"]
    image_urls=[]
    additional_image_urls=[]
    titles=[]
    descriptions=[]
    prices=[]
    listing_urls=[]
    def fix_ascii(input_string):
        return input_string.replace("&#39;",r"'")
    while not got_all:
        sleep(0.11) #so no more that 10 calls per second
        print(f"Parsing listing of shop: {shop_string}, page: {page}")
        response = requests.get(f"https://openapi.etsy.com/v2/shops/{etsystore}/listings/active?limit={per_call}&includes=Images&page={page}&api_key={api_key}").json()
        page+=1
        # count = response["count"]
        listings= response["results"]
        for listing in listings:
            listing_urls.append(listing["url"])
            image_urls.append(listing["Images"][0]["url_fullxfull"])
            # try:
            #     additional_image_urls.append(listing["Images"][1]["url_fullxfull"])
            # except :
            #     additional_image_urls.append(None)
            #     print(listing["title"] + " has only one image")
            extra_images_string=""
            for x in listing["Images"][1:]:
                extra_images_string+=x["url_fullxfull"]+","
            additional_image_urls.append(extra_images_string[:-1])
            titles.append(listing["title"])
            descriptions.append(listing["description"])
            prices.append(listing["price"]+" USD")

        if 100 != len(listings):
            got_all=True

    availabilities=["in stock"]*len(titles)
    conditions = [condition]*len(titles)
    brands=[brand_string]*len(titles)
    id_list=[f"{sku_base}_{i}" for i in range(0,len(titles))]
  
    descriptions=[fix_ascii(x) for x in descriptions]
    titles= [fix_ascii(x) for x in titles]
    listing_urls=[x.split("?")[0] for x in listing_urls] #remove last part of url metadata not needed

    df = pd.DataFrame(list(zip(id_list,titles,descriptions,availabilities,conditions,prices,listing_urls,image_urls,brands,additional_image_urls)),columns=column_names)
    df.to_csv(output_path,index=False)
    print(f"Done creating csv, outputted to: {output_path}")




if name==if __name__ == '__main__':
    
    
etsystore="ahueofGreekblue"
ListingToFacebookCsv(etsystore,api_key,"ahueofGreekblue",sku_base="agreek")
