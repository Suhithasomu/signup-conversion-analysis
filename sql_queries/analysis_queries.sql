SELECT * FROM user_sessions LIMIT 5;
#Did conversion really drop from Week 1 to Week 2?

SELECT 
    week_number,
    COUNT(*) as total_sessions,
    SUM(signup_completed) as total_signups,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) as conversion_rate_percent
FROM user_sessions
GROUP BY week_number
ORDER BY week_number;

#Is the drop happening on all devices, or just some?
SELECT 
    device_type,
    week_number,
    COUNT(*) as sessions,
    SUM(signup_completed) as signups,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) as conversion_rate
FROM user_sessions
GROUP BY device_type, week_number
ORDER BY device_type, week_number;

#Is paid traffic performing worse?
SELECT 
    traffic_source,
    COUNT(*) as sessions,
    SUM(signup_completed) as signups,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) as conversion_rate
FROM user_sessions
WHERE week_number = 2
GROUP BY traffic_source
ORDER BY conversion_rate DESC;

#Mobile-Specific Analysis (The Root Cause!)
SELECT 
    week_number,
    traffic_source,
    COUNT(*) as mobile_sessions,
    SUM(signup_completed) as signups,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) as conversion_rate
FROM user_sessions
WHERE device_type = 'mobile'
GROUP BY week_number, traffic_source
ORDER BY week_number, conversion_rate DESC;

#Landing Page Performance
SELECT 
    landing_page,
    device_type,
    COUNT(*) as sessions,
    SUM(signup_completed) as signups,
    ROUND(SUM(signup_completed) * 100.0 / COUNT(*), 2) as conversion_rate
FROM user_sessions
WHERE week_number = 2
GROUP BY landing_page, device_type
ORDER BY landing_page, device_type;

