# Signup Conversion Analysis 📊

## Project Overview
Investigated a 25% drop in signup conversion rate using 
Python, MySQL, SQL, and Tableau. Identified mobile-specific 
UX issue as the root cause.

## Business Problem
Signup conversion dropped from 11.88% to 10.58% in Week 2.
Leadership needed to understand why and what to fix.

## Tools Used
- **Python** (pandas) - Data generation and processing
- **MySQL** - Data storage and management
- **SQL** - Data analysis and querying
- **Tableau** - Data visualization and dashboard

## Key Findings
- Overall conversion dropped 11% (11.88% → 10.58%)
- Mobile conversion dropped 30% (11% → 7.75%)
- Desktop conversion remained stable at ~15%
- Organic traffic converts best at ~13%
- Root cause: Mobile-specific UX issue in Week 2

## Project Structure
```
signup-conversion-analysis/
├── data/
│   └── user_sessions.csv      # 10,000 user sessions
├── sql_queries/
│   └── analysis_queries.sql   # 5 key analysis queries
├── python_scripts/
│   ├── generate_data.py       # Generates simulated data
│   ├── load_data_to_mysql.py  # Loads data into MySQL
│   └── export_for_tableau.py  # Exports data for Tableau
└── report/
    └── Analysis_Report.pdf    # Full analysis report
```

## SQL Analysis Highlights

### Overall Conversion by Week
```sql
SELECT 
    week_number,
    COUNT(*) as total_sessions,
    SUM(signup_completed) as total_signups,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) 
    as conversion_rate
FROM user_sessions
GROUP BY week_number;
```

### Device Performance Analysis
```sql
SELECT 
    device_type,
    week_number,
    COUNT(*) as sessions,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) 
    as conversion_rate
FROM user_sessions
GROUP BY device_type, week_number
ORDER BY device_type, week_number;
```

## Key Recommendations
1. Investigate mobile UX changes deployed in Week 2
2. Audit mobile signup form for usability issues
3. Set up automated alerts for device-specific conversion drops
4. Invest more in organic traffic (highest conversion at 13%)

## Dashboard
[View Interactive Tableau Dashboard](#) 
(https://public.tableau.com/app/profile/suhitha.reddy.somu/viz/SignupConversionAnalysis-Project/Dashboard1)

## Contact
https://www.linkedin.com/in/suhitha-somu/
