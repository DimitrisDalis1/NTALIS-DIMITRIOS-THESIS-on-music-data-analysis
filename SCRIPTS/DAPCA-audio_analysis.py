import pandas as pd
from sklearn.decomposition import PCA
import statsmodels.api as sm
from statsmodels.multivariate.manova import MANOVA
import numpy as np
from DAPCA import DAPCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


def enumerate_strings(strings):
    """Enumerate a list of strings, assigning unique numbers to unique strings.

    Args:
        strings: A list of strings.

    Returns:
        A list of integers, where each integer corresponds to the unique identifier of the string.
    """

    unique_strings = set()
    string_to_number = {}
    enumerated_strings = []

    for string in strings:
        if string not in unique_strings:
            unique_strings.add(string)
            string_to_number[string] = len(unique_strings)
        enumerated_strings.append(string_to_number[string])

    return enumerated_strings

# Load your data
data = pd.read_csv('results_features.csv')

numerical_data = data.iloc[:, :-1]

artist_category = data.iloc[:, -1]


numerical_data = np.array(numerical_data)  # Assuming X is your data
artist_category = np.array(artist_category)  # Assuming artist_category is a list or array

#Change this number to alter the amount of features and PCAs are shown/compared
Pca_number = 3
# Perform DAPCA
V, D, PX, PY, kNNs = DAPCA(numerical_data, artist_category, nComp=Pca_number)
'''
# Calculate the cumulative explained variance ratio
cumulative_variance_ratio = np.cumsum(D) / np.sum(D)

# Choose a threshold (e.g., 95%)
threshold = 0.9

# Determine the number of components to keep
num_components_to_keep = np.argmax(cumulative_variance_ratio >= threshold) + 1
print(num_components_to_keep)
'''
# Select the top components
V_reduced = V[:, :Pca_number]
X_reduced = numerical_data[:, :Pca_number]

# ... (rest of your code)

# Get absolute loadings for selected components
abs_loadings = np.abs(V_reduced)

# Identify top features for each component (assuming 3 components)
top_features_per_component = []
for i in range(Pca_number):
    top_features_per_component.append(data.columns[:-1][abs_loadings[:, i].argsort()[-4:]])  # Get top 3 features

# Print interpretation for each component
for i in range(Pca_number):
    print(f"PC{i+1} - Top Features:", *top_features_per_component[i])

#print(PX)
'''
#Match the number of nComp the one below
X_reduced = PX[:, :6]
'''
# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Fit and transform the artist_category array
artist_category_encoded = label_encoder.fit_transform(artist_category)

# Create a scatter plot
# Assuming you have the X_reduced matrix with all principal components
num_components = X_reduced.shape[1]


for i in range(num_components):
    for j in range(i+1, num_components):
        plt.figure()  # Create a new figure for each plot
        plt.scatter(X_reduced[:, i], X_reduced[:, j], c=artist_category_encoded)
        plt.xlabel(f"PC{i+1}")
        plt.ylabel(f"PC{j+1}")
        plt.title(f"PC{i+1} vs PC{j+1}")
        plt.colorbar()
        plt.show()
