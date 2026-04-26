from src.data_loader import load_data

df = load_data()

print("First 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())