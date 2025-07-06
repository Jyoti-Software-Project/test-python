from db import get_connection

def get_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return items

def add_item(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
    conn.commit()
    conn.close()

def delete_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = %s", (item_id,))
    conn.commit()
    conn.close()
