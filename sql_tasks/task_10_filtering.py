import sqlite3

def get_pending_customers():
    conn = sqlite3.connect('parts_avatar.db')
    cursor = conn.cursor()
    
    # Task: Select customer email and order_date where status is 'Pending'.
    query = """
    
    select distinct customer_email, order_date
from (
    select a.customer_id, a.customer_email, b.order_date
    from Customers a 
    join (
    select customer_id, order_date, status from Orders
    where status = 'Pending' ) b
    on a.customer_id = b.customer_id
) as r

    """
    
    cursor.execute(query)
    return cursor.fetchall()
