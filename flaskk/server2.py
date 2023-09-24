from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})
CORS(app, resources={r"/insert_data/*": {"origins": "http://localhost:5173"}})
CORS(app, resources={r"/get_data/*": {"origins": "http://localhost:5173"}})
#mongo = PyMongo(app)
from pymongo import MongoClient
client = MongoClient("mongodb+srv://Chamax:chameadores@cluster0.onh5ksw.mongodb.net/?retryWrites=true&w=majority")

@app.route('/api', methods=['POST','GET'])
def save_data():
    data = request.get_json()  # Assuming data is sent in JSON format
    
    # Process and save the data as needed
    print(data["data"])
    return  jsonify({"message": "Data saved successfully"})

@app.route('/insert_data', methods=['POST','GET'])
def insert_data():
    db = client["prueba1"]
    data_collection = db["2"]
    data_to_insert = request.get_json()
    inserted_data = data_collection.insert_one(data_to_insert)
    print('algo')
    return jsonify({'message': 'Data inserted successfully'})

@app.route('/get_data')
def get_data():
    db = client["prueba1"]
    data_collection = db["2"]
    data = data_collection.find({})
    result = []
    for document in data:
        
        result.append({
            'name': document['name'],
            'email': document['email'],
            # Add other fields as needed
        })
    
    print(result)
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True)