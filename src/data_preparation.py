def prepare_data(df):
    # Extract year & month
    df['year'] = df['trans_date'].dt.year
    df['month'] = df['trans_date'].dt.month

    # Create total value (same as amount here)
    df['total_value'] = df['tran_amount']

    return df