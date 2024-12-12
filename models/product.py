import mysql.connector
from config import Config #configure mysql database


def get_products(user_message):

    # Create a MySQL connection
    conn = mysql.connector.connect(
        host=Config.SQL_HOST,
        user=Config.SQL_USER,
        password=Config.SQL_PASSWORD,
        database=Config.SQL_DATABASE
    )
    cursor = conn.cursor(dictionary=True)

    # Query products that match the user input/not working rn
    query = "SELECT * FROM products WHERE LOWER(name) LIKE %s"
    cursor.execute(query, ('%' + user_message.lower() + '%',))

    products = cursor.fetchall()


    if products:
        response = "Here are some products I found:\n"
        for product in products:
            response += f"Name: {product['product_name']}, Description: {product['product_description']}, Price: ${product['price']}\n"
    else:
        response = "Sorry, I couldn't find any products matching your query."

    cursor.close()
    conn.close()

    return response