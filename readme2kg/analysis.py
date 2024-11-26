import os
import re
import nltk
import string
import hdbscan

import numpy as np
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
import argparse

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('wordnet')


class Analyzer:
    def __init__(self, **kwargs):
        self._impl_notes = set()
        self.documents = []
        self.vectorizer = None
        self.transformed_documents = None
        self.cfg = {}
        self.data = {}
        self.debug = kwargs.pop('debug', False)

    @property
    def impl_notes(self):
        return ','.join(sorted(self._impl_notes))

    def get_version(self, kwargs):
        serialized_string = json.dumps(kwargs, sort_keys=True)
        hash_object = hashlib.sha256()
        hash_object.update(serialized_string.encode('utf-8'))
        hashed = hash_object.hexdigest()
        return hashed[:8]

    def vectorize(self):
        if self.vectorizer:
            return self

        max_features = 1000
        self.cfg['vectorize:max_features'] = max_features
        self.vectorizer = TfidfVectorizer(max_features=max_features, stop_words='english')
        self.transformed_documents = self.vectorizer.fit_transform(self.documents)
        return self

    def save(self, base_path='results'):
        self.cfg['impl_notes'] = self.impl_notes
        # version = self.get_version(self.cfg)
        if self.cfg.get('kmeans', False):
            num_clusters = self.cfg['kmeans:num_clusters']
            top_n = self.cfg['kmeans:top_n']
            version = f'kmeans-cluster_{num_clusters}-topn_{top_n}'
        elif self.cfg.get('pca', False):
            n_components = self.cfg['pca:n_components']
            top_n = self.cfg['pca:top_n']
            version = f'pca-components_{n_components}-topn_{top_n}'
        elif self.cfg.get('lda', False):
            n_components = self.cfg['lda:n_components']
            top_n = self.cfg['lda:top_n']
            version = f'lda-components_{n_components}-topn_{top_n}'
        elif self.cfg.get('dbscan', False):
            min_cluster_size = self.cfg['dbscan:min_cluster_size']
            top_n = self.cfg['dbscan:top_n']
            version = f'dbscan-clusetr_{min_cluster_size}-topn_{top_n}'

        path = os.path.join(base_path, version)
        os.makedirs(path, exist_ok=True)

        with open(os.path.join(path, 'info.json'), 'w') as fd:
            json.dump(self.cfg, fd)

        np.save(os.path.join(path, 'result.npy'), self.data, allow_pickle=True)

    def run_kmeans(self, num_clusters=8, top_n=100):
        num_clusters = 8 if num_clusters is None else num_clusters

        self.cfg['kmeans:num_clusters'] = num_clusters
        self.cfg['kmeans:top_n'] = top_n
        self.cfg['kmeans'] = True

        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(self.transformed_documents)
        terms = self.vectorizer.get_feature_names_out()
        keywords = []
        keywords_with_centroid = []
        for cluster_idx in range(num_clusters):
            center = kmeans.cluster_centers_[cluster_idx]
            indices = center.argsort()[-top_n:][::-1]
            # keywords.append([(terms[i], cluster_idx, center[i]) for i in indices])
            keywords.append([terms[i] for i in indices])
            keywords_with_centroid.append([(terms[i], cluster_idx, center[i]) for i in indices])
            print(f'Cluster {cluster_idx}: {keywords[-1]}')

        self.data['kmeans'] = keywords
        self.data['kmeans_with_centroid'] = keywords_with_centroid
        return self

    def run_pca(self, n_components=2, top_n=100):
        n_components = 2
        top_n = 100

        self.cfg['pca:n_components'] = n_components
        self.cfg['pca:top_n'] = top_n
        self.cfg['pca'] = True

        # tfidf_scores = self.transformed_documents.toarray().flatten()
        tfidf_scores = self.transformed_documents.toarray().sum(axis=0)

        terms = self.vectorizer.get_feature_names_out()
        top_indices = tfidf_scores.argsort()[-top_n:][::-1]
        keywords = [(terms[i], tfidf_scores[i]) for i in top_indices]
        pca = PCA(n_components=n_components)
        X_pca = pca.fit_transform(self.transformed_documents.toarray())

        import ipdb; ipdb.set_trace()
        explained_variance = pca.explained_variance_ratio_
        cumulative_variance = explained_variance.cumsum()

        # Use the cumulative explained variance ratio to decide how many components to retain. Typically, choose enough components to capture 90%-95% of the variance.
        # num_components = (cumulative_variance >= 0.95).argmax() + 1
        keywords2 = []
        for component_idx in range(n_components):
            keywords2.append([terms[i] for i in pca.components_[component_idx].argsort()[-top_n:][::-1]])


        print(f"Principal Keywords: {keywords}")
        print(f"Principal Keywords 2: {keywords2}")

        self.data['keywords'] = keywords
        self.data['keywords2'] = keywords2
        self.data['X_pca'] = X_pca
        self.data['terms'] = terms
        # import matplotlib.pyplot as plt
        # plt.figure(figsize=(8, 5))
        # plt.plot(range(1, len(cumulative_variance)+1), cumulative_variance, marker='o', linestyle='--')
        # plt.title('Cumulative Explained Variance by PCA Components')
        # plt.xlabel('Number of Components')
        # plt.ylabel('Cumulative Explained Variance')
        # plt.axhline(y=0.95, color='r', linestyle='--')
        # plt.grid(True)
        # plt.show()
        return self

    # def run_lda(self, n_components, top_n=100):
    #     self.cfg['lda:n_components'] = n_components
    #     self.cfg['lda:top_n'] = top_n
    #     self.cfg['lda'] = True
    #     lda = LatentDirichletAllocation(n_components=n_components, random_state=42)
    #     lda.fit(self.transformed_documents)
    #     terms = self.vectorizer.get_feature_names_out()
    #     keywords = []
    #     for idx, topic in enumerate(lda.components_):
    #         keywords.append([terms[i] for i in topic.argsort()[-top_n:]])
    #         print(f"Topic {idx}: {keywords[-1]}")
    #     self.data['lda'] = keywords
    #     return self

    # def run_dbscan(self, min_cluster_size=3, top_n=100):
    #     # FIXME: Not test yet
    #     self.cfg['dbscan:min_cluster_size'] = min_cluster_size
    #     self.cfg['dbscan:top_n'] = top_n
    #     self.cfg['dbscan'] = True

    #     hdb = hdbscan.HDBSCAN(min_cluster_size=min_cluster_size)
    #     clusters = hdb.fit_predict(self.transformed_documents.toarray())
    #     terms = self.vectorizer.get_feature_names_out()
    #     keywords = []
    #     for cluster_label in set(clusters):
    #         if cluster_label == -1:  # Noise cluster
    #             continue
    #         cluster_indices = [i for i, x in enumerate(clusters) if x == cluster_label]
    #         keywords.append([terms[i] for i in cluster_indices][:top_n])
    #         print(f"Cluster {cluster_label}: {keywords[-1]}")

    #     self.data['dbscan'] = keywords
    #     return self

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
        if self.debug is True:
            df = pd.read_csv(file_path, nrows=100)
        else:
            df = pd.read_csv(file_path)

        documents = df['abstract'].tolist()
        cleaned_documents = []

        for idx, document in enumerate(documents):
            document = self.preprocess_text(document)
            cleaned_documents.append(document)

        return documents

    def preprocess_text(self, text):
        stop_words = set(nltk.corpus.stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        tokens = word_tokenize(text.lower())
        tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words and word not in string.punctuation]
        return tokens


