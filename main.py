from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.data_preparation import prepare_data

df = load_data()

print("Original Data:")
print(df.head())

# Cleaning
df = clean_data(df)

# Preparation
df = prepare_data(df)

print("\nCleaned Data:")
print(df.head())

print("\nFinal Info:")
print(df.info())

monthly_sales = df.groupby('month')['total_value'].sum()

print("\nMonthly Sales:")
print(monthly_sales)