import os
import re
import nltk
import string
import hdbscan

from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA, LatentDirichletAllocation
import pandas as pd
from joblib import Parallel, delayed

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')

# def preprocess_readme(text):
#     return text

# def preprocess_readme(text):
#     stop_words = set(nltk.corpus.stopwords.words('english'))
#     lemmatizer = WordNetLemmatizer()
#     tokens = word_tokenize(text.lower())
#     tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in string.punctuation]
#     import ipdb; ipdb.set_trace()
#     return tokens

# Step 1: Preprocessing Function
def preprocess_readme(text):
    """Clean and preprocess README content."""
    # Remove Markdown or HTML tags
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove Markdown links
    text = BeautifulSoup(text, "html.parser").get_text()  # Parse HTML

    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

# Step 2: Process a Single File
def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        raw_text = file.read()
        return preprocess_readme(raw_text)

# Step 3: Process All Files in Parallel
def process_all_files(file_paths):
    return Parallel(n_jobs=-1)(delayed(process_file)(file) for file in file_paths)

# Step 4: Extract Keywords Using KMeans
def kmeans(documents, num_clusters=5, top_n=10):
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(documents)

    # Apply KMeans
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(X)

    # Extract keywords for each cluster
    keywords = []
    terms = vectorizer.get_feature_names_out()
    for i in range(num_clusters):
        cluster_center = kmeans.cluster_centers_[i]
        top_indices = cluster_center.argsort()[-top_n:][::-1]
        keywords.append([terms[idx] for idx in top_indices])

    return keywords

def pca(documents, n_components=5):
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(documents)

    pca = PCA(n_components=n_components)
    pca_result = pca.fit_transform(X.toarray())
    keywords = vectorizer.get_feature_names_out()
    top_keywords = [keywords[i] for i in pca.components_[0].argsort()[-10:]]
    print(f"Principal Keywords: {top_keywords}")

def dbscan(documents, min_cluster_size=5):
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(documents)

    hdb = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
    clusters = hdb.fit_predict(X.toarray())

    keywords = vectorizer.get_feature_names_out()
    for cluster_label in set(clusters):
        if cluster_label == -1:  # Noise cluster
            continue
        cluster_indices = [i for i, x in enumerate(clusters) if x == cluster_label]
        cluster_keywords = [keywords[i] for i in cluster_indices]
        print(f"Cluster {cluster_label}: {cluster_keywords[:10]}")


def lda(documents, n_components=5):
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X = vectorizer.fit_transform(documents)

    _lda = LatentDirichletAllocation(n_components=5, random_state=42)
    _lda.fit(X)

    for idx, topic in enumerate(_lda.components_):
        print(f"Topic {idx}:")
        print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])


# Step 5: Main Execution
if __name__ == "__main__":
    # Directory containing README files
    readme_dir = "data/readmes/"

    # Get all README file paths
    file_paths = [
        os.path.join(readme_dir, f)
        for f in os.listdir(readme_dir)
        if f.endswith(('.txt', '.md'))
    ][:100]

    print(f"Found {len(file_paths)} README files.")

    # # Process README files
    # document = process_file(file_paths[0])
    documents = process_all_files(file_paths)

    # Extract keywords
    num_clusters = 5
    top_n = 10
    keywords = kmeans(documents, num_clusters=num_clusters, top_n=top_n)

    # Save results to CSV
    keywords_df = pd.DataFrame(
        {f"Cluster {i+1}": keywords[i] for i in range(num_clusters)}
    )
    keywords_df.to_csv("keywords_clusters.csv", index=False)
    print("Keywords extracted and saved to keywords_clusters.csv.")
    pca(documents)
    dbscan(documents)
    lda(documents)
