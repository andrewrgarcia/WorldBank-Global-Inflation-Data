import pandas as pd 
import matplotlib.pyplot as plt

"""
(base) andrew@punchparty:~/WorldBank-Global-Inflation-Data/data$ ls
Aggregate_Annual_Average_Inflation.csv  GDP_Deflator_Growth_Rate_Annual.csv
Core_CPI_Inflation_Annual.csv           GDP_Deflator_Index_Quarterly.csv
Core_CPI_Monthly.csv                    Headline_CPI_Annual.csv
Core_CPI_Quarterly.csv                  Headline_CPI_Monthly.csv
Energy_Price_Index_Monthly.csv          Headline_CPI_Quarterly.csv
Energy_Price_Index_Quarterly.csv        Producer_Price_Index_Monthly.csv
Energy_Price_Inflation_Annual.csv       Producer_Price_Index_Quarterly.csv
Food_Price_Index_Monthly.csv            Producer_Price_Inflation_Annual.csv
Food_Price_Index_Quarterly.csv          README.md
Food_Price_Inflation_Annual.csv

Note: While CSV files exist for all expected data tables, some countries may be missing from specific files. Data availability varies by country and dataset.
"""

def worldbank_read(country_code='USA', csv_path='../data/Headline_CPI_Monthly.csv'):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Filter by country code
    filtered_df = df[df['Country Code'] == country_code]

    return filtered_df


df = worldbank_read("PER","../data/Headline_CPI_Monthly.csv")
print(df)

df.iloc[:,3] = df.iloc[:,3].astype(float)       # Data
df['Date'] = pd.to_datetime(df['Date'])         # Dates

plt.plot(df["Date"],df.iloc[:, 3])
plt.show()