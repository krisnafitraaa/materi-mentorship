#belajar read and write file dengan format JSON (Javascript Object Notation)
#definisikan list yang menyimpan data
# 1. Customer
# 2. Produk
# 3. Transaksi

import json
  
# Opening JSON file
f = open('db.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['users']:
    print(i)
  
# Closing file
f.close()