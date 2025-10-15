import pandas as pd
import mysql.connector
from config import MODE, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_db_connection():
    if MODE == "DEV":
        return None
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

def fetch_data():
    if MODE == "DEV":
        sales_df = pd.DataFrame({
            'item_id':[1,2,3,4,5],
            'title':['Book A','Book B','Book C','Book D','Book E'],
            'category':['Fiction','Science','History','Fiction','Science'],
            'quantity_sold':[50,30,20,10,5],
            'sale_date':['2025-10-01']*5,
            'price':[200,150,100,250,120],
            'profit':[100,60,30,120,50]
        })
        inventory_df = pd.DataFrame({
            'item_id':[1,2,3,4,5],
            'title':['Book A','Book B','Book C','Book D','Book E'],
            'category':['Fiction','Science','History','Fiction','Science'],
            'stock_quantity':[100,50,20,60,30],
            'stock_age_days':[10,20,30,15,5],
            'supplier':['Supplier1','Supplier2','Supplier3','Supplier1','Supplier2']
        })
        return sales_df, inventory_df
    else:
        conn = get_db_connection()
        sales_df = pd.read_sql("SELECT * FROM sales", conn)
        inventory_df = pd.read_sql("SELECT * FROM inventory", conn)
        conn.close()
        return sales_df, inventory_df
