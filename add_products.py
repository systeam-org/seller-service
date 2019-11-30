import sys
import os
import requests
from random import randint
import ssl
import base64
import json
from urllib.request import urlopen


if __name__ == '__main__':

    products = [
        "Furniture#Armoire#200#Bedroom Armoire 2-door 2-drawers wardrobe storage closet cabinet wood Home NEW#https://i.ebayimg.com/thumbs/images/m/mNRfL5FcdHme89XBITDA7EA/s-l225.jpg",
        "Furniture#Closet#150#Heavy Duty Portable Closet Storage Organizer Clothes Shelf Wardrobe Rack Shelves#https://i.ebayimg.com/thumbs/images/m/mfClPX52lx6DbMY-D-17vow/s-l225.jpg",
        "Furniture#Wardobe#120#Bedroom Armoire 2-Door Wardrobe Storage 4-Shelves Adjustable Cabinet Hanging Bar#https://i.ebayimg.com/thumbs/images/m/maj_khdS1CCkGs7p610YhpA/s-l225.jpg",
        "Furniture#Wardobe with mirror#400#Cosmo 3-Door Wardrobe/Armoire/Closet with Mirror and 3 Drawers by Palace Imports#https://i.ebayimg.com/thumbs/images/m/mD-hq5rk71zs6KcJS9js_jQ/s-l225.jpg",
        "Furniture#Closet Storage#190#Heavy Duty Portable Closet Storage Organizer Clothes Shelf Wardrobe Rack Shelves#https://i.ebayimg.com/thumbs/images/m/mAS04UvwkEJXWXGLbswP7pg/s-l225.jpg",
        "Kitchen#Mixer#200#KitchenAid Stand Mixer tilt 5-QT RRK150 Artisan Tilt Choose From Many Colors#https://i.ebayimg.com/thumbs/images/m/mc0O93srrR48KrNRdMD2Mng/s-l225.jpg",
        "Kitchen#Bowl lift mixer#100#KitchenAid® Refurbished Pro 600™ Series 6 Quart Bowl-Lift Stand Mixer, RKP26M1X#https://i.ebayimg.com/thumbs/images/m/mX47HQWjI8UgU-Oyij5HETQ/s-l225.jpg",
        "Kitchen#Filter#200#FRIGIDAIRE ULTRAWF PURESOURCE 3 KENMORE 46-9999 Genrt Water Filter 1~6PK#https://i.ebayimg.com/thumbs/images/m/m944ItGe0Meg_4SCOpzYW_A/s-l225.jpg",
        "Kitchen#Fridge water filter#200#1/2/3/4Pack Genuine Samsung DA29-00020B HAF-CIN/EXP Fridge Water Filter Replace#https://i.ebayimg.com/thumbs/images/m/mgq_N4EvDv8rYxItto6tYXg/s-l225.jpg",
        "Mens#Hoodie#20#Classic PEECHEE Folder Tee Shirt Sweatshirt Hoodie Ladies Mens  New Pee Chee#https://i.ebayimg.com/thumbs/images/m/mu60qQDutD3kfQLiAYrE8DA/s-l225.jpg",
        "Mens#Tee Shirt#30#Corona Tank Top Ocean Wave Extra Beer Graphic Tee Shirt Men's Size Medium-3XL#https://i.ebayimg.com/thumbs/images/m/motUMJNE7T1tD1ELJ1tBJRw/s-l225.jpg",
        "Mens#Holt Shirt#40#OFFICIAL GARY HOLT OFFICER HOLT SHIRTS!#https://i.ebayimg.com/thumbs/images/m/meQp5cSTNesWb2pIAccxDZA/s-l225.jpg",
        "Mens#Black T-shirt#50#FREESHIP Grinch NFL Official Team Football Baltimore Ravens T-Shirt Black S-6XL#https://i.ebayimg.com/thumbs/images/m/m01k9J6x49_fdKTRXKj2AQA/s-l225.jpg",
        "Mens#Personalized text T-shirt#100#PERSONALIZED CUSTOM PRINT YOUR OWN TEXT ON A T-SHIRT CUSTOMIZED MEN/WOMEN#https://i.ebayimg.com/thumbs/images/m/mAiwvu6MVeqeFrEhvlbw-ag/s-l225.jpg",
        "Mens#Polo shirt#40# Ralph Lauren Men CrewNeck Classic Fit Long Sleeve Tee S M L XL 3x 4x 5x Nwt#https://i.ebayimg.com/thumbs/images/m/myf5qCFjk8scd8Ynev594-w/s-l225.jpg",
        "Shoes#Fila Boot#160# Men's WeatherTech Extreme Waterproof Boot#https://i.ebayimg.com/thumbs/images/m/muJH1udgYxs_oHI3gdRve4Q/s-l225.jpg",
        "Shoes#Waterproof boot#200#Timberland 6 Inch Premium Waterproof Boots Wheat Men's Shoes TB0 10061-713#https://i.ebayimg.com/thumbs/images/m/myrLhHrHQPlEs_SsHQq4ztA/s-l225.jpg",
        "Shoes#All weather shoes#140#Fila Men's Weathertec Boot#https://i.ebayimg.com/thumbs/images/m/mrEA6cfTsLew_qLMWu3Seqg/s-l225.jpg",
        "Shoes#Skechers#150# Men's   Work Burgin Tarlac Steel Toe Boot#https://i.ebayimg.com/thumbs/images/m/m54PQcAWdzd_3IgqXhOSigA/s-l225.jpg",
        "Shoes#Work boots#40#MEN'S SQUARE STEEL TOE WORK BOOTS GENUINE SOFT LEATHER COWBOY PULL ON BOTAS#https://i.ebayimg.com/thumbs/images/m/mb3rcKFf-kz9Vq7WjU2Fk4g/s-l225.jpg",
        "Shoes#Ankle boots#80#Brown Men's Lace Up  Cap Toe Dress Oxford Ankle Boots #https://i.ebayimg.com/thumbs/images/m/m_LwQJKDROCKqq52hACDi4g/s-l225.jpg",
        "Sports#Dual Motor scooter#220#2019 Upgraded Mercane Electric Scooter WideWheel Folding Dual Motor  wide wheel#https://i.ebayimg.com/thumbs/images/m/mra3IoViGh78aYJCevXopAQ/s-l225.jpg",
        "Sports#Hoverboard#400#SWAGTRON T6 UL2272 Rugged Off-Road Motorized Self Balancing Electric Hoverboard#https://i.ebayimg.com/thumbs/images/m/m74LUFwqjYvec01Sw1-414Q/s-l225.jpg",
        "Sports#Light weight scooter#200#2019 Electric Scooter, 250 W Motor, 3-speed, Ultra Lightweight#https://i.ebayimg.com/thumbs/images/m/mjFSG8XbxHgEhbV3sbscMfQ/s-l225.jpg",
        "Sports#Electric Scooter#300#Hiboy S2 Foldable 350W Kich E-Scooter High Speed Electric Scooter 8.5” for Adult#https://i.ebayimg.com/thumbs/images/m/mWQXu9tXLoXtbj4Ir-Zz84g/s-l225.jpg",
        ]
    for p in products[13:]:
        product = {}
        product['category'] = p.split("#")[0]
        product['name'] = p.split("#")[1]
        product['price'] = p.split("#")[2]
        product['description'] = p.split("#")[3]
        product['image_url'] = p.split("#")[4]

        email = "praveen.thakur@sjsu.edu"
        category = product['category']
        productname = product['name']
        productdesc = product['description']
        url = product['image_url']
        price = randint(10, 80)
        quantity = randint(1, 9)

        imageFile = urlopen(url)
        files = {
            "image": (productdesc, imageFile, 'application-type')
        }

        productdata = {
            "category_name": category,
            "email": email,
            "product_name": productname,
            "description": productdesc,
            "price": price,
            "available_quantity": quantity
        }
        data = {
            "data": json.dumps(productdata)
        }

        r = requests.post(url="https://sellerapi.systeambiz.com/addproduct", data=data,files=files, verify=False)


