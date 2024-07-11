import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the product table with the specified columns
create_table_query = '''
CREATE TABLE IF NOT EXISTS product (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    product_details TEXT,
    expiry_date TEXT,
    vendor TEXT,
    location TEXT
)
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Product table created successfully.")
