
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object to interact with the database
cursor = conn.cursor()



insert_query = '''
   INSERT INTO farm_animal ('Animal_name', 'County', 'Location', 'vendor', 'phone', 'image', 'details')
VALUES 
('Cow', 'Nyeri', 'Kiganjo', 'John Doe', '0712345678', 'cow.jpg', 'Healthy dairy cow'),
('Chicken', 'Nairobi', 'Kasarani', 'Jane Smith', '0723456789', 'chicken.jpg', 'Free-range chicken'),
('Goat', 'Nakuru', 'Naivasha', 'Peter Johnson', '0734567890', 'goat.jpg', 'Boer goat for breeding'),
('Sheep', 'Nyeri', 'Nyeri Town', 'Lucy Wangui', '0745678901', 'sheep.jpg', 'Dorper sheep, suitable for meat'),
('Pig', 'Nairobi', 'Dagoretti', 'James Kamau', '0756789012', 'pig.jpg', 'Large White pig for pork production'),
('Rabbit', 'Nakuru', 'Njoro', 'Mary Njoki', '0767890123', 'rabbit.jpg', 'New Zealand White rabbit for breeding'),
('Duck', 'Nyeri', 'Othaya', 'George Mwangi', '0778901234', 'duck.jpg', 'Pekin duck for meat and eggs'),
('Turkey', 'Nairobi', 'Karen', 'Anne Muthoni', '0789012345', 'turkey.jpg', 'Broad Breasted White turkey'),
('Horse', 'Nakuru', 'Gilgil', 'Joseph Njoroge', '0790123456', 'horse.jpg', 'Thoroughbred horse for racing'),
('Donkey', 'Nyeri', 'Karatina', 'Elizabeth Wanjiku', '0701234567', 'donkey.jpg', 'Donkey suitable for farm work');
    '''
cursor.execute(insert_query, (product_name, product_details, expiry_date, vendor, location))
conn.commit()