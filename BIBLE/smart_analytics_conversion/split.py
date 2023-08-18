import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('FemaleB_Restraint_Fos_output.csv')
df.head()
print(df.head)

left_df = df[df['name'].str.contains('left', case=False)]
right_df = df[df['name'].str.contains('right', case=False)]

right_df.head()

left_summary = left_df['density (cells/mm^3)'].describe()
right_summary = right_df['density (cells/mm^3)'].describe()

print("Left brain summary:")
print(left_summary)
print("\nRight brain summary:")
print(right_summary)


# Combine the data and add a column indicating the side of the brain
left_df['side'] = 'Left'
right_df['side'] = 'Right'

print(left_df.head)



# combined_df = pd.concat([left_df, right_df], axis=0)

# # Create new DataFrames to avoid modifying the original slices
# left_df = left_df.copy()
# right_df = right_df.copy()

# # Add the 'side' column
# left_df['side'] = 'Left'
# right_df['side'] = 'Right'

# # Combine the data
# combined_df = pd.concat([left_df, right_df], axis=0)

# combined_df.head()

# # Find the outlier(s) in the left DataFrame
# outliers = left_df[left_df['density (cells/mm^3)'] > left_summary['75%'] + 1.5 * (left_summary['75%'] - left_summary['25%'])]

# print("Outliers:")
# print(outliers)

# structures_of_interest = ['PVH', 'ARH']

# left_interest = left_df[left_df['acronym'].str.contains('|'.join(structures_of_interest), case=False)]
# right_interest = right_df[right_df['acronym'].str.contains('|'.join(structures_of_interest), case=False)]

# left_interest['side'] = 'Left'
# right_interest['side'] = 'Right'
# combined_interest = pd.concat([left_interest, right_interest], axis=0)

# plt.figure(figsize=(10, 5))
# sns.barplot(x='acronym', y='density (cells/mm^3)', hue='side', data=combined_interest)
# plt.title('Density comparison of left and right brain structures of interest')
# plt.show()