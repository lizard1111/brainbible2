import pandas as pd

# Read the CSV file
csv_file_path = 'merged_JSON.csv'
data = pd.read_csv(csv_file_path)

# Convert to HTML
html_table = data.to_html(index=False)

# Save to HTML file
with open('output.html', 'w') as file:
    file.write(html_table)
