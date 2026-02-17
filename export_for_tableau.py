import pandas as pd
import mysql.connector

print("Connecting to MySQL...")

# Connect to MySQL
connection = mysql.connector.connect(
    host='localhost',
    database='signup_analysis',
    user='root',
    password='abc@123'  # Add your password here if you have one
)

print("✅ Connected!")
print("Reading data from user_sessions table...")

# Read all data
query = "SELECT * FROM user_sessions"
df = pd.read_sql(query, connection)

print(f"✅ Found {len(df)} rows")

# Save to CSV
output_path = '../data/tableau_data.csv'
df.to_csv(output_path, index=False)

print(f"✅ SUCCESS! Data exported to: {output_path}")
print(f"\nColumns: {list(df.columns)}")
print(f"\nFirst 3 rows:")
print(df.head(3))

connection.close()
print("\nMySQL connection closed")
