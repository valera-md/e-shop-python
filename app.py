#from Product import Product
from Money import Money
from Bag import Bag
#from BagItem import BagItem
from Client import Client
from Product import Product
from Stock import Stock
from ui import *
from os import system

system("cls")
client_id = int(input('Enter client ID please: '))
client = Client.find(client_id)
while True:
 print(f"Hello, {client.fullname}!")
 option = printMainMenu()
 if option == 1:
  printCatalog()
  input()
 if option == 2:
  bag = addToBag(client_id)
  input()
 if option == 3:
  bag = Bag.findByClient(client_id)
  printBag(bag.id)
  input()
 if option == 4:
  keyword = input("Enter product name: ")
  products = Product.findAllByName(keyword)
  if len(products) > 0:
   for product in products:
    stock = Stock.findByProduct(product.id)
    if stock == None:
     print("product_id is not found in stock")
    elif stock.quantity == 0:
     print(f"{product.name} sold out")
     input()
    else:
     print(product)
     input()
  else:
   print("product is not found in products table")
   input()
  
# APP:
# 1. show catalog
# 2. add to bag
# 3. show bag
# 4. find products by name