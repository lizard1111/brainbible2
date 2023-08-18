import json
import pandas as pd

# Load the JSON files again
with open('RGB_TO_ACR.json', 'r') as file_rgb:
    rgb_to_acr_mapping = json.load(file_rgb)

with open('ACR_TO_PARENT.json', 'r') as file_parent:
    acr_to_parent_mapping = json.load(file_parent)

#Load the CSV
processedCSV = pd.read_csv('processed_data809.csv')

# Create DataFrames from the JSON mappings
rgb_to_acr_df = pd.DataFrame(list(rgb_to_acr_mapping.items()), columns=['RGB', 'acronym'])
acr_to_parent_df = pd.DataFrame(list(acr_to_parent_mapping.items()), columns=['acronym', 'parent_region'])

# Merge the processed data with the RGB-to-acronym mapping using the acronyms
merged_with_rgb = pd.merge(processedCSV, rgb_to_acr_df, on='acronym', how='left')

# Merge the resulting DataFrame with the acronym-to-parent mapping using the acronyms
final_merged_data = pd.merge(merged_with_rgb, acr_to_parent_df, on='acronym', how='left')

# Show the first few rows of the final merged data
final_merged_data.head()
print(final_merged_data)
final_merged_data.to_csv('merged_json.csv', index=False)