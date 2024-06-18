# import pandas as pd
# import matplotlib.pyplot as plt

# # List of filenames
# filenames = ["2018.csv", "2019.csv", "2020.csv", "2021.csv", "2022.csv", "2023.csv", "2024.csv"]

# # Empty dictionary to store dataframes
# data_dict = {}

# # Loop through filenames, read data, and convert date
# for filename in filenames:
#   year = int(filename.replace(".csv", ""))  # Extract year from filename
#   data_dict[year] = pd.read_csv(filename)
#   data_dict[year]["DATE"] = pd.to_datetime(data_dict[year]["DATE"])  # Convert date to datetime format

# # Create the figure and plot
# plt.figure(figsize=(12, 6))

# # Loop through years and plot weekly average for each year
# for year, data in data_dict.items():
#   # Resample data by week and calculate weekly average
#   weekly_avg = data.resample("W-SUN", on="DATE")["WEEKLY AVG"].mean()
#   plt.plot(weekly_avg.index, weekly_avg, label=f"{year}")

# # Customize the plot
# plt.ylabel("Weekly Average")
# plt.xlabel("Date")
# plt.title("Weekly Average by Year")
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

# # Display the plot
# plt.tight_layout()
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Define a list to store dataframes from each CSV
dataframes = []

# Loop through each CSV file
for year in range(2018, 2025):
  filename = f"{year}.csv"
  
  # Read the CSV file and store in a dataframe
  df = pd.read_csv(filename)
  
  # Convert the "DATE" column to datetime format
  df["DATE"] = pd.to_datetime(df["DATE"])
  
  # Resample data by week and calculate weekly average
  df_weekly_avg = df.resample("W-SUN", on="DATE")["WEEKLY AVG"].mean()
  
  # Add dataframe to the list
  dataframes.append(df_weekly_avg)

# Define a list of colors for each year
colors = ["blue", "green", "red", "purple", "orange", "magenta", "cyan"]

# Create the plot
plt.figure(figsize=(12, 6))

# Loop through dataframes and plot each year's data with its color
for i, df in enumerate(dataframes):
  plt.plot(df.index, df.values, label=f"20{18+i}", color=colors[i])

# Set labels and title
plt.ylabel("WEEKLY AVG")
plt.xlabel("DATE")
plt.title("Weekly Average Overlapping Years")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
