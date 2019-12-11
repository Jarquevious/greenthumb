from flask import Flask, render_template
from bson.objectid import ObjectId
# Import pymongo and initialize client
from pymongo import MongoClient
client = MongoClient()

app = Flask(__name__)

@app.route('/')
def index():
    """Show all Appointments."""
    # change the original return statement you wrote to the one below
    return render_template('home.html')

@app.route('/sign_up')
def sign_up():
    """Create a new appointment."""
    return render_template('sign_up.html')

@app.route('/')


if __name__ == '__main__':
    app.run(debug=True)