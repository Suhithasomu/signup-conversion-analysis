import pandas as pd
import mysql.connector
from mysql.connector import Error

# Read CSV file
print("Reading CSV file...")
df = pd.read_csv('../data/user_sessions.csv')

print(f"Found {len(df)} rows in CSV")

# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='signup_analysis',
        user='root',
        password='abc@123'  # If you have a password, put it here in quotes
    )
    
    if connection.is_connected():
        print("✅ Successfully connected to MySQL!")
        
        cursor = connection.cursor()
        
        # Clear table first (in case you're running this again)
        cursor.execute("DELETE FROM user_sessions")
        print("Cleared existing data (if any)")
        
        # Insert data row by row
        insert_query = """
        INSERT INTO user_sessions 
        (session_id, user_id, session_date, week_number, device_type, 
         traffic_source, landing_page, signup_completed)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        print("Inserting data... this will take about 30 seconds...")
        
        for index, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))
            
            # Show progress every 1000 rows
            if (index + 1) % 1000 == 0:
                print(f"  Inserted {index + 1} rows...")
        
        connection.commit()
        print(f"\n✅ SUCCESS! Inserted {len(df)} rows into MySQL!")
        
        # Verify
        cursor.execute("SELECT COUNT(*) FROM user_sessions")
        count = cursor.fetchone()[0]
        print(f"✅ Verified: {count} rows in database")
        
        # Show sample data
        cursor.execute("SELECT * FROM user_sessions LIMIT 3")
        print(f"\nFirst 3 rows:")
        for row in cursor.fetchall():
            print(row)
        
        cursor.close()
        
except Error as e:
    print(f"❌ Error: {e}")
    print("\nIf you see 'Access denied', you might need to add your password.")
    print("Edit the script and change: password='' to password='your_password'")
    
finally:
    if connection.is_connected():
        connection.close()
        print("\nMySQL connection closed")
