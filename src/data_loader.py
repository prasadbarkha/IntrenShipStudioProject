import pandas as pd
from src.db_connection import get_connection

def load_data():
    conn = get_connection()
    query = "SELECT * FROM transactions"
    
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df