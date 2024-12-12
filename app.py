from flask import Flask, render_template, request, jsonify # type: ignore
import mysql.connector # type: ignore
from config import Config
import os
from groq import Groq # type: ignore

app = Flask(__name__)

# Initialize Groq client with the API key
client = Groq(
    api_key="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",
)

# Function to get chat response from Groq API
def get_chat_response(user_message):
    # If user asks for products, call the get_all_products route
    if "all products" in user_message.lower() or "show products" in user_message.lower():
        return get_all_products_from_db()
    else:
        try:
            chat_completion = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": user_message,
                }],
                model="llama3-8b-8192",
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error fetching chat response: {str(e)}"

# Function to get all products from the database
def get_all_products_from_db():
    try:
        # Create a MySQL connection
        conn = mysql.connector.connect(
            host=Config.SQL_HOST,
            user=Config.SQL_USER,
            password=Config.SQL_PASSWORD,
            database=Config.SQL_DATABASE
        )
        cursor = conn.cursor(dictionary=True)

        # Query to fetch all products
        query = "SELECT * FROM products"
        cursor.execute(query)

        products = cursor.fetchall()

        if products:
            response = "Here are all the products we have:\n"
            for product in products:
                response += f"Name: {product['product_name']}, Description: {product['product_description']}, Price: ${product['price']}\n"
        else:
            response = "Sorry, I couldn't find any products in the database."

    except mysql.connector.Error as err:
        response = f"Error retrieving products from the database: {err}"

    finally:
        cursor.close()
        conn.close()

    return response

# Home route to render the index page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle AI query (POST request)
@app.route('/ai-query', methods=['POST'])
def ai_query():
    user_message = request.form.get('user_query')
    if user_message:
        # Get the AI response or product response based on the query
        ai_response = get_chat_response(user_message)
        return render_template('index.html', ai_response=ai_response)
    else:
        return render_template('index.html', ai_response="Please provide a message.")

# Route to fetch all products (as a separate API endpoint)
@app.route('/get_all_products', methods=['GET'])
def get_products():
    products = get_all_products_from_db()
    return jsonify({"response": products})

if __name__ == '__main__':
    app.run(debug=True)
