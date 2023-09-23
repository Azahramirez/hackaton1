from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/save-data', methods=['POST'])
def save_data():
    data = request.json  # Assuming data is sent in JSON format
    # Process and save the data as needed
    return jsonify({"message": "Data saved successfully"})

if __name__ == "__main__":
    app.run(debug=True)