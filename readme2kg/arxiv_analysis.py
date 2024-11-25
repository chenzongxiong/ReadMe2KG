import arxiv
import pandas as pd

README_PATH = './readme_samples/2975_readme_links.csv'
df = pd.read_csv(README_PATH, dtype={'paper_arxiv_id': 'string'})


# Replace 'arXivID' with the actual identifier of the paper
arxiv_id_list = df['paper_arxiv_id'].to_list()
arxiv_id_list = arxiv_id_list[:1]  # for debugging
search = arxiv.Search(id_list=arxiv_id_list)

for result in search.results():
    print(f"Title: {result.title}")
    print(f"Authors: {', '.join(author.name for author in result.authors)}")
    print(f"Abstract: {result.summary}")
    print(f"Published: {result.published}")
    print(f"PDF URL: {result.pdf_url}")
