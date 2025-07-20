# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters

# Register converters to avoid Matplotlib warnings
register_matplotlib_converters()

# --------------------------------------------
# Load DataFrames from CSV files
# --------------------------------------------

# Load Tesla data
tesla_dataframe = pd.read_csv('tesla_dataframe Search Trend vs Price.csv')
tesla_dataframe.describe()  # Show summary statistics

# Load Unemployment data
unemployment_dataframe = pd.read_csv('UE Benefits Search vs UE Rate 2004-19.csv')
unemployment_dataframe.describe()

# Load daily Bitcoin price data
daily_bitcoin_dataframe = pd.read_csv('Daily Bitcoin Price.csv')
daily_bitcoin_dataframe.describe()

# Load Bitcoin search trend data
bitcoin_search_trend_dataframe = pd.read_csv('Bitcoin Search Trend.csv')
bitcoin_search_trend_dataframe.describe()

# --------------------------------------------
# Check for missing values
# --------------------------------------------

# .isna() returns a DataFrame of True/False values. .values.any() checks if any are True.
print(f'Is there any missing values for U/E?: {unemployment_dataframe.isna().values.any()}')
print(f'Is there any missing values for Tesla?: {tesla_dataframe.isna().values.any()}')
print(f'Is there any missing values for BTC Search?: {bitcoin_search_trend_dataframe.isna().values.any()}')
print(f'Is there any missing values for BTC daily Price?: {daily_bitcoin_dataframe.isna().values.any()}')

# Count how many missing values are in the Bitcoin price data
print(f'Missing values in Bitcoin daily price: {daily_bitcoin_dataframe.isna().values.sum()}')

# Check specifically for missing values in the 'CLOSE' column
print(daily_bitcoin_dataframe.CLOSE.isna())

# Drop rows with missing values from Bitcoin data
daily_bitcoin_dataframe.dropna(inplace=True)

# --------------------------------------------
# Convert date columns to datetime objects
# --------------------------------------------

tesla_dataframe['MONTH'] = pd.to_datetime(tesla_dataframe['MONTH'])
bitcoin_search_trend_dataframe['MONTH'] = pd.to_datetime(bitcoin_search_trend_dataframe['MONTH'])
unemployment_dataframe['MONTH'] = pd.to_datetime(unemployment_dataframe['MONTH'])
daily_bitcoin_dataframe['DATE'] = pd.to_datetime(daily_bitcoin_dataframe['DATE'])

# --------------------------------------------
# Resample Bitcoin daily data to monthly frequency
# --------------------------------------------

# Use resample() to convert daily data into monthly data using the last value of each month
bitcoin_monthly_dataframe = daily_bitcoin_dataframe.resample('M', on='DATE').last()

# --------------------------------------------
# Plot Tesla stock price and search trend
# --------------------------------------------

axis1 = plt.gca()
axis2 = axis1.twinx()

plt.xticks(fontsize=12, rotation=50)
axis1.set_ylabel("Stock Price TESLA", fontsize=15, color="black")

axis1.plot(tesla_dataframe.MONTH, tesla_dataframe.TSLA_USD_CLOSE, linewidth=2, color="#FF6B6B")

plt.yticks(fontsize=12)
axis2.set_ylabel("Search Trend", fontsize=15, color="black")

axis2.plot(tesla_dataframe.MONTH, tesla_dataframe.TSLA_WEB_SEARCH, linewidth=2, color="black")

plt.tight_layout()
axis1.set_xlim([tesla_dataframe.MONTH.min(), tesla_dataframe.MONTH.max()])
axis1.set_ylim([0, 600])
plt.title("Tesla Stock Price Line Chart")
plt.show()

# --------------------------------------------
# Format time axis using locators and formatters
# --------------------------------------------

# Define locators and formatters
months = mdates.MonthLocator()
years = mdates.YearLocator()
formatted_years = mdates.DateFormatter('%Y')

# Apply to chart axis (this part only sets it up; apply in plotting)
# Example:
# axis1.xaxis.set_major_locator(years)
# axis1.xaxis.set_major_formatter(formatted_years)
# axis1.xaxis.set_minor_locator(months)

# --------------------------------------------
# Plot Bitcoin price vs search trend
# --------------------------------------------

plt.figure(figsize=(15, 7), dpi=130)
plt.title('Bitcoin News - Resampled Price', fontsize=15)
plt.xticks(fontsize=12, rotation=50)

