# Q.11



import pandas as pd

# 1. Create a Series and print specified elements and length on one line
s = pd.Series(["Employee_1", "Employee_2", "Employee_3"], index=["a", "b", "c"])
print(s["b"], s.iloc[2], len(s))

# 2. Create a DataFrame from a list of dictionaries
df_dict = [{"item": "pen", "qty": 10}, {"item": "book", "qty": 4}, {"item": "bag", "qty": 2}]
df_items = pd.DataFrame(df_dict)
print(df_items)

# 3. Read CSV, print first 3 rows, shape, and column names as a list on one line
df = pd.read_csv("employees.csv")
print(df.head(3))
print(df.shape, list(df.columns))

# 4. Print number of duplicate rows, then number of missing values per column
print(df.duplicated().sum())
print(df.isnull().sum())

import pandas as pd

# -------------------------------------------------------------
# Optional: Creating 'employees.csv' if you don't have it yet
# -------------------------------------------------------------
data = {
    "EmpID": [101, 102, 103, 101, 104, 105, 106, 107, 108, 109, 110, 111],
    "Name": ["Asha", "Ravi", "Meena", "Asha", "John", "Sara", "Ali", "Raj", "Priya", "Amit", "Neha", "Kiran"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR", "IT", "Finance", "Sales", "HR", "IT", "Finance"],
    "City": ["Pune", "Mumbai", "Pune", "Pune", "Delhi", "Delhi", "Mumbai", "Pune", "Mumbai", "Delhi", "Pune", "Mumbai"],
    "JoinDate": ["2019-03-12", "2020-07-01", "2018-11-20", "2019-03-12", "2021-01-10", "2022-05-14", "2020-11-11", "2019-08-19", "2021-03-04", "2020-12-01", "2022-02-02", "2021-06-06"],
    "Salary": [60000.0, 45000.0, 52000.0, 60000.0, 48000.0, 50000.0, 55000.0, 47000.0, 53000.0, 49000.0, 51000.0, 54000.0],
    "Bonus": [5000, 2000, "pending", 5000, 3000, 2500, 4000, 3500, 2000, 1500, 2500, 3000]
}
df_temp = pd.DataFrame(data)
df_temp.to_csv("employees.csv", index=False)


# -------------------------------------------------------------
# Main Assignment Code
# -------------------------------------------------------------

# 1. Create a Series and print specified elements and length on one line[cite: 4]
s = pd.Series(["Employee_1", "Employee_2", "Employee_3"], index=["a", "b", "c"])
print(s["b"], s.iloc[2], len(s))

# 2. Create a DataFrame from a list of dictionaries[cite: 4]
df_dict = [{"item": "pen", "qty": 10}, {"item": "book", "qty": 4}, {"item": "bag", "qty": 2}]
df_items = pd.DataFrame(df_dict)
print(df_items)

# 3. Read CSV, print first 3 rows, shape, and column names as a list on one line[cite: 4]
df = pd.read_csv("employees.csv")
print(df.head(3))
print(df.shape, list(df.columns))

# 4. Print number of duplicate rows, then number of missing values per column[cite: 4]
print(df.duplicated().sum())
print(df.isnull().sum())
print("----------------------------------------------------------------------------------------------------------------------------------")

# Q.12

import pandas as pd

# 1. Remove duplicate rows[cite: 5]
df = df.drop_duplicates()

# 2. Convert Bonus to numeric, fill missing values with 0, and convert to int[cite: 5]
df["Bonus"] = pd.to_numeric(df["Bonus"], errors="coerce").fillna(0).astype(int)

# 3. Fill missing Salary with mean rounded to whole number and convert to int (without inplace=True)[cite: 5]
fill_value = int(round(df["Salary"].mean()))
df["Salary"] = df["Salary"].fillna(fill_value).astype(int)

# 4. Convert JoinDate to datetime and add Year, Weekday, and Years columns[cite: 5]
df["JoinDate"] = pd.to_datetime(df["JoinDate"])
df["Year"] = df["JoinDate"].dt.year
df["Weekday"] = df["JoinDate"].dt.day_name()
df["Years"] = (pd.Timestamp("2026-01-01") - df["JoinDate"]).dt.days // 365

# 5. Print the fill value, shape, dtypes of Salary and Bonus on one line, then first 4 rows[cite: 5]
print(fill_value, df.shape, df["Salary"].dtype, df["Bonus"].dtype)
print(df[["EmpID", "Year", "Weekday", "Years"]].head(4))


print("--------------------------------------------------------------------------------------------------------------------")

# Q.13

import pandas as pd

# 1. Add the column Net = Salary + Bonus[cite: 6]
df["Net"] = df["Salary"] + df["Bonus"]

# 2. Print EmpID, Name and Net where Department is 'IT' and Net > 50000[cite: 6]
print(df.loc[(df["Department"] == "IT") & (df["Net"] > 50000), ["EmpID", "Name", "Net"]])

# 3. Print type names of df["Name"] and df[["Name"]] on one line; then loc and iloc values on one line[cite: 6]
print(type(df["Name"]).__name__, type(df[["Name"]]).__name__)
print(df.loc[0, "Name"], df.iloc[1, 1])

# 4. Write band function, add Band column with apply, and convert to ordered Categorical[cite: 6]
def band(n):
    if n >= 65000:
        return "High"
    elif n >= 50000:
        return "Mid"
    else:
        return "Low"

df["Band"] = df["Net"].apply(band)
df["Band"] = pd.Categorical(df["Band"], categories=["Low", "Mid", "High"], ordered=True)

# 5. Sort by Band descending (highest first) and EmpID ascending, then print first 4 rows and value_counts[cite: 6]
sorted_df = df.sort_values(by=["Band", "EmpID"], ascending=[False, True])
print(sorted_df[["EmpID", "Band"]].head(4))
print(df["Band"].value_counts().sort_index())

print("------------------------------------------------------------------------------------------------------------------------------------------")

# Q.14

import pandas as pd

# 1. Group by Department, find mean, max, and count of Salary rounded to 1 decimal, sorted by mean descending[cite: 7]
grouped = df.groupby("Department")["Salary"].agg(mean="mean", max="max", count="count")
print(grouped.round(1).sort_values(by="mean", ascending=False))

# 2. Add PctOfGroup as percentage of group's total Salary, rounded to 1 decimal, and print first 4 rows[cite: 7]
df["PctOfGroup"] = round((df["Salary"] / df.groupby("Department")["Salary"].transform("sum")) * 100, 1)
print(df[["EmpID", "Department", "PctOfGroup"]].head(4))

# 3. Create a pivot table with Department as rows, City as columns, sum of Salary as values, and 0 for empty cells[cite: 7]
pivot_tbl = pd.pivot_table(df, values="Salary", index="Department", columns="City", aggfunc="sum", fill_value=0)
print(pivot_tbl)

print ("---------------------------------------------------------------------------------------------------------------------------------------")

import pandas as pd

# 1. Read heads.csv, merge with df using left join on Department, print missing Head values and shape[cite: 9]
heads_df = pd.read_csv("heads.csv")
merged_left = pd.merge(df, heads_df, on="Department", how="left")
print(merged_left["Head"].isnull().sum(), merged_left.shape)

# 2. Do inner and outer merge and print the number of rows of each on one line[cite: 9]
merged_inner = pd.merge(df, heads_df, on="Department", how="inner")
merged_outer = pd.merge(df, heads_df, on="Department", how="outer")
print(len(merged_inner), len(merged_outer))

# 3. Set EmpID as index, print name for EmpID 106, reset index, rename Salary, print first 6 columns[cite: 9]
df = df.set_index("EmpID")
print(df.loc[106, "Name"])
df = df.reset_index().rename(columns={"Salary": "Monthly Salary"})
print(list(df.columns[:6]))

# 4. Save EmpID and Name to names.json, read it back, and print its shape[cite: 9]
df[["EmpID", "Name"]].to_json("names.json", orient="records")
json_df = pd.read_json("names.json")
print(json_df.shape)


import pandas as pd

# Create the heads.csv file with department heads
heads_data = {
    "Department": ["IT", "HR", "Finance", "Sales"],
    "Head": ["Alice", "Bob", "Charlie", "David"]
}

heads_df = pd.DataFrame(heads_data)
heads_df.to_csv("heads.csv", index=False)

print("Successfully created 'heads.csv'!")



import pandas as pd

# 0. Generate 'heads.csv' if it doesn't exist yet
pd.DataFrame({
    "Department": ["IT", "HR", "Finance", "Sales"],
    "Head": ["Alice", "Bob", "Charlie", "David"]
}).to_csv("heads.csv", index=False)

# 1. Read heads.csv, merge with df using left join on Department, print missing Head values and shape[cite: 9]
heads_df = pd.read_csv("heads.csv")
merged_left = pd.merge(df, heads_df, on="Department", how="left")
print(merged_left["Head"].isnull().sum(), merged_left.shape)

# 2. Do inner and outer merge and print the number of rows of each on one line[cite: 9]
merged_inner = pd.merge(df, heads_df, on="Department", how="inner")
merged_outer = pd.merge(df, heads_df, on="Department", how="outer")
print(len(merged_inner), len(merged_outer))

# 3. Set EmpID as index, print name for EmpID 106, reset index, rename Salary, print first 6 columns[cite: 9]
df = df.set_index("EmpID")
print(df.loc[106, "Name"])
df = df.reset_index().rename(columns={"Salary": "Monthly Salary"})
print(list(df.columns[:6]))

# 4. Save EmpID and Name to names.json, read it back, and print its shape[cite: 9]
df[["EmpID", "Name"]].to_json("names.json", orient="records")
json_df = pd.read_json("names.json")
print(json_df.shape)