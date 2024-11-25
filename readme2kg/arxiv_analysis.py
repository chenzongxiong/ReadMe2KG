import time
import arxiv
import pandas as pd

README_PATH = 'data/2975_readme_links.csv'
def get_metadata_list(arxiv_id_list):
    search = arxiv.Search(id_list=arxiv_id_list)
    metadata_list = []

    for paper_id, result in zip(arxiv_id_list, search.results()):
        assert paper_id in result.entry_id, ''  # Ensure
        metadata = {}
        metadata['paper_id'] = paper_id
        metadata['title'] = result.title
        metadata['authors'] = [author.name for author in result.authors]
        metadata['abstract'] = result.summary
        metadata['published'] = result.published
        metadata['pdf_url'] = result.pdf_url
        metadata['categories'] = result.categories
        metadata['primary_category'] = result.primary_category
        metadata['doi'] = result.doi
        metadata_list.append(metadata)
    return metadata_list


if __name__ == "__main__":
    df = pd.read_csv(README_PATH, dtype={'paper_arxiv_id': 'string'})
    arxiv_id_list = df['paper_arxiv_id'].to_list()

    batch_size = 50
    pos = 0
    metadata_list = []
    while True:
        id_list = arxiv_id_list[pos:pos+batch_size]
        if len(id_list) == 0:
            break
        resp = get_metadata_list(id_list)
        metadata_list.extend(resp)

        pos += batch_size
        time.sleep(1)

    metadata_df = pd.DataFrame(metadata_list)
    metadata_df.to_csv('data/2975_arxiv_metadata.csv', index=False)
    metadata_df.to_json('data/2975_arxiv_metadata.jsonl', orient='records', index=False, lines=True)
