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
conn.commit()

def insert_product(product_name, product_details, expiry_date, vendor, location):
    insert_query = '''
    INSERT INTO product (product_name, product_details, expiry_date, vendor, location)
    VALUES (?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_query, (product_name, product_details, expiry_date, vendor, location))
    conn.commit()

def update_product(product_id, product_name=None, product_details=None, expiry_date=None, vendor=None, location=None):
    update_query = 'UPDATE product SET'
    parameters = []
    if product_name:
        update_query += ' product_name = ?,'
        parameters.append(product_name)
    if product_details:
        update_query += ' product_details = ?,'
        parameters.append(product_details)
    if expiry_date:
        update_query += ' expiry_date = ?,'
        parameters.append(expiry_date)
    if vendor:
        update_query += ' vendor = ?,'
        parameters.append(vendor)
    if location:
        update_query += ' location = ?,'
        parameters.append(location)
    
    # Remove the trailing comma and add the WHERE clause
    update_query = update_query.rstrip(',') + ' WHERE id = ?'
    parameters.append(product_id)
    
    cursor.execute(update_query, tuple(parameters))
    conn.commit()

def get_products():
    select_query = 'SELECT * FROM product'
    cursor.execute(select_query)
    return cursor.fetchall()

def get_product_by_id(product_id):
    select_query = 'SELECT * FROM product WHERE id = ?'
    cursor.execute(select_query, (product_id,))
    return cursor.fetchone()

# Example usage:
# Insert a new product
insert_product('Product A', 'Details of Product A', '2024-12-31', 'Vendor A', 'Location A')

# Update the product
# update_product(1, product_name='Updated Product A', product_details='Updated Details')

# Retrieve and print all products
products = get_products()
for product in products:
    print(product)

# Retrieve and print a specific product by id
product = get_product_by_id(1)
print(product)

# Close the connection when done
conn.close()
