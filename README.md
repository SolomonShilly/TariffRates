## Analysis of Tariff Rates and Government Debt from 1901 - 2024/25

### Visualizations
- TariffRates.twbx
- Area chart with annotations is a replication of Irina Ivanova and Doug Chayka's work in "How to Survive a Trade War" from Fortune Magazine
- Treemap was done to find comparable tariff rates to 2025. 1922 and 1939 were the closest
- U.S. tariff rates are reaching peaks that have not been seen in almost a century
- Line chart on U.S. outstanding debt from 1901 - 2024
- Double Line Chart comparing the movement of U.S. outstanding debt to tariff rates

### Data Scraper
- TariffScraper.py
- Tariff data scraped from https://www.visualcapitalist.com/the-average-u-s-tariff-rate-since-1890/ (Dorothy Neufeld's Chart: The Average U.S. Tariff Rate (1890-2025))
- Selenium was used to automate data scraping

### Data Cleaning
- Historical debt outstanding data was downloaded from https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/historical-debt-outstanding
- Pandas was used to handle original file, rename columns, and convert dates to years

### Data File
- Tariff Data was saved to TariffRates.csv
- Debt Data was saved to GovDebt.csv
