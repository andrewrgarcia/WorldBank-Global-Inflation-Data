# WorldBank-Global-Inflation-Data

This repository contains processed [data](data) versions of the World Bank's ["_A Global Database of Inflation_"](https://www.worldbank.org/en/research/brief/inflation-database) inflation data. The information has been structured and cleaned for enhanced usability in AI, machine learning, and data science applications. No scripts or code are included in this repository; only the processed datasets are provided.

To access and use the data files in this repository:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/WorldBank-Global-Inflation-Data.git
   ```
   
2. **Navigate to the directory**:
   ```bash
   cd WorldBank-Global-Inflation-Data
   ```
   
## Explore the SQLite Database

Besides the .csv content found in the [data](data) directory, the data is also provided in SQLite format as `world_bank_inflation.db` for efficient querying and analysis. Below are some nifty functions to use for some data surfing. 

### Open the Database (Command Line):
   Use the SQLite command-line interface or any SQLite-compatible tool:
   ```bash
   sqlite3 world_bank_inflation.db
   ```

   ### List Available Tables (SQL Queries):
   ```sql
   .tables
   ```
   ### Retrieve all countries present for a specific table (SQL Queries):
   ```sql
   SELECT DISTINCT country_code, country FROM producer_price_index_quarterly_data;
   ```
   Replace `producer_price_index_quarterly_data` and `country_code, country` with the relevant table and column names for your analysis.

   ### Retrieve data from a specific country (SQL Queries):
   ```sql
   SELECT * FROM headline_cpi_monthly_data WHERE country_code = 'USA';
   ```

### Python Example:
   Use SQLite in Python with the `sqlite3` library:
   ```python
   import sqlite3

   # Connect to the database
   conn = sqlite3.connect('world_bank_inflation.db')
   cursor = conn.cursor()

   # Execute a query
   cursor.execute("SELECT * FROM headline_cpi_monthly_data WHERE country_code = 'USA'")
   rows = cursor.fetchall()

   # Close the connection
   conn.close()
   ```

### Example Scripts

For clear, code-ready demonstrations of how to load, filter, and work with both the CSV files and the SQLite database, please check out the [`examples/`](examples) directory. These snippets illustrate how to treat the data programmatically using Python and pandas, including caveats about partial country coverage across datasets.

## About the Data

- **Source**: [The World Bank’s Prospects Group Global Inflation Database (April 2024 version)](https://www.worldbank.org/en/research/brief/inflation-database).
- **Coverage**: Up to 209 countries from 1970 to 2023.
- **Included Measures**:
  - Headline consumer price index (CPI) inflation
  - Food CPI inflation
  - Energy CPI inflation
  - Core CPI inflation
  - Producer price index inflation
  - Gross domestic product deflator

The database also provides aggregate inflation for global, advanced-economy, and emerging market and developing economies, as well as measures of global commodity prices.

## Citation

If you use this data, please cite the original source, the [research paper](https://www.sciencedirect.com/science/article/abs/pii/S0261560623000979) by Jongrim Ha, M. Ayhan Kose, and Franziska Ohnsorge:

> Ha, Jongrim, M. Ayhan Kose, and Franziska Ohnsorge (2023). "One-Stop Source: A Global Database of Inflation." Journal of International Money and Finance 137 (October): 102896.

## Disclaimer

The findings, interpretations, and conclusions expressed in the processed datasets are those of the original authors and do not necessarily represent the views of the World Bank or its affiliated organizations.

## License

The data in this repository is derived from publicly available sources provided by the World Bank. While this repository is licensed under the [MIT License](LICENSE), please ensure any usage complies with the World Bank's data access and citation policies. The MIT license applies solely to the organization and presentation of the data files, not to the data content, which remains the intellectual property of the World Bank.
