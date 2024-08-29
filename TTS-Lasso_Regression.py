##############################################
#So..
#For this example we have 13 hpeirwtika(RED songs)
#We also have 8 psarantonis (BLUE songs)
#5 of our songs are for testing 
#Song 10 is rated as psarantonis but is in fact hpeirwtiko
#The way to read the diagram as is:
#First 13 songs are hpeirwtika, which means 0-12 are hpeirwtika
#The rest are psarantonis
#Song 10 belongs to hpeirwtika
#But is rated as psarantonis because it is located on the blue area
##############################################

from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier 
import numpy as np 
import pandas as pd 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn import datasets, neighbors
from mlxtend.plotting import plot_decision_regions
from sklearn.metrics import accuracy_score, classification_report

#Define a specific random state
random_state = 11

#Read our csv
df = pd.read_csv("results_features.csv")

#X and y
X = df.drop("singer", axis=1)
y = df["singer"]

#Apply PCA to my data
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)




'''
#Checking how many n_components are necessary
explained_variance_ratio = pca.explained_variance_ratio_

plt.plot(np.cumsum(explained_variance_ratio))
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')
plt.title('Explained variance plot')
plt.show()
'''

#Trick to get the names of where each song belongs to
X_keep_track_of_the_songs = list(range(len(df)))

X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=random_state)

################
#What I am trying to do below is match my data with which song they were in the beginning before fitting
for i in range(X_test.shape[0]):
    for j in range(len(X_keep_track_of_the_songs)):
        if(X_test[i][0] == X_pca[j][0] and X_test[i][1] == X_pca[j][1]):
            X_keep_track_of_the_songs[i] = j

for i in range(X_test.shape[0], X_train.shape[0] + X_test.shape[0],1):
    X_keep_track_of_the_songs[i] = 0

#################

#Building the KNN model

#Create KNN model:
knn = KNeighborsClassifier(n_neighbors=2) #Based on the amount of singers we could potentially change that number

#Train the model
knn.fit(X_train, y_train)

#Make predictions on the test set:
y_pred = knn.predict(X_test)

#Evaluating the models performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

report = classification_report(y_test, y_pred)
print("Classification report:\n", report)

from sklearn.metrics import confusion_matrix
import seaborn as sns

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Create a heatmap   

sns.heatmap(cm, annot=True, cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()


# Get the nearest neighbors for each training point

# Assign songs to groups based on nearest neighbors
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
song_groups1 = kmeans.fit_predict(X_train)
song_groups2 = kmeans.fit_predict(X_test)
# Create a colormap to distinguish between groups
cmap = 'RdYlBu'

# Scatter plot with colors based on groups
plt.scatter(X_train[:, 0], X_train[:, 1], c=song_groups1, cmap=cmap, alpha=0.7)
plt.scatter(X_test[:, 0], X_test[:, 1], c=song_groups2, cmap=cmap, alpha=0.3)


for i in range(len(X_test)):
    row_index = df.index[i]  # Get the row index
    column_name = df.columns[-1]  # Assuming you want the first column's name
    plt.text(X_test[i, 0], X_test[i, 1], f"Song {X_keep_track_of_the_songs[i]} ", fontsize=8)
    print("ahahahahah", X_test[i, 0])


# Add labels and title
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('KNN Classification: Neighbor Groups')

# Add colorbar to show group assignments
plt.colorbar(cmap=cmap, label='Group')

plt.show()


#Reds are hpeirwtika
#Psarantonis ta alla
