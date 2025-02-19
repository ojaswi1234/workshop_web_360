from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['portfolio']

# Define the contactus route with both GET and POST methods
@app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Create a document to insert into the database
        doc = {
            'name': name,
            'email': email,
            'message': message
        }

        # Insert the document into the database
        db.contactus.insert_one(doc)

    # Render the contactus template
    return "done"

# Define the index route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=80, debug=True)


