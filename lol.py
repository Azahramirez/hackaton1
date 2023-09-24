from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb+srv://Chamax:chameadores@cluster0.onh5ksw.mongodb.net/?retryWrites=true&w=majority")

# Select the database you want to check for collections
db = client["prueba1"]
collection = db["2"]

data_to_insert = {
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}

result = collection.insert_one(data_to_insert)

# Print the inserted document's ID (a unique identifier)
#print(f"Inserted document ID: {result.inserted_id}")
# List the collections in the selected database
#collections = db.list_collection_names()



#for collection in collections:
 #   print(collection)