axis_one = plt.gca()
axis_two = axis_one.twinx()

axis_one.set_ylabel('Bitcoin Price', color='black', fontsize=12)
axis_two.set_ylabel('Trend Search', color='black', fontsize=12)

axis_one.xaxis.set_major_locator(years)
axis_one.xaxis.set_major_formatter(formatted_years)
axis_one.xaxis.set_minor_locator(months)

axis_one.set_ylim(bottom=0, top=15000)
axis_one.set_xlim([bitcoin_monthly_dataframe.index.min(), bitcoin_monthly_dataframe.index.max()])

axis_one.plot(bitcoin_monthly_dataframe.index, bitcoin_monthly_dataframe.CLOSE,
              color='#F2A900', linewidth=2, linestyle='-')

axis_two.plot(bitcoin_search_trend_dataframe.MONTH, bitcoin_search_trend_dataframe.BTC_NEWS_SEARCH,
              color='black', linewidth=2, marker='o')

plt.show()

# --------------------------------------------
# Plot Unemployment rate vs web search interest
# --------------------------------------------

plt.figure(figsize=(15, 7), dpi=130)
plt.title('Official Unemployment Rate in the US vs Benefits Search', fontsize=16)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15, rotation=50)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.set_ylabel('Unemployment Rate (FRED)', color='black', fontsize=13)
ax2.set_ylabel('Search Trend', color='black', fontsize=13)

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(formatted_years)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylim(3, 10.5)
ax1.set_xlim([unemployment_dataframe.MONTH.min(), unemployment_dataframe.MONTH.max()])

ax1.grid(color='black', linestyle='--')

ax1.plot(unemployment_dataframe.MONTH, unemployment_dataframe.UNRATE, color='red', linewidth=2, linestyle='--')
ax2.plot(unemployment_dataframe.MONTH, unemployment_dataframe.UE_BENEFITS_WEB_SEARCH, color='#004080', linewidth=2)

plt.show()

# --------------------------------------------
# Rolling average (smoothing) visualization
# --------------------------------------------

plt.figure(figsize=(15, 7), dpi=130)
plt.title('Rolling Monthly Unemployment in US vs UNRATE', fontsize=16)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15, rotation=50)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(formatted_years)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel('Unemployment Rate', color='black', fontsize=15)
ax2.set_ylabel('Search Trend', color='black', fontsize=15)

ax1.set_ylim(3, 10)
ax1.set_xlim([unemployment_dataframe.MONTH[0], unemployment_dataframe.MONTH.max()])

# Calculate rolling average over 6 months
rolling_df = unemployment_dataframe[['UE_BENEFITS_WEB_SEARCH', 'UNRATE']].rolling(window=6).mean()

ax1.plot(unemployment_dataframe.MONTH, rolling_df.UNRATE, color='black', linewidth=2, linestyle='-.')
ax2.plot(unemployment_dataframe.MONTH, rolling_df.UE_BENEFITS_WEB_SEARCH, color='darkgreen', linewidth=2)

plt.show()

# --------------------------------------------
# Add 2020 data and visualize impact
# --------------------------------------------

# Load updated dataset with 2020 data
unemployment_2020_dataframe = pd.read_csv('UE Benefits Search vs UE Rate 2004-20.csv')
unemployment_2020_dataframe['MONTH'] = pd.to_datetime(unemployment_2020_dataframe['MONTH'])

plt.figure(figsize=(15, 7), dpi=130)
plt.title('Monthly US Unemployment Benefits vs UNRATE - INCLUDING 2020', fontsize=16)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15, rotation=50)

ax1 = plt.gca()
ax2 = ax1.twinx()

ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(formatted_years)
ax1.xaxis.set_minor_locator(months)

ax1.set_ylabel('Unemployment Rate', color='black', fontsize=15)
ax2.set_ylabel('Trend Search', color='black', fontsize=15)

ax1.set_xlim([unemployment_2020_dataframe.MONTH.min(), unemployment_2020_dataframe.MONTH.max()])

ax1.plot(unemployment_2020_dataframe.MONTH, unemployment_2020_dataframe.UNRATE,
         color='black', linewidth=2, linestyle='-.')
ax2.plot(unemployment_2020_dataframe.MONTH, unemployment_2020_dataframe.UE_BENEFITS_WEB_SEARCH,
         color='beige', linewidth=2)

plt.show()
