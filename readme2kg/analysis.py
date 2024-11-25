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
import hashlib
import json

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')


class Analyzer:
    def __init__(self, **kwargs):
        self._impl_notes = []
        self.documents = []
        self.vectorizer = None
        self.transformed_documents = None
        self.cfg = {}
        self.data = {}
        self.debug = kwargs.pop('debug', False)

    @property
    def impl_notes(self):
        return ','.join(self._impl_notes)

    def get_version(self, kwargs):
        serialized_string = json.dumps(kwargs, sort_keys=True)
        hash_object = hashlib.sha256()
        hash_object.update(serialized_string.encode('utf-8'))
        hashed = hash_object.hexdigest()
        return hashed[:8]

    def vectorize(self):
        if self.vectorizer:
            return self

        self.cfg['vectorize:max_features'] = None
        self.vectorizer = TfidfVectorizer(max_features=None, stop_words='english')
        self.transformed_documents = self.vectorizer.fit_transform(self.documents)
        return self

    def save(self, base_path='results'):
        self.cfg['impl_notes'] = self.impl_notes
        version = self.get_version(self.cfg)
        path = os.path.join(base_path, version)
        os.makedirs(path, exist_ok=True)

        with open(os.path.join(path, 'info.json'), 'w') as fd:
            json.dump(self.cfg, fd)

        with open(os.path.join(path, 'result.json'), 'w') as fd:
            json.dump(self.data, fd)

    def run_kmeans(self, num_clusters=5, top_n=10):
        self.cfg['kmeans:num_clusters'] = num_clusters
        self.cfg['kmeans:top_n'] = top_n
        self.cfg['kmeans'] = True

        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(self.transformed_documents)
        terms = self.vectorizer.get_feature_names_out()
        keywords = []
        for cluster_idx in range(num_clusters):
            center = kmeans.cluster_centers_[cluster_idx]
            indices = center.argsort()[-top_n:][::-1]
            # keywords.append([(terms[i], cluster_idx, center[i]) for i in indices])
            keywords.append([terms[i] for i in indices])
            print(f'Cluster {cluster_idx}: {keywords[-1]}')

        self.data['kmeans'] = keywords
        return self

    def run_pca(self, n_components, top_n):
        self.cfg['pca:n_components'] = n_components
        self.cfg['pca:top_n'] = top_n
        self.cfg['pca'] = True
        pca = PCA(n_components=n_components)
        pca_result = pca.fit_transform(self.transformed_documents.toarray())
        terms = self.vectorizer.get_feature_names_out()
        keywords = [terms[i] for i in pca.components_[0].argsort()[-top_n:]]
        print(f"Principal Keywords: {keywords}")
        self.data['pca'] = keywords
        return self

    def run_lda(self, n_components, top_n):
        self.cfg['lda:n_components'] = n_components
        self.cfg['lda:top_n'] = top_n
        self.cfg['lda'] = True
        lda = LatentDirichletAllocation(n_components=n_components, random_state=42)
        lda.fit(self.transformed_documents)
        terms = self.vectorizer.get_feature_names_out()
        keywords = []
        for idx, topic in enumerate(lda.components_):
            keywords.append([terms[i] for i in topic.argsort()[-top_n:]])
            print(f"Topic {idx}: {keywords[-1]}")
        self.data['lda'] = keywords
        return self

    def run_dbscan(self, min_cluster_size=3, top_n=10):
        self.cfg['dbscan:min_cluster_size'] = min_cluster_size
        self.cfg['dbscan:top_n'] = top_n
        self.cfg['dbscan'] = True

        hdb = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
        clusters = hdb.fit_predict(self.transformed_documents.toarray())
        terms = self.vectorizer.get_feature_names_out()
        keywords = []
        for cluster_label in set(clusters):
            if cluster_label == -1:  # Noise cluster
                continue
            cluster_indices = [i for i, x in enumerate(clusters) if x == cluster_label]
            keywords.append([terms[i] for i in cluster_indices][:top_n])
            print(f"Cluster {cluster_label}: {keywords[-1]}")

        self.data['dbscan'] = keywords
        return self

    # def plot(self, keywords):
    #     """Plot a bubble chart of keywords."""
    #     df = pd.DataFrame(keywords, columns=["Keyword", "Cluster", "Score"])
    #     df["x"] = df["Cluster"] + (pd.Series(range(len(df))) % 3)  # Spread x-coordinates
    #     df["y"] = df["Score"]
    #     plt.figure(figsize=(12, 8))
    #     scatter = plt.scatter(df["x"], df["y"], s=df["Score"] * 1000, alpha=0.6, c=df["Cluster"], cmap='viridis')
    #     for i, row in df.iterrows():
    #         plt.text(row["x"], row["y"], row["Keyword"], fontsize=10, ha='center')

    #     plt.title("Bubble Chart of Keywords in README Files", fontsize=16)
    #     plt.xlabel("Clusters", fontsize=12)
    #     plt.ylabel("TF-IDF Score", fontsize=12)
    #     plt.colorbar(scatter, label="Cluster")
    #     plt.show()


