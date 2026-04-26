import pandas as pd

def clean_data(df):
    # Convert date format
    df['trans_date'] = pd.to_datetime(df['trans_date'], format='%d-%b-%y')

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove invalid amounts (if any)
    df = df[df['tran_amount'] > 0]

    return df