class ReadmeAnalyzer(Analyzer):
    def __init__(self, file_paths, **kwargs):
        super().__init__(**kwargs)
        self.documents = self.process_all_files(file_paths)

    def preprocess_readme_v1(self, text):
        self._impl_notes.append('use raw text')
        return text

    def preprocess_readme_v2(self, text):
        """Clean and preprocess README content."""
        self._impl_notes.add('clean markdown and html tags')
        # Remove Markdown or HTML tags
        text = re.sub(r'\[.*?\]\(.*?\)', '', text)  # Remove Markdown links
        text = BeautifulSoup(text, "html.parser").get_text()  # Parse HTML
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def process_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_text = file.read()
        return self.preprocess_readme_v2(raw_text)

    def process_all_files(self, file_paths):
        if self.debug is True:
            file_paths = file_paths[:100]

        documents = []
        for idx, file_path in enumerate(file_paths):
            document = self.process_file(file_path)
            documents.append(document)

        return documents


def analyze_readme(args):
    print("############################## ReadMe ##############################")
    # Get all README file paths
    file_paths = [os.path.join('data/readmes', f) for f in os.listdir('data/readmes') if f.endswith(('.txt', '.md'))]

    print(f"Found {len(file_paths)} README files.")

    analyzer = ReadmeAnalyzer(file_paths, debug=args.debug)

    top_n = args.top_n
    n_components = args.n_components

    min_cluster_size = n_components
    num_clusters = n_components

    # KMeans
    num_clusters = n_components
    # analyzer.vectorize().run_kmeans(num_clusters, top_n).save()
    # # PCA
    analyzer.vectorize().run_pca(n_components, top_n).save()
    # # LDA
    # analyzer.vectorize().run_lda(n_components, top_n).save()
    # # DBScan
    # analyzer.vectorize().run_dbscan(min_cluster_size, top_n).save()

    # method_list = ['run_kmeans', 'run_pca', 'run_lda', 'run_dbscan']
    # method_list = ['run_pca']
    # tasks = Parallel(n_jobs=-1)(delayed(getattr(analyzer.vectorize(), method))(n_components, top_n) for method in method_list)
    # for task in tasks:
    #     task.save('results/readme')


def analyze_arxiv(args):
    print("############################## ARXIV ##############################")
    # Get Arxiv
    file_path = './data/2975_arxiv_metadata.csv'

    analyzer = ArxivAnalyzer(file_path, debug=args.debug)

    n_components = args.n_components
    min_cluster_size = n_components
    num_clusters = n_components

    top_n = args.top_n
    # KMeans
    num_clusters = n_components
    # analyzer.vectorize().run_kmeans(num_clusters, top_n).save()
    # # PCA
    # analyzer.vectorize().run_pca(n_components, top_n).save()
    # # LDA
    # analyzer.vectorize().run_lda(n_components, top_n).save()
    # # DBScan
    # analyzer.vectorize().run_dbscan(min_cluster_size, top_n).save()
    # method_list = ['run_kmeans', 'run_pca', 'run_lda', 'run_dbscan']
    method_list = ['run_pca', 'run_kmeans']
    tasks = Parallel(n_jobs=-1)(delayed(getattr(analyzer.vectorize(), method))(n_components, top_n) for method in method_list)
    for task in tasks:
        task.save('results/arxiv')


def get_parse():
    parser = argparse.ArgumentParser(description="Analyzer")

    parser.add_argument('--n_components', type=int, default=None)
    parser.add_argument('--top_n', type=int, default=100)
    parser.add_argument('--readme', action='store_true')
    parser.add_argument('--arxiv', action='store_true')
    parser.add_argument('--debug', action='store_true')

    return parser


def main(args):
    ################################################################################
    if args.readme:
        analyze_readme(args)
    if args.arxiv:
        analyze_arxiv(args)


if __name__ == "__main__":
    parser = get_parse()
    args = parser.parse_args()
    main(args)
