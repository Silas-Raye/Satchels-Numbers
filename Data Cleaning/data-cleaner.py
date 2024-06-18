import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('2024-raw.csv')

# Convert the 'DATE' column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'], format='%m/%d/%Y', errors='coerce')

# Drop rows where 'DATE' column is NaT (which indicates missing or invalid dates)
df = df.dropna(subset=['DATE'])

# Select only the required columns
columns_to_keep = ['DATE', 'DAY', 'NIGHT', 'SATCH Z', 'LSE TOT', 'TOTAL']
df = df[columns_to_keep]

# Rename the columns
df = df.rename(columns={
    'DAY': 'SATCH-DAY',
    'NIGHT': 'SATCH-NIGHT',
    'SATCH Z': 'SATCH-TOT',
    'LSE TOT': 'LSE-TOT'
})

# Function to replace non-numeric values with NaN
def remove_non_numeric(df):
    for col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

# Replace non-numeric values with NaN
df = remove_non_numeric(df)

# Convert the 'DATE' column back to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Add new columns
df['LSE-PERCENT'] = df['LSE-TOT'] / df['TOTAL']
df['LSE-DAY'] = pd.NA
df['LSE-NIGHT'] = pd.NA

# Save the cleaned DataFrame back to a CSV file if needed
df.to_csv('2024-clean.csv', index=False)
