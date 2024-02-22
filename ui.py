from os import system
from Product import Product
from Bag import Bag
from BagItem import BagItem
from Money import Money
from Client import Client
from Stock import Stock
from random import randint

def printMainMenu():
    print("#" * 60)
    print("""
        1. show catalog
        2. add to bag
        3. show bag
        4. find products by name
    """)
    print("#" * 60)
    option = int(input(">>> "))
    return option

def printCatalog():
    products = Product.findAll()
    print("#" * 60)
    for product in products:
        print (product)
    print("#" * 60)

def addToBag(client_id):
    bag = Bag.findByClient(client_id)
    if bag == None:
        cost = Money(randint(999999, 2000000), 0, "EUR")
        cost.save()
        bag = Bag(randint(999999, 2000000), cost.id, client_id)
        bag.save()
    product_id = int(input("Enter Product ID>>> "))
    #bag_item = BagItem(randint(999999, 2000000), bag.id, product_id, 1)
    quantity = int(input('How many products ? '))
    bag_item = BagItem(randint(999999, 2000000), bag.id, product_id, quantity)
    bag_item.save()
    stock = Stock.findByProduct(product_id)
    if stock != None:
        if stock.quantity < quantity:
            print("There are not enough products in stock.")
        else:
         stock.quantity -= quantity
         stock.update()

def printBag(bag_id):
    bag_items = BagItem.findAllByBag(bag_id)
    total_cost = 0
    for bi in bag_items:
        b = Bag.find(bi.bag_id)
        total_cost += b.cost.amount * bi.quantity
        print(bi, "total cost: ", total_cost, b.cost.currency)