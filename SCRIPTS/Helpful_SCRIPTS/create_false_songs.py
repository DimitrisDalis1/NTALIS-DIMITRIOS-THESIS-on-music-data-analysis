import pandas as pd
import numpy as np

def generate_new_rows(row, num_rows=25):
    new_rows = []
    for _ in range(num_rows):
        new_row = row.copy()
        new_row['chroma_mean_0'] += np.random.uniform(-1, 1)
        new_row['chroma_mean_1'] += np.random.uniform(-1, 1)
        new_row['chroma_mean_2'] += np.random.uniform(-1, 1)
        new_row['chroma_mean_3'] += np.random.uniform(-1, 1)
        new_row['chroma_mean_4'] += np.random.uniform(-1, 1)
        new_row['chroma_mean_5'] += np.random.uniform(-1, 1)
        new_row['chroma_mean_6'] += np.random.uniform(-1,1)
        new_row['chroma_mean_7'] += np.random.uniform(-1,1)
        new_row['chroma_mean_8'] += np.random.uniform(-1,1)
        new_row['chroma_mean_9'] += np.random.uniform(-1,1)
        new_row['chroma_mean_10'] += np.random.uniform(-1,1)
        new_row['chroma_mean_11'] += np.random.uniform(-1,1)
        new_row['chroma_std_0'] += np.random.uniform(-1,1)
        new_row['chroma_std_1'] += np.random.uniform(-1,1)
        new_row['chroma_std_2'] += np.random.uniform(-1,1)
        new_row['chroma_std_3'] += np.random.uniform(-1,1)
        new_row['chroma_std_4'] += np.random.uniform(-1,1)
        new_row['chroma_std_5'] += np.random.uniform(-1,1)
        new_row['chroma_std_6'] += np.random.uniform(-1,1)
        new_row['chroma_std_7'] += np.random.uniform(-1,1)
        new_row['chroma_std_8'] += np.random.uniform(-1,1)
        new_row['chroma_std_9'] += np.random.uniform(-1,1)
        new_row['chroma_std_10'] += np.random.uniform(-1,1)
        new_row['chroma_std_11'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_0'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_1'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_2'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_3'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_4'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_5'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_6'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_7'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_8'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_9'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_10'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_11'] += np.random.uniform(-1,1)
        new_row['mfccs_mean_12'] += np.random.uniform(-1,1)
        new_row['mfccs_std_0'] += np.random.uniform(-1,1)
        new_row['mfccs_std_1'] += np.random.uniform(-1,1)
        new_row['mfccs_std_2'] += np.random.uniform(-1,1)
        new_row['mfccs_std_3'] += np.random.uniform(-1,1)
        new_row['mfccs_std_4'] += np.random.uniform(-1,1)
        new_row['mfccs_std_5'] += np.random.uniform(-1,1)
        new_row['mfccs_std_6'] += np.random.uniform(-1,1)
        new_row['mfccs_std_7'] += np.random.uniform(-1,1)
        new_row['mfccs_std_8'] += np.random.uniform(-1,1)
        new_row['mfccs_std_9'] += np.random.uniform(-1,1)
        new_row['mfccs_std_10'] += np.random.uniform(-1,1)
        new_row['mfccs_std_11'] += np.random.uniform(-1,1)
        new_row['mfccs_std_12'] += np.random.uniform(-1,1)
        new_row['cent_mean'] += np.random.uniform(-1,1)
        new_row['cent_std'] += np.random.uniform(-1,1)
        new_row['cent_skew'] += np.random.uniform(-1,1)
        new_row['contrast_mean_0'] += np.random.uniform(-1,1)
        new_row['contrast_mean_1'] += np.random.uniform(-1,1)
        new_row['contrast_mean_2'] += np.random.uniform(-1,1)
        new_row['contrast_mean_3'] += np.random.uniform(-1,1)
        new_row['contrast_mean_4'] += np.random.uniform(-1,1)
        new_row['contrast_mean_5'] += np.random.uniform(-1,1)
        new_row['contrast_mean_6'] += np.random.uniform(-1,1)
        new_row['contrast_std_0'] += np.random.uniform(-1,1)
        new_row['contrast_std_1'] += np.random.uniform(-1,1)
        new_row['contrast_std_2'] += np.random.uniform(-1,1)
        new_row['contrast_std_3'] += np.random.uniform(-1,1)
        new_row['contrast_std_4'] += np.random.uniform(-1,1)
        new_row['contrast_std_5'] += np.random.uniform(-1,1)
        new_row['contrast_std_6'] += np.random.uniform(-1,1)
        new_row['rolloff_mean'] += np.random.uniform(-1,1)
        new_row['rolloff_std'] += np.random.uniform(-1,1)
        new_row['rolloff_skew'] += np.random.uniform(-1,1)
        new_row['zrate_mean'] += np.random.uniform(-1,1)
        new_row['zrate_std'] += np.random.uniform(-1,1)
        new_row['zrate_skew'] += np.random.uniform(-1,1)
        new_row['tempo'] += np.random.uniform(-1,1)




        new_rows.append(new_row)
    return new_rows

# Load the original CSV file
df = pd.read_csv('normalized_results.csv')

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