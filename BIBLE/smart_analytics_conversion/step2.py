import pandas as pd

# Read the original CSV file
df = pd.read_csv('FemaleB_Restraint_Fos_output.csv')

# Print unique values in the 'volume (mm^3)' column
unique_values = df['volume (mm^3)'].unique()
for value in unique_values:
    print(value)

# Rest of your code...

# Split the 'name' column to extract the side information (left/right)
df[['side', 'name']] = df['name'].str.split(' ', n=1, expand=True)

# Strip any whitespace from the 'side' and 'name' columns
df['side'] = df['side'].str.strip()
df['name'] = df['name'].str.strip()

# Convert 'acronym' column to string type
df['acronym'] = df['acronym'].astype(str)

# Remove '-L' or '-R' suffix from the 'acronym' column
df['acronym'] = df['acronym'].str.replace('-L', '').str.replace('-R', '')

# Drop the 'parent_structure_ID' column
if 'parent_structure_id' in df.columns:
    df.drop('parent_structure_id', axis=1, inplace=True)

# Split the DataFrame into two separate DataFrames for left and right sides
left_df = df[df['side'] == 'left'].copy()  # Using .copy() to avoid SettingWithCopyWarning
right_df = df[df['side'] == 'right'].copy()  # Using .copy() to avoid SettingWithCopyWarning

# Drop the 'side' column from both DataFrames
left_df.drop(['side'], axis=1, inplace=True)
right_df.drop(['side'], axis=1, inplace=True)

# Rename the 'count' columns in left_df and right_df
left_df.rename(columns={'count': 'left_count'}, inplace=True)
right_df.rename(columns={'count': 'right_count'}, inplace=True)

# Convert 'volume (mm^3)' column to strings before splitting
left_df['volume (mm^3)'] = left_df['volume (mm^3)'].astype(str)
right_df['volume (mm^3)'] = right_df['volume (mm^3)'].astype(str)

# Split 'volume' and 'density' columns into left and right sides
left_df[['left_volume', 'right_volume']] = left_df['volume (mm^3)'].str.split('/', expand=True)
right_df[['left_volume', 'right_volume']] = right_df['volume (mm^3)'].str.split('/', expand=True)

# Drop the original 'volume (mm^3)' column
left_df.drop('volume (mm^3)', axis=1, inplace=True)
right_df.drop('volume (mm^3)', axis=1, inplace=True)

# Combine left_df and right_df into _combined_df
_combined_df = pd.concat([left_df, right_df], ignore_index=True)

# Define the filename for the combined CSV file
combined_filename = 'combined_CSV.csv'

# Save the combined DataFrame to a new CSV file
_combined_df.to_csv(combined_filename, index=False)

print(f"Combined CSV saved as: {combined_filename}")
