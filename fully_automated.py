from etsy_csv_getter import ListingToFacebookCsv
from save_to_dropbox import backup


shop_index = input("Type 1 for ahueofGreekBlue or 2 for ahueofDuckeggblue: ")
shop_index = int(shop_index)
assert (shop_index ==1 or shop_index ==2), "Invalid input, should be 1 or 2"
etsyshoplist=["ahueofGreekblue","ahueofDuckeggblue"]
skubaselist=["agreek","aduck"]

etsystore=etsyshoplist[shop_index-1]
sku_base=skubaselist[shop_index-1]

with open("api_key.txt","r") as f:
        api_key=f.read()

ListingToFacebookCsv(etsystore,api_key,etsystore,sku_base="")


backup(f"{etsystore}_facebook_catalogue.csv",f"/{etsystore}_facebook_catalogue.csv")

print("All done can close window!")