Craft Store AI Chatbot - Setup Guide
Project Overview:
The Craft Store AI Chatbot is a web app that allows users to inquire about products in a craft store. It fetches product data from a MySQL database and responds based on user queries. The app uses Flask for the web framework and Groq's AI model for natural language processing.


File Summaries:
app.py:
    Main Flask app that handles routes, user queries, database interactions, and integrates with Groq API for AI responses.

config.py:
    Contains MySQL database connection settings (host, user, password, and database name).

product.py:
    Defines get_products() to query the MySQL database for products matching user input.

<<<<<<< HEAD
style.css:
    CSS file for frontend styling, including layout, colors, and button styles.

script.js:
    JavaScript for frontend interactivity, handling the "Show Products" button and displaying product data.

index.html:
    HTML template for rendering the webpage, including user input forms and displaying AI responses.

Setup Guide:
1. Clone the Repository:
    git clone https://github.com/yourusername/craft-store-ai-chatbot.git

2. Install Dependencies:
    cd craft-store-ai-chatbot
    pip install -r requirements.txt

3. Set Up MySQL Database:
    CREATE TABLE products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        product_name VARCHAR(255) NOT NULL,
        product_description TEXT,
        price DECIMAL(10, 2)
    );
    Add sample data:
    INSERT INTO products (product_name, product_description, price) 
    VALUES ('Craft Paper', 'High-quality paper for crafting', 5.99),
        ('Glue Gun', 'Hot glue gun for quick crafting', 12.49);
        
4. Configure Database Connection:
class Config:
    SQL_HOST = 'localhost'  # or your MySQL server hostname
    SQL_USER = 'your_mysql_user'
    SQL_PASSWORD = 'your_mysql_password'
    SQL_DATABASE = 'craftstoredb'  # database name

5. Run the Application:
    python app.py


**Capabilities:**  
This AI application is connected to a database, allowing it to display all products at once. However, it is currently unable to retrieve individual product details on demand.

**Limitations:**  
While I initially aimed to create a more basic, "rag"-like application, I ended up developing a model that integrates with a database. In cases where the database does not have a specific answer, the model can provide a response based on its own knowledge.

**Future Improvements:**  
In the future, the application could be enhanced to include the logic necessary to retrieve individual product details. This project has been a valuable learning experience, and I would approach it differently if I were to build it again.
=======
### 1. Clone the Repository:
If you haven't already, clone the repository to your local machine using:
```bash
git clone https://github.com/laNelson197/CraftStoreAI.git
>>>>>>> df93cb9e29762adbaf9d0ee021a7293eb4378d4f
