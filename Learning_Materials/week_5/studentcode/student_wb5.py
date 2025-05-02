# DO NOT change anything except within the function
from approvedimports import *

def cluster_and_visualise(datafile_name:str, K:int, feature_names:list):
    """Function to get the data from a file, perform K-means clustering and produce a visualisation of results.

    Parameters
        ----------
        datafile_name: str
            path to data file

        K: int
            number of clusters to use

        feature_names: list
            list of feature names

        Returns
        ---------
        fig: matplotlib.figure.Figure
            the figure object for the plot

        axs: matplotlib.axes.Axes
            the axes object for the plot
    """
   # ====> insert your code below here

    user_name = "a9-bhandari"

    data = np.genfromtxt(datafile_name, delimiter = ",")

    model = KMeans(n_clusters = K)
    model.fit(data)
    labels = model.labels_

    n_features = len(feature_names)

    cmap = plt.get_cmap('viridis')
    norm = plt.Normalize(0, K - 1)

    if n_features == 1:
        # Single feature: histogram with cluster colors
        fig, ax = plt.subplots(1, 1, figsize=(6, 6))
        for k in range(K):
            ax.hist(data[labels == k, 0], color=cmap(norm(k)), alpha=0.5, bins=20)
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel('Frequency')
        axs = ax
    else:
        # Multiple features: scatter plot matrix
        fig, axs = plt.subplots(n_features, n_features, figsize=(12, 12))
        for i in range(n_features):
            for j in range(n_features):
                ax = axs[i, j]
                if i == j:
                    # Diagonal: histogram for each cluster
                    for k in range(K):
                        ax.hist(data[labels == k, i], color=cmap(norm(k)), 
                                alpha=0.5, bins=20)
                else:
                    # Off-diagonal: scatter plot with cluster colors
                    ax.scatter(data[:, j], data[:, i], c=labels, cmap=cmap, 
                              norm=norm, s=10)
                # Label axes: x on bottom row, y on left column
                if i == n_features - 1:
                    ax.set_xlabel(feature_names[j])
                if j == 0:
                    ax.set_ylabel(feature_names[i])

    file_name = f"Visualisation of {K} clusters by {user_name}"
    fig.suptitle(file_name)
    fig.savefig(f"myVisualisation.jpg.jpg")
    return fig, axs
    # <==== insert your code above here
