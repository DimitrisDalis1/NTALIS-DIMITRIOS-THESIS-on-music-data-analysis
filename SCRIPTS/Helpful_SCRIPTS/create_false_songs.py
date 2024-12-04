import pandas as pd
import numpy as np

def generate_new_rows(row, num_rows=100):
    new_rows = []
    for _ in range(num_rows):
        new_row = row.copy()
        new_row['cent_std'] += np.random.uniform(-15, 15)
        new_row['rolloff_std'] += np.random.uniform(-15, 15)
        new_row['cent_mean'] += np.random.uniform(-15, 15)
        new_row['rolloff_mean'] += np.random.uniform(-25, 25)
        new_rows.append(new_row)
    return new_rows

# Load the original CSV file
df = pd.read_csv('results_features.csv')

# Create a list to store the new DataFrames
new_dfs = []

# Iterate over each row and generate new rows
for index, row in df.iterrows():
    new_rows = generate_new_rows(row)
    new_df = pd.DataFrame(new_rows)
    new_dfs.append(new_df)

# Concatenate all new DataFrames into a single DataFrame
expanded_df = pd.concat(new_dfs, ignore_index=True)

# Save the expanded DataFrame to a new CSV file
expanded_df.to_csv('false_data_songs.csv', index=False)