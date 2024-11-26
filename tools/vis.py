import os
import json
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_kmeans(keywords, path):
    """Plot a bubble chart of keywords."""
    df = pd.DataFrame(keywords, columns=["Keyword", "Cluster", "Score"])
    df["x"] = df["Cluster"] + (pd.Series(range(len(df))) % 3)  # Spread x-coordinates
    df["y"] = df["Score"]

    plt.figure(figsize=(16, 12))
    scatter = plt.scatter(df["x"], df["y"], s=df["Score"] * 1000, alpha=0.6, c=df["Cluster"], cmap='viridis')
    for i, row in df.iterrows():
        plt.text(row["x"], row["y"], row["Keyword"], fontsize=8, ha='center')

    plt.title("Bubble Chart of Keywords in README Files", fontsize=16)
    plt.xlabel("Clusters", fontsize=12)
    plt.ylabel("TF-IDF Score", fontsize=12)
    plt.yscale('log')
    plt.colorbar(scatter, label="Cluster")
    # plt.show()
    plt.savefig(f"{path}.png", bbox_inches='tight')


# Step 3: Bubble Chart Visualization
def plot_pca(keywords, X_pca, terms, path):
    """Plot a bubble chart of keywords using PCA-reduced dimensions."""
    top_keywords = [kw[0] for kw in keywords]
    top_scores = [kw[1] for kw in keywords]
    # Filter PCA components for top keywords
    indices = [list(terms).index(kw) for kw in top_keywords]

    pca_x = X_pca[0, indices]
    pca_y = X_pca[0, indices]

    # Plot
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(pca_x, pca_y, s=[score * 1000 for score in top_scores], alpha=0.6, c=pca_x + pca_y, cmap="viridis")
    for i, kw in enumerate(top_keywords):
        plt.text(pca_x[i], pca_y[i], kw, fontsize=8, ha='center')

    plt.title("PCA Bubble Chart of Keywords", fontsize=16)
    plt.xlabel("PCA Component 1", fontsize=12)
    plt.ylabel("PCA Component 2", fontsize=12)
    plt.colorbar(scatter, label="PCA Combination")
    plt.yscale('log')
    # plt.show()
    plt.savefig(f"{path}.png", bbox_inches='tight')


if __name__ == "__main__":
    source_list = ['readme', 'arxiv']
    for source in source_list:
        path = f'results/{source}/kmeans-cluster_8-topn_100/result.npy'
        data = np.load(path, allow_pickle=True)
        content = data.item()
        keywords = content['kmeans_with_centroid']
        keywords_ = []
        for keyword_list in keywords:
            keywords_ += keyword_list[:20]

        plot_kmeans(keywords_, path)

    for source in source_list:
        path = f'results/{source}/pca-components_2-topn_100/result.npy'
        data = np.load(path, allow_pickle=True)
        content = data.item()
        keywords = content['keywords'][:50]
        X_pca = content['X_pca'].T
        terms = content['terms']
        plot_pca(keywords, X_pca, terms, path)
