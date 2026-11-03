# Python Standard Library Practice & Utilities

This repository contains practical examples and code snippets demonstrating the usage of various built-in and standard modules in Python, including `datetime`, `math`, `random`, `uuid`, and `time`.

---

## Table of Contents
- [Overview](#overview)
- [Code Structure & Breakdown](#code-structure--breakdown)
  - [Q.1: Date, Time, and Timedelta Operations (`datetime`)](#q1-date-time-and-timedelta-operations-datetime)
  - [Q.2: Mathematical Calculations and Randomness (`math`, `random`)](#q2-mathematical-calculations-and-randomness-math-random)
  - [Q.3: Unique Identifiers, Time Conversion, and Performance Measurement (`uuid`, `time`)](#q3-unique-identifiers-time-conversion-and-performance-measurement-uuid-time)
- [Requirements](#requirements)
- [Running the Code](#running-the-code)

---

## Overview

The scripts are divided into three main sections covering essential Python standard library features:
1. **Date & Time Management:** Determining leap years, calculating days between dates, parsing/formatting strings, and applying timedeltas.
2. **Math & Random Operations:** Ceiling division, time unit conversions, finding greatest common divisors, solving basic trigonometry, and generating pseudo-random numbers/shuffling.
3. **Identifiers & Performance Tracking:** Generating name-based UUIDs (v3/v5), handling epoch timestamps, and measuring execution time with high precision.

---

## Code Structure & Breakdown

### Q.1: Date, Time, and Timedelta Operations (`datetime`)
* **Leap Year Verification:** Custom logic checking divisibility rules (`% 400`, `% 100`, `% 4`).
* **Day of the Week Extraction:** Formatting dates using `strptime` and `strftime`.
* **Date Arithmetic:** Subtracting dates to find duration in days and adding a `timedelta` (weeks, days, hours) to a specific timestamp.

### Q.2: Mathematical Calculations and Randomness (`math`, `random`)
* **Ceiling & Division:** Using `math.ceil()` to compute container capacity and floor division (`//`) with modulo (`%`) to break down seconds into hours, minutes, and seconds.
* **Simplifying Fractions:** Utilizing `math.gcd()` to simplify rational numbers into tuples.
* **Trigonometry:** Calculating building/tower height using `math.radians()` and `math.tan()`.
* **Randomness & Shuffling:** Seeded generation of die rolls, list comprehension, and shuffling a list/choosing random elements from a sequence.

### Q.3: Unique Identifiers, Time Conversion, and Performance Measurement (`uuid`, `time`)
* **Deterministic UUIDs:** Creating namespace-based UUIDs (`uuid5`) for a list of names and verifying uniqueness. Comparing version 3 and version 5 UUIDs.
* **Timestamp Formatting:** Converting epoch timestamps (`31536000`) into readable UTC dates and strings using `time` and `datetime`.
* **Performance Counter:** Benchmarking the execution time of summing a large range (`sum(range(1_000_000))`) using `time.perf_counter()`.

---

## Requirements

* **Python:** Version 3.x (No external third-party libraries or `pip` installations are required since all modules belong to the Python Standard Library).

---

## Running the Code

You can run each section individually or combine them into a single Python file:

```bash
python script.py

---

 Code Structure & Breakdown (Continued)

### Q.4: File System Operations (`os`, `shutil`)
* **Directory Creation & Management:** Using `os.makedirs(..., exist_ok=True)` to safely create nested directory structures (`proj/logs`) without raising errors if they already exist.
* **File I/O:** Writing sample `.txt` and `.csv` files (`a.txt`, `b.txt`, `c.csv`) and reading line counts and content from them.
* **File Filtering & Listing:** Filtering directory contents via list comprehensions (`os.listdir`) to find and sort specific file extensions (e.g., `.txt`).
* **Moving & Renaming:** Utilizing `shutil.move()` to relocate files between directories (`logs` to `archive`) and `os.rename()` to rename files in place.
* **Cleanup (`shutil.rmtree`):** Completely deleting directories and subtrees recursively, verifying deletion with `os.path.exists()`.

### Q.5: Modular Script Design (`datetools` pattern)
* **Constants & Encapsulation:** Defining module-level constants (like `DATE_FORMAT`) and helper functions for date checking and day name extraction.
* **Direct Execution Safeguard:** Using the standard Python idiom `if __name__ == "__main__":` to ensure testing code runs only when the script is executed directly rather than imported as a module.

---

## Updated README Integration Example

If you choose to merge all five parts into a single monolithic script or handle them as separate modules, your project overview will look like this:
---

## Code Structure & Breakdown (Continued)

### Q.7: NumPy Array Creation & Initialization (`numpy`)
* **Range-based Arrays:** Using `np.arange(start, stop, step)` to create sequences with defined steps.
* **Specialized Arrays:** Initializing arrays of zeros, ones with specific data types (`dtype=float`), and identity matrices (`np.eye()`) scaled by a factor.
* **Linearly Spaced Data:** Generating evenly spaced numbers over a specified range using `np.linspace()`.
* **Random Sampling & Slicing:** Seeding the random number generator (`np.random.seed()`), generating 2D random integer matrices (`np.random.randint()`), modifying rows, and slicing sub-blocks (e.g., bottom-right $2 \times 2$ matrices).

### Q.8: Advanced Indexing & Boolean Masking (`numpy`)
* **Boolean Filtering:** Extracting elements satisfying specific conditions (e.g., ages $\ge 18$, strict ranges using logical operators like `&`, or negation `~`).
* **Conditional Substitution:** Using `np.where()` to assign categorical strings ("Pass" / "Fail") based on numerical thresholds.
* **In-place Updates & Views vs. Copies:** Modifying values using boolean masks, understanding memory sharing via array views (`mat[0]`), and ensuring independence via `.copy()`.
* **2D Slicing:** Extracting specific sub-grids from multi-dimensional arrays (e.g., rows 1–3, columns 2–4).

### Q.9: Mathematical, Statistical & Linear Algebra Operations (`numpy`)
* **Matrix Operations:** Performing element-wise multiplication, division (with rounding), and true matrix multiplication (`@`).
* **Standardization (Z-scores):** Centering and scaling data using `.mean()` and `.std()`, followed by rounding.
* **Linear Algebra & Geometry:** Calculating Euclidean distances between coordinate points using vector subtraction and `np.sqrt(np.sum(...))`.
* **Descriptive Statistics:** Finding extreme values (`argmax`, `argmin`, `max`, `min`), calculating measures of central tendency and dispersion (mean, median, variance, standard deviation).
* **Sorting & Counting:** Sorting multi-dimensional arrays along specific axes (`axis=0`, `axis=1`) and counting conditional elements (positive, negative, zero values).
 Q.10: Reshaping, Broadcasting & Splitting (`numpy`)
* **Reshaping & Flattening:** Using automatic dimension inference (`-1`) in `.reshape()` and flattening arrays back to 1D lists.
* **Broadcasting Mechanics:** Adding columns/rows with mismatched shapes using `np.newaxis` and scaling matrices element-wise against 1D rate vectors.
* **Safe Array Splitting:** Handling `ValueError` exceptions when splitting arrays unevenly using `np.split()`, and using `np.array_split()` for safe handling of unequal partitions.

---

## Complete Project Structure Overview

With all parts integrated, your project file layout looks like this:

---

## Code Structure & Breakdown (Continued)

### Q.11: Pandas Basics & Data Loading (`pandas`)
* **Series & DataFrames:** Creating labeled Series with custom indices and constructing DataFrames from dictionaries.
* **CSV Import & Inspection:** Loading external data via `pd.read_csv()`, checking dimensions (`.shape`), inspecting column headers, checking for duplicate rows (`.duplicated()`), and identifying missing values (`.isnull()`).
* **Synthetic Data Setup:** Includes embedded helper scripts to generate sample datasets (`employees.csv`) for testing pipeline logic.

### Q.12: Data Cleaning & Transformation (`pandas`)
* **Duplicate Removal & Type Conversion:** Dropping duplicate records and coercing columns into proper data types using `pd.to_numeric(..., errors="coerce")`.
* **Missing Value Imputation:** Filling missing values in numerical columns (e.g., calculating mean salary, rounding, casting to integers).
* **Datetime Parsing:** Converting date strings into datetime objects via `pd.to_datetime()` to extract components like year, weekday name, and elapsed duration.

### Q.13: Advanced Filtering, Application & Categorization (`pandas`)
* **Feature Engineering:** Creating derived columns (e.g., `Net = Salary + Bonus`).
* **Conditional Masking (`loc`):** Filtering DataFrames based on multiple criteria (e.g., department matching and salary thresholds).
* **Custom Mappings & Categoricals:** Using `.apply()` with custom functions to assign performance bands, and converting string tiers into ordered categorical data types (`pd.Categorical(..., ordered=True)`).
* **Multi-level Sorting:** Sorting DataFrames by categorical columns descending and ID columns ascending.

### Q.14: Aggregations & Pivot Tables (`pandas`)
* **Group Operations (`groupby`):** Calculating multi-metric summary statistics (`mean`, `max`, `count`) using `.agg()` and sorting results.
* **Transformations:** Computing group-wise proportions (percentage of department total) using `.transform("sum")`.
* **Pivot Tables:** Reshaping data into multi-dimensional matrices using `pd.pivot_table()` with custom aggregation functions and fill values.

### Q.15: Joins, Indexing & Serialization (`pandas`)
* **Relational Joins (`merge`):** Combining datasets using left, inner, and outer joins (`pd.merge()`) to handle department head mapping.
* **Index Manipulation:** Setting and resetting custom indices (`set_index`, `reset_index`) and renaming columns in-place (`.rename()`).
* **JSON Persistence:** Exporting DataFrames to JSON format (`to_json()`) and reloading them back (`read_json()`).

---

## Final Project Structure Overview

With all parts fully integrated (Standard Library, NumPy, and Pandas modules), your complete project layout looks like this:

Your name :
Harsh Hedau
