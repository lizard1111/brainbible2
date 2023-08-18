import pandas as pd

# Read the original CSV file
df = pd.read_csv('FemaleB_Restraint_Fos_output.csv')

# Split the 'name' column to extract the side information (left/right)
df[['side', 'name']] = df['name'].str.split(' ', n=1, expand=True)

# Strip any whitespace from the 'side' and 'name' columns
df['side'] = df['side'].str.strip()
df['name'] = df['name'].str.strip()

# Convert 'acronym' column to string type
df['acronym'] = df['acronym'].astype(str)

# Remove '-L' or '-R' suffix from the 'acronym' column
df['acronym'] = df['acronym'].str.replace('-L', '').str.replace('-R', '')

# Calculate the total volume by summing up the 'volume (mm^3)' values
df['total_volume'] = df['volume (mm^3)'].sum()

# Process the data further as needed
# For example, calculate average, maximum, minimum, or any other relevant metrics
# You can also filter, sort, or perform any other data manipulation operations

# Save the processed data to a new CSV file
processed_csv_filename = 'processed_data_doesTHISwork.csv'
df.to_csv(processed_csv_filename, index=False)
