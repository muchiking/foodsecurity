import sqlite3



def get_products(product):
  
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('db.sqlite3')
   
    # Create a cursor object to interact with the database

    cursor = conn.cursor()
    select_query = f'SELECT * FROM {product}'
    cursor.execute(select_query)
    ans=cursor.fetchall()
    # Close the connection when done
    conn.close()
    return ans
