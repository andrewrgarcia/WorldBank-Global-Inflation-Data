# Examples for WorldBank-Global-Inflation-Data

This directory contains simple scripts that demonstrate how to work with the inflation datasets provided in both SQLite and CSV formats. If you're looking for a quick way to get started or just want to see working code before pretending you understand pandas, you're in the right place.

## What's Included

* `sql_queries.py`:
  Shows how to query the SQLite database, filter by country, and plot the results using `matplotlib`.

* `csv_queries.py`:
  Reads a CSV file, filters it by country code, and plots the time series. Same goal as above, just with less database.

* `show.txt`:
  Currently empty. It's there to remind you that sometimes, life has placeholders too.

## Notes on Data Coverage

While the database and CSVs are structured to include all expected tables, some countries may be missing from certain datasets. Data completeness varies by file. This is normal, frustrating, and very on-brand for real-world data.

## Requirements

* Python 3.x
* `pandas`
* `matplotlib`
* `sqlite3` (included with Python)

Install missing packages with:

```bash
pip install pandas matplotlib
```

## Running the Scripts

From this directory, run:

```bash
python sql_queries.py
```

or

```bash
python csv_queries.py
```

Each script will display a plot based on inflation data for the selected country.

