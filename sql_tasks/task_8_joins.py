import sqlite3

def get_customer_spend():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Join Customers, Orders, and Order_Items to calculate 
    # total spend (price * quantity) per Customer Name.
    query = """
    select customer_id, price * quantity from (
    select customer_id, order_id, price, quantity 
    from Orders a
    join Order_items b on a.order_id = b.order_id
    ) as a
    group by customer_id
    
    """
     
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results
