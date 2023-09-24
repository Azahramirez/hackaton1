from flask import Flask, request, render_template, send_from_directory, jsonify
from markupsafe import escape
from flask_cors import CORS
from flask_pymongo import PyMongo
from pymongo import MongoClient
import os

app = Flask(__name__)

CORS(app)

client = MongoClient("mongodb+srv://Chamax:chameadores@cluster0.onh5ksw.mongodb.net/?retryWrites=true&w=majority")

react_folder = "hack_mty"
directory=os.getcwd() + f"/{react_folder}/build/static"

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

@app.route('/', methods=['GET', 'POST'])
def index():
    path=os.getcwd() + f"/{react_folder}/build"
    if request.method == 'GET':
        return send_from_directory(directory=path, path='index.html')  
    else:
        return send_from_directory(directory=path, path='index.html')

@app.route('/static/<folder>/<file>')
def css(folder, file):
    path = folder+"/"+file
    return send_from_directory(directory=directory, path=path)

@app.route('/user/json')
def user_json():
    return {"name": "John", "email": "raag0206@hotmail.com"}

if __name__ == '__main__':
    app.run(debug=True, threaded=True)




# @app.route('/hello')
# def hello():
#     return 'Hello, World'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

# def show_the_login_form():
#     return '<form method="post" action="http://127.0.0.1:5000/login"><input placeholder="hola" name="name"/><button type="submit">Submit</button></form>'

# def do_the_login():
#     return f'<h1>{request.form["name"]}<h1>'