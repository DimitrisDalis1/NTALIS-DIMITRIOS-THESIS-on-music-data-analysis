import pandas as pd
features_df = pd.read_csv('results_features.csv')

from sklearn.decomposition import PCA
import plotly.express as px
from sklearn.tree import DecisionTreeClassifier

pca = PCA()

#Drop singers column
col = "singer"

df = features_df
df = df.loc[:, df.columns != col]
df.index = features.keys()
df.index
singer=[ind[0:4] for ind in df.index]
##singer=[ind for ind in df.index]
singer
##singer=['skordalos', 'psarantonis', 'psarantonis', 'psarantonis', 'skordalos', 'psarantonis', 'skordalos', 'skordalos']
singercol=[]
for s in singer:
    if s == 'hpeirwtika':
        singercol.append('red')
    elif s == 'psarantonis':
        singercol.append('blue')
    elif s == 'skordalos':
        singercol.append('green')
        
df_normalized=(df - df.mean()) / df.std()





components = pca.fit_transform(df_normalized)
labels = {
    str(i): f"PC {i+1} ({var:.1f}%)"
    for i, var in enumerate(pca.explained_variance_ratio_ * 100)
}

fig = px.scatter_matrix(
    components,
    labels=labels,
    dimensions=range(4),
    color=singer
)
fig.update_traces(diagonal_visible=False)
fig.show()


fig2 = px.scatter(components, x=0, y=1, color=singer, text=df.index)
fig2.show()