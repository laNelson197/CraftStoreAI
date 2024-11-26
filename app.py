from flask import Flask, render_template, jsonify
import mysql.connector
from config import Config

app = Flask(__name__)

# Function to get all products from the database
def get_all_products():
    conn = mysql.connector.connect(
        host=Config.SQL_HOST,
        user=Config.SQL_USER,
        password=Config.SQL_PASSWORD,
        database=Config.SQL_DATABASE
    )
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM products"
    cursor.execute(query)

    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return products

# Home route to render the index page
@app.route('/')
def home():
    return render_template('index.html')

# Route to fetch all products
@app.route('/get_all_products', methods=['GET'])
def get_products():
    products = get_all_products()
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)
