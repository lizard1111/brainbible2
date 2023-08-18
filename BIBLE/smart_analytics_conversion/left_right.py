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

# Split the DataFrame into two separate DataFrames for left and right sides
left_df = df[df['side'] == 'left']
right_df = df[df['side'] == 'right']

# Drop the 'side' column from both DataFrames
left_df.drop('side', axis=1, inplace=True)
right_df.drop('side', axis=1, inplace=True)

# Define the new filenames for the left and right CSV files
left_filename = 'df_left.csv'
right_filename = 'df_right.csv'

# Save the left and right DataFrames to new CSV files
left_df.to_csv(left_filename, index=False)
right_df.to_csv(right_filename, index=False)

print(f"Left CSV saved as: {left_filename}")
print(f"Right CSV saved as: {right_filename}")

# These following comments will give you instructions on how to modify this code.

# 1. First I want you to rename left_df 'count' to 'left_count' and right_df 'count' to 'right_count'

# 2. Then I want to to combine left_df and right_df as _combined_df

#3. Then I want to save this as "combined_CSV"

