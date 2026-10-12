# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT

# Warehouse audit schedule for a 30-day month

total_days = 30
cycle_count_interval = 3
scanner_audit_interval = 5

# Check both conditions first because some days need a full audit.
for day in range(1, total_days + 1):
    if day % cycle_count_interval == 0 and day % scanner_audit_interval == 0:
        print(f"Day {day}: FULL AUDIT")
    elif day % cycle_count_interval == 0:
        print(f"Day {day}: Cycle count")
    elif day % scanner_audit_interval == 0:
        print(f"Day {day}: Scanner audit")
    else:
        print(f"Day {day}: Normal operations")