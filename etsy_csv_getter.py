import requests
from time import sleep
import pandas as pd



def fix_ascii(input_string):
    return input_string.replace("&#39;",r"'")

def ListingToFacebookCsv(shop_string,api_key,brand_string,sku_base="",condition="new"):

    got_all=False
    per_call=100 #number of items per call/page
    page=1
    
    column_names=["id","title","description","availability","condition","price","link","image_link","brand","additional_image_link"]
    image_urls=[]
    additional_image_urls=[]
    titles=[]
    descriptions=[]
    prices=[]
    listing_urls=[]
    etsy_sku=[]

    while not got_all:
        sleep(0.11) #so no more that 10 calls per second
        print(f"Parsing listings of shop: {shop_string}, page: {page}")
        response = requests.get(f"https://openapi.etsy.com/v2/shops/{shop_string}/listings/active?limit={per_call}&includes=Images&page={page}&api_key={api_key}").json()
        page+=1
        # count = response["count"]
        listings= response["results"]
        for listing in listings:
            listing_urls.append(listing["url"])
            etsy_sku.append(listing["sku"])
            image_urls.append(listing["Images"][0]["url_fullxfull"])
            extra_images_string=""
            for x in listing["Images"][1:]: 
                extra_images_string+=x["url_fullxfull"]+","  
            additional_image_urls.append(extra_images_string[:-1]) #cut last comma
            titles.append(listing["title"])
            descriptions.append(listing["description"])
            prices.append(listing["price"]+" USD")

        if 100 != len(listings): 
            got_all=True

    availabilities=["in stock"]*len(titles)
    conditions = [condition]*len(titles)
    brands=[brand_string]*len(titles)

    if len(sku_base)==0:  #if no sku base given, default to etsy sku
        id_list=etsy_sku
    else:
        id_list=[f"{sku_base}_{i}" for i in range(0,len(titles))]
    
    
    descriptions=[fix_ascii(x) for x in descriptions]
    titles= [fix_ascii(x) for x in titles]
    listing_urls=[x.split("?")[0] for x in listing_urls] #remove last part of url metadata not needed

    df = pd.DataFrame(list(zip(id_list,titles,descriptions,availabilities,conditions,prices,listing_urls,image_urls,brands,additional_image_urls)),columns=column_names)
    df.to_csv(f"{brand_string}_facebook_catalogue.csv",index=False)
    print(f"Done creating csv, outputted to: {brand_string}_facebook_catalogue.csv")




if __name__ == '__main__':
    
    
    with open("api_key.txt","r") as f:
        api_key=f.read()
    
    etsystore="myshopname"
    brandname="mybrandname"
    sku_base="base for id on fb catalogue, if not inputted will default to etsy sku "
    ListingToFacebookCsv(etsystore,api_key,brandname,sku_base="agreek")
    from save_to_dropbox import backup
  
    backup(f"{etsystore}_facebook_catalogue.csv",f"/{etsystore}_facebook_catalogue.csv")
    
    print("Finished!")

    




