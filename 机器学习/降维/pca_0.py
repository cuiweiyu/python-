from sklearn.decomposition import PCA
pca=PCA(n_components=1)
newData=pca.fit_transform(data)