class ArxivAnalyzer(Analyzer):
    def __init__(self, file_path, **kwargs):
        super().__init__(**kwargs)
        self.documents = self.process_file(file_path)

    def process_file(self, file_path):
        df = pd.read_csv(file_path)
        documents = df['abstract'].tolist()
        if self.debug is True:
            documents = documents[:100]
        return documents


class ReadmeAnalyzer(Analyzer):
    def __init__(self, file_paths, **kwargs):
        super().__init__(**kwargs)
        self.documents = self.process_all_files(file_paths)

    def preprocess_readme(self, text):
        return text

    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_text = file.read()
        return self.preprocess_readme(raw_text)

    def process_all_files(self, file_paths):
        self._impl_notes.append('use raw text')
        documents = []
        for idx, file_path in enumerate(file_paths):
            if self.debug is True and idx >= 100:
                break
            document = self.process_file(file_path)
            documents.append(document)

        return documents

    # def preprocess_readme(text):
    #     stop_words = set(nltk.corpus.stopwords.words('english'))
    #     lemmatizer = WordNetLemmatizer()
    #     tokens = word_tokenize(text.lower())
    #     tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in string.punctuation]
    #     return tokens

    # def preprocess_readme(text):
    #     """Clean and preprocess README content."""
    #     # Remove Markdown or HTML tags
    #     text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove Markdown links
    #     text = BeautifulSoup(text, "html.parser").get_text()  # Parse HTML
    #     # Remove special characters and digits
    #     text = re.sub(r'[^a-zA-Z\s]', '', text)
    #     # Normalize whitespace
    #     text = re.sub(r'\s+', ' ', text).strip()
    #     return text



if __name__ == "__main__":
    debug = True
    print("############################## ReadMe ##############################")
    # Get all README file paths
    file_paths = [os.path.join('data/readmes', f) for f in os.listdir('data/readmes') if f.endswith(('.txt', '.md'))]

    print(f"Found {len(file_paths)} README files.")

    # Extract keywords
    analyzer = ReadmeAnalyzer(file_paths, debug=debug)

    n_components = 10
    min_cluster_size = n_components
    num_clusters = n_components

    top_n = 10
    # KMeans
    num_clusters = n_components
    analyzer.vectorize().run_kmeans(num_clusters, top_n).save()
    # PCA
    analyzer.vectorize().run_pca(n_components, top_n).save()
    # LDA
    analyzer.vectorize().run_lda(n_components, top_n).save()
    # DBScan
    analyzer.vectorize().run_dbscan(min_cluster_size, top_n).save()


    ################################################################################
    print("############################## ARXIV ##############################")
    # Get Arxiv
    file_path = './data/2975_arxiv_metadata.csv'

    # Extract keywords
    analyzer = ArxivAnalyzer(file_path, debug=debug)

    n_components = 10
    min_cluster_size = n_components
    num_clusters = n_components

    top_n = 10
    # KMeans
    num_clusters = n_components
    analyzer.vectorize().run_kmeans(num_clusters, top_n).save()
    # PCA
    analyzer.vectorize().run_pca(n_components, top_n).save()
    # LDA
    analyzer.vectorize().run_lda(n_components, top_n).save()
    # DBScan
    analyzer.vectorize().run_dbscan(min_cluster_size, top_n).save()
