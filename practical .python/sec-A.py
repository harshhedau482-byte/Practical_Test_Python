# Q.1
from datetime import datetime, timedelta

# 1. Leap year function and test list
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

for year in [1900, 2000, 2024, 2023, 2100]:
    print(year, is_leap_year(year))


# 2. Day of the week function and test list
def day_of_week(text):
    dt = datetime.strptime(text, "%Y-%m-%d")
    return dt.strftime("%A")

for date_str in ['2026-01-01', '2026-03-08', '2026-12-25']:
    print(date_str, day_of_week(date_str))


# 3. Number of days between two dates
date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 12, 31)
print((date2 - date1).days)


# 4. Specific datetime formatting
now = datetime(2026, 3, 8, 14, 30, 45)
print(now.strftime("%d-%m-%Y %m/%d/%Y"))
print(now.strftime("%H:%M:%S %I:%M:%S %p"))


# 5. Add timedelta (2 weeks, 3 days, and 5 hours) to now
future_time = now + timedelta(weeks=2, days=3, hours=5)
print(future_time.strftime("%Y-%m-%d %H:%M:%S"))

print("------------------------------------------------------------------------------------------------------------------")

# Q.2

import math
import random

# 1. A bus holds 10 passengers. Print how many buses are needed for 47 passengers (math.ceil).
buses = math.ceil(47 / 10)
print(buses)

# 2. Convert 3725 seconds to hours, minutes and seconds (use // and %) and print them on one line.
total_seconds = 3725
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(hours, minutes, seconds)

# 3. Write simplify(n, d) using math.gcd and print simplify(24, 36) as a tuple.
def simplify(n, d):
    common = math.gcd(n, d)
    return (n // common, d // common)

print(simplify(24, 36))

# 4. A tower is seen at an angle of 30 degrees from a point 50 m away. Print its height dist * tan(angle) using math.radians and math.tan, rounded to 2 decimals.
dist = 50
angle = math.radians(30)
height = dist * math.tan(angle)
print(round(height, 2))

# 5. Call random.seed(12); roll a die 5 times with random.randint(1, 6) into a list and print the list and its sum on one line.
random.seed(12)
dice_rolls = [random.randint(1, 6) for _ in range(5)]
print(dice_rolls, sum(dice_rolls))

# 6. Make deck = list(range(1, 9)), shuffle it with random.shuffle and print it. Then print random.choice(["rock", "paper", "scissors"]) (do not re-seed).
deck = list(range(1, 9))
random.shuffle(deck)
print(deck)
print(random.choice(["rock", "paper", "scissors"]))


print("--------------------------------------------------------------------------------------------------------------------")

# Q.3


import uuid
import time
from datetime import datetime, timezone

# --- Part 1 ---
names = ['Asha', 'Ravi', 'Meena', 'Karan']
ids = {name: uuid.uuid5(uuid.NAMESPACE_DNS, name.lower() + ".example") for name in names}

for name in names:
    print(f"{name} {str(ids[name])[:8]}")

# Check if all UUIDs are unique (comparing count of set of values to total length)
print(len(set(ids.values())) == len(ids))

# --- Part 2 ---
u3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
print(u3 != u5, u3.version, u5.version)

# --- Part 3 ---
ts = 31536000
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts)))
print(time.asctime(time.gmtime(ts)))
print(datetime.fromtimestamp(ts, timezone.utc).strftime("%d %b %Y"))

# --- Part 4 ---
start = time.perf_counter()
total_sum = sum(range(1_000_000))
end = time.perf_counter()

elapsed = end - start
print(total_sum, type(elapsed).__name__, elapsed >= 0)

print("-----------------------------------------------------------------------------------------------------------------------------")