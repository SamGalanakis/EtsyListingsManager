# EtsyListingsManager


Uses etsy api to generate a csv in the required data feed file format for integration with facebook/instagram webshops. The facebook csv template can be found [here](https://www.facebook.com/business/help/120325381656392?id=725943027795860). Only the required columns + the extra images are implemented although the code could easily be explanded to include more columns.

For use an etsi api key must be stored in a txt document "api_key.txt" in the root directory. For also using the automatic backup to dropbox (which can then be linked to facebook [catalogue data feed](https://www.facebook.com/business/help/125074381480892?id=725943027795860)) a valid dropbox api token is also needed, should be stored in "dropbox_token.txt" in root.

A useful guide for the general process is [this](https://www.youtube.com/watch?v=uzr559BMsjQ&t=668s). 


The "etsy_csv_getter.py" script can be run directly, the following variables are needed:

* etsystore : name of shop as it appears on etsy
* brandname: name of brand as it should appear on facebook, often same as etsystore
* sku_base: base for id on facebook catalogue, if not inputted will default to etsy sku 

If also using dropbox:

Configer the "BACKUP" path, where the csv will be uploaded to, is relative to folder of dropbox app connected to the given token. The default is the root directory.

For ease of use this can be packaged into a single script with a simple interface and then made into an executable, "fully_automated.py" is what I am using.

The dropbox saving script is not my code, taken from [here](https://gist.github.com/Keshava11/d14db1e22765e8de2670b8976f3c7efb).