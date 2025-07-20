# 📊 Data Trends Analysis with Python

This project is a personal data analysis exploration built as a student while following the **Udemy course by Dr. Angela Yu** from **The App Brewery**. It focuses on real-world datasets to visualize and understand time-series trends using Python, especially in areas like:

- Tesla stock price vs search trends  
- Bitcoin price vs Google search trends  
- U.S. unemployment rate vs benefits-related search behavior  

## 🛠️ Technologies Used

- **Python** (pandas, matplotlib)
- **pandas** for data wrangling and time-series resampling
- **matplotlib** for data visualization
- **Jupyter Notebook** (recommended environment)

## 📁 Datasets

The project uses several CSV datasets (manually downloaded or provided through the course):
- `tesla_dataframe Search Trend vs Price.csv`
- `UE Benefits Search vs UE Rate 2004-19.csv`
- `UE Benefits Search vs UE Rate 2004-20.csv`
- `Daily Bitcoin Price.csv`
- `Bitcoin Search Trend.csv`  

## 📈 Visualizations

Each section in the notebook visualizes a different relationship, helping explore correlations or highlight trends using real data. These include:
- Line charts with dual y-axes
- Rolling averages to smooth short-term noise
- Clear x-axis formatting with major/minor date locators

## 🎓 Credits

Built with guidance from the **"Python for Data Science and Machine Learning Bootcamp"** by **Dr. Angela Yu** and **The App Brewery**.

## 💡 Note

This is a beginner project for learning purposes. The datasets were cleaned manually and contain real-world imperfections to encourage better data handling skills.



### Data Analysis Learning Summary 🧠

As part of my journey in learning data analysis with Python, I’ve explored a variety of techniques using pandas and Matplotlib. Below is a concise summary of key concepts and tools I’ve practiced:

📈 Descriptive Stats & Missing Data
	•	.describe(): Instantly view summary statistics (mean, std, min, max, quartiles) for numerical columns in a DataFrame.
	•	.isna().values.sum(): Quickly count the total number of missing (NaN) values in a dataset.

⏱ Time Series Handling
	•	.resample(): Modify the frequency of time-series data (e.g., daily to monthly) to make it comparable across different time intervals.
	•	matplotlib.dates locators: Customize time-based x-axis ticks for better timeline styling—great for improving readability on time series plots.

🖼 Chart Styling & Customization
	•	Chart resolution: Adjust figure clarity with plt.figure(dpi=100) or any other dpi value to control sharpness.
	•	Line styles: Use linestyle='--' for dashed lines or linestyle='-.' for dotted-dashed lines to distinguish data visually.
	•	Markers: Enhance visibility by using different marker types (e.g., 'o' for circles, '^' for triangles) in line plots.
	•	Styling elements:
	•	Set axis limits: plt.xlim() / plt.ylim()
	•	Add axis labels and titles
	•	Customize linewidth and color using named colors or HEX codes like '#1f77b4'.
	•	.grid(): Enable grid lines to make it easier to detect seasonality or patterns across time in time series charts.
