import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt

"""
(base) andrew@punchparty:~/WorldBank-Global-Inflation-Data$ sqlite3 world_bank_inflation.db
SQLite version 3.41.2 2023-03-22 11:56:21
Enter ".help" for usage hints.
sqlite> .tables
core_cpi_inflation_annual_data        gdp_deflator_growth_rate_annual_data
core_cpi_monthly_data                 gdp_deflator_index_quarterly_data   
core_cpi_quarterly_data               headline_cpi_annual_data            
energy_price_index_annual_data        headline_cpi_monthly_data           
energy_price_index_monthly_data       headline_cpi_quarterly_data         
energy_price_index_quarterly_data     producer_price_index_monthly_data   
food_price_index_monthly_data         producer_price_index_quarterly_data 
food_price_index_quarterly_data       producer_price_inflation_annual_data
food_price_inflation_annual_data    

Note: While these tables are part of the database schema, not every country has data available in all of them. Missing entries may occur.
"""

def worldbank_query(country_code='USA', table='headline_cpi_monthly_data'):
    # Connect to the database
    conn = sqlite3.connect('../world_bank_inflation.db')

    # Filter by country code
    query = f"SELECT * FROM {table} WHERE country_code = '{country_code}'"
    df = pd.read_sql_query(query, conn)
    
    conn.close()

    return df

df = worldbank_query("ISR","energy_price_index_annual_data")
print(df)

df.iloc[:,3] = df.iloc[:,3].astype(float)       # Data
df['date'] = pd.to_datetime(df['date'])         # Dates

plt.plot(df["date"], df.iloc[:,3])
plt.show()