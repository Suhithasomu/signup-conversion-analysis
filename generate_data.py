import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
fake = Faker()

# Configuration
num_sessions_week1 = 5000  # Week 1
num_sessions_week2 = 5000  # Week 2

# Start date
start_date = datetime(2024, 2, 5)  # Week 1 starts Feb 5

print("Generating data... this will take about 30 seconds...")

# Function to generate session data
def generate_sessions(num_sessions, week_num, start_date):
    data = []
    
    for i in range(num_sessions):
        session_id = f"S{week_num}_{i+1:05d}"
        user_id = f"U{random.randint(1, num_sessions*2)}"
        
        # Random day within the week
        day_offset = random.randint(0, 6)
        session_date = start_date + timedelta(days=day_offset)
        
        # Device type distribution
        device_type = random.choices(
            ['mobile', 'desktop', 'tablet'],
            weights=[0.60, 0.35, 0.05]
        )[0]
        
        # Traffic source
        traffic_source = random.choices(
            ['organic', 'paid_search', 'social', 'direct'],
            weights=[0.40, 0.30, 0.20, 0.10]
        )[0]
        
        # Landing page
        landing_page = random.choice(['homepage', 'pricing', 'product'])
        
        # Conversion logic (this is where we create the "problem")
        if week_num == 1:
            # Week 1: Normal conversion rates
            if device_type == 'mobile':
                conversion_prob = 0.10  # 10% mobile conversion
            elif device_type == 'desktop':
                conversion_prob = 0.14  # 14% desktop conversion
            else:
                conversion_prob = 0.08  # 8% tablet
        else:
            # Week 2: Mobile drops significantly
            if device_type == 'mobile':
                conversion_prob = 0.06  # DROPPED to 6%
            elif device_type == 'desktop':
                conversion_prob = 0.14  # Desktop stays same
            else:
                conversion_prob = 0.08  # Tablet stays same
        
        # Organic traffic converts better
        if traffic_source == 'organic':
            conversion_prob *= 1.2
        elif traffic_source == 'paid_search':
            conversion_prob *= 0.8
        
        # Did they convert?
        signup_completed = random.random() < conversion_prob
        
        data.append({
            'session_id': session_id,
            'user_id': user_id,
            'session_date': session_date.strftime('%Y-%m-%d'),
            'week_number': week_num,
            'device_type': device_type,
            'traffic_source': traffic_source,
            'landing_page': landing_page,
            'signup_completed': signup_completed
        })
    
    return data

# Generate Week 1 data
print("Generating Week 1 data...")
week1_data = generate_sessions(num_sessions_week1, 1, start_date)

# Generate Week 2 data (one week later)
print("Generating Week 2 data...")
week2_start = start_date + timedelta(days=7)
week2_data = generate_sessions(num_sessions_week2, 2, week2_start)

# Combine both weeks
all_sessions = week1_data + week2_data

# Create DataFrame
df_sessions = pd.DataFrame(all_sessions)

# Save to CSV
output_path = '../data/user_sessions.csv'
df_sessions.to_csv(output_path, index=False)

print(f"\n✅ SUCCESS! Data saved to: {output_path}")
print(f"\n📊 Data Summary:")
print(f"Total sessions: {len(df_sessions)}")
print(f"Week 1 sessions: {len(df_sessions[df_sessions['week_number']==1])}")
print(f"Week 2 sessions: {len(df_sessions[df_sessions['week_number']==2])}")
print(f"\nConversion Rates:")
print(df_sessions.groupby('week_number')['signup_completed'].mean())
print(f"\nBy Device:")
print(df_sessions.groupby(['week_number', 'device_type'])['signup_completed'].mean())