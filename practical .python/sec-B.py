# Q.4
import os
import shutil

# 1. Create proj/logs using os.makedirs twice with exist_ok=True[cite: 3]
logs_path = os.path.join("proj", "logs")
os.makedirs(logs_path, exist_ok=True)
os.makedirs(logs_path, exist_ok=True)

# 2. Inside logs write three files: a.txt, b.txt, and c.csv[cite: 3]
with open(os.path.join(logs_path, "a.txt"), "w") as f:
    f.write("alpha\nbeta")

with open(os.path.join(logs_path, "b.txt"), "w") as f:
    f.write("gamma")

with open(os.path.join(logs_path, "c.csv"), "w") as f:
    f.write("x,y\n1,2")

# 3. Print the sorted list of .txt files in logs[cite: 3]
txt_files = sorted([f for f in os.listdir(logs_path) if f.endswith(".txt")])
print(txt_files)

# 4. Read a.txt and print the number of lines and its first line on one line[cite: 3]
a_path = os.path.join(logs_path, "a.txt")
with open(a_path, "r") as f:
    lines = f.readlines()
print(len(lines), lines[0].strip())

# 5. Create proj/archive, move a.txt into it, and print listings[cite: 3]
archive_path = os.path.join("proj", "archive")
os.makedirs(archive_path, exist_ok=True)
shutil.move(a_path, os.path.join(archive_path, "a.txt"))
print(sorted(os.listdir(logs_path)), sorted(os.listdir(archive_path)))

# 6. Rename b.txt to old_b.txt and check existence/file type[cite: 3]
b_path = os.path.join(logs_path, "b.txt")
old_b_path = os.path.join(logs_path, "old_b.txt")
os.rename(b_path, old_b_path)
print(os.path.exists(b_path), os.path.isfile(old_b_path))

# 7. Delete proj completely and print whether it still exists[cite: 3]
proj_path = "proj"
shutil.rmtree(proj_path)
print(os.path.exists(proj_path))

print("-----------------------------------------------------------------------------------------------------------")

# Q.5

DATE_FORMAT = "%Y-%m-%d"

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return year % 4 == 0

def day_name(text):
    import datetime
    dt = datetime.datetime.strptime(text, DATE_FORMAT)
    return dt.strftime("%A")

if __name__ == "__main__":
    print("Testing datetools directly")
    print(is_leap_year(2024), day_name("2026-01-01"))
    
print("--------------------------------------------------------------------------------------------------------------------")

# Q.6


