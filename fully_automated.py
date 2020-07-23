from etsy_csv_getter import ListingToFacebookCsv
from save_to_dropbox import backup



etsyshoplist=["ahueofGreekblue","ahueofDuckeggblue"]
valid_input=False
while not valid_input:
        shop_index = input("Type 1 for ahueofGreekBlue or 2 for ahueofDuckeggblue: ")
        try:
                shop_index = int(shop_index)
        except:
                print("Invalid input for shop index, not an integer, try again!")
                continue

        if shop_index in range(0,len(etsyshoplist)):
                valid_input=True
        else:
                print("Shop index does not match shop in shop list, please try again!")



skubaselist=["agreek","aduck"]

etsystore=etsyshoplist[shop_index-1]
sku_base=skubaselist[shop_index-1]

with open("api_key.txt","r") as f:
        api_key=f.read()

ListingToFacebookCsv(etsystore,api_key,etsystore,sku_base="")


backup(f"{etsystore}_facebook_catalogue.csv",f"/{etsystore}_facebook_catalogue.csv")

print("All done can close window!")