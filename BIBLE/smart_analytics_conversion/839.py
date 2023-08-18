import pandas as pd

# Read the original CSV file
df = pd.read_csv('FemaleB_Restraint_Fos_output.csv')

# Separate left and right regions
left_data = df[df['name'].str.contains('left ')].copy()
right_data = df[df['name'].str.contains('right ')].copy()

# Remove 'left ' and 'right ' from the names
left_data['name'] = left_data['name'].str.replace('left ', '')
right_data['name'] = right_data['name'].str.replace('right ', '')

# Merge left and right data on the 'name' column
merged_data = pd.merge(left_data, right_data, on='name', suffixes=('_left', '_right'))

# Calculate sum total for count, volume, and density
merged_data['count_total'] = merged_data['count_left'] + merged_data['count_right']
merged_data['volume_total (mm^3)'] = merged_data['volume (mm^3)_left'] + merged_data['volume (mm^3)_right']
merged_data['density_total (cells/mm^3)'] = (merged_data['density (cells/mm^3)_left'] + merged_data['density (cells/mm^3)_right']) / 2

# Select the necessary columns
final_data = merged_data[['acronym', 'count_left', 'count_right', 'count_total', 'volume (mm^3)_left', 'volume (mm^3)_right', 'volume_total (mm^3)', 'density (cells/mm^3)_left', 'density (cells/mm^3)_right', 'density_total (cells/mm^3)']]

# You can save the final_data to a new CSV file if needed
final_data.to_csv('processed_data839.csv', index=False)
