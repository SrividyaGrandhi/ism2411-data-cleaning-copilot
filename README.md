What the script does:
Standardizes column names (lowercase, underscores, no extra spaces)
Strips whitespace and removes extra quotes from product/category text
Converts price and qty to numeric values
Drops rows with missing price or quantity
Removes rows with negative price/quantity (invalid data)

How to run it
Make sure you have Python 3 installed
Install pandas (in terminal) (pip install pandas)
run python3 src/data_cleaning.py
This will create an updated sales_data_clean.csv in the data/processed/ folder and print the first few rows to the terminal.
