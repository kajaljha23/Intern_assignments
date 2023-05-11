from pymongo import MongoClient  # import mongo client to connect
# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
# Creating database
db = client.interns_b2_23
inventory_item = {"category": "books",
                  "product_id": "5678",
                  "product_name": "Oil",
                  "quantity": "3",
                  "price": "300"
                  }
# # Creating document
inventory = db.Kajal_kumari
# # Inserting data
inventory.insert_one(inventory_item)
# # Fetching data
print(inventory.find_one({"product_id": "5678"}))
