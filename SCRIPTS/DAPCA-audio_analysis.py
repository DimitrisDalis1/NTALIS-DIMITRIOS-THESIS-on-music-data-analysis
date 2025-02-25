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

data = pd.read_csv('extracted_data.csv')

# Separate numerical data: from the beginning to the 4th column before the end
numerical_data = data.iloc[:, :-4]

# Separate artist category: the 3rd column from the end
artist_category = data.iloc[:, -3]


numerical_data = np.array(numerical_data)  
artist_category = np.array(artist_category) 

#Change this number to alter the amount of features and PCAs are shown/compared
Pca_number = 4

# Perform DAPCA
V, D, PX, PY, kNNs = DAPCA(numerical_data, artist_category, nComp=Pca_number)

V_reduced = V[:, :Pca_number]
X_reduced = numerical_data[:, :Pca_number]


# Get absolute loadings for selected components
abs_loadings = np.abs(V_reduced)

# Identify top features for each component
top_features_per_component = []
for i in range(Pca_number):
    top_features_per_component.append(data.columns[:-1][abs_loadings[:, i].argsort()[-4:]])  # Get top 4 features

# Print interpretation for each component
for i in range(Pca_number):
    print(f"PC{i+1} - Top Features:", *top_features_per_component[i])


# Create a LabelEncoder object
label_encoder = LabelEncoder()

# Fit and transform the artist_category array
artist_category_encoded = label_encoder.fit_transform(artist_category)

# Create a scatter plot
num_components = X_reduced.shape[1]


for i in range(num_components):
    for j in range(i + 1, num_components):
        plt.figure(figsize=(10, 8))  # Increase figure size
        scatter = plt.scatter(X_reduced[:, i], X_reduced[:, j], c=artist_category_encoded, cmap='rainbow') 

        # Create a legend
        unique_artists = label_encoder.classes_
        handles = [plt.Line2D([], [], marker='o', color=scatter.cmap(scatter.norm(label_encoder.transform([artist]))[0])) 
                   for artist in unique_artists]
        plt.legend(handles, unique_artists, title="Artists", loc='upper left', bbox_to_anchor=(0.75, 1)) 

        plt.xlabel(f"PC{i+1}")
        plt.ylabel(f"PC{j+1}")
        plt.title(f"PC{i+1} vs PC{j+1}")
        # Remove the colorbar
        plt.colorbar().remove() 
        plt.show()

