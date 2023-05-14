# csv-to-sqlscript
This script reads data from a CSV file, replaces NaN values with NULL, and generates SQL INSERT statements. The SQL statements are written to a file named `script.sql`.

## Requirements
- Python 3
- pandas
- NumPy

## Usage
1. Place the input CSV file named `data.csv` in the same directory as the script.
2. Replace the `table_name` in the SQL statement with the desired table name.
3. Run the script. The generated SQL statements will be written to a file named `script.sql` in the same directory as the script.

## Notes
- This script assumes that the input CSV file is encoded with UTF-8.
- This script uses the `itertuples()` method, which is faster than the `iterrows()` method for iterating through rows in a pandas dataframe.
- The generated SQL statements use NULL for any missing or empty values in the dataframe.