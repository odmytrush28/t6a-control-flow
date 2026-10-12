# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start

# Print the numbers for 10 scanner checks
for check in range(1, 11):
    minutes = check * 15
    print(f"Check {check}: {minutes} minutes after shift start")
    # Each scanner is checked every 15 minutes.
check_interval = 15

# Calculate the time for each of the 10 checks.
for check_number in range(1, 11):
    minutes_after_start = check_number * check_interval
    print(f"Check {check_number}: {minutes_after_start} minutes after shift start")