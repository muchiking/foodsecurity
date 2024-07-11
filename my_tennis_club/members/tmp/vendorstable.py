import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('vendors.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create the vendor table with the specified columns
create_table_query = '''
CREATE TABLE IF NOT EXISTS vendor (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_name TEXT NOT NULL,
    details TEXT,
    vendor_promo TEXT
)
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Vendor table created successfully.")
