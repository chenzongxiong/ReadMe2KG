# Paraphrase Detection: Human vs. Machine Content

[![arXiv](https://img.shields.io/badge/arXiv-2303.13989-b31b1b.svg)](https://arxiv.org/abs/2303.13989)

This is the official repository for the paper [Paraphrase Detection: Human vs. Machine Content](https://arxiv.org/abs/2303.13989).

## Setup

We recommend using Python 3.10 for this project.

First install the requirements:
```pip install -r requirements.txt```

---

To use GloVe and Fasttext, you need to place their corresponding pre-trained word vectors into the `models` directory.
 - GloVe: Get the `glove.6B.11d.txt` from [here](https://nlp.stanford.edu/projects/glove/).
 - Fasttext: Get the `cc.en.300.bin` from [here](https://fasttext.cc/docs/en/crawl-vectors.html).

### Experiments

The project has multiple scripts included, each used for separate parts of the experiment.

1) Parse datasets from the `datasets` folder to a unified json format: `parse.py`
2) Create the BERT embeddings for text pairs in `true_data.json` and visualize them with t-SNE: `embedding_handler.py`
3) Apply detection methods (training & testing): `detect_paraphrases.py`
4) Evaluate the detection results: `evaluate.py`
5) Get examples sorted by best / worst / random performance: `get_examples.py`

## Datasets

Not all datasets used in the paper are freely available to the public which is why we do not offer the prediction results on text pairs from these datasets for download. However, you are free to reprocess the experiments using all datasets from the paper once you got access.

This study includes twelve datasets (seven human-generated and five machine-generated). For further information, please refer to the paper.

**Human-generated datasets:** ETPC, QQP, TURL, SaR, MSCOCO, ParaSCI, APH

**Machine-generated datasets:** MPC, SAv2, ParaNMT-50M, PAWS-Wiki, APT

## Results

We evaluated the results of our experiments in the linked paper above. However, we provide additional material here that was not used in the final version of the paper.

<details open>
  <summary>t-SNE visualizations of each datasets BERT embeddings</summary>
  <table>
  <tr>
    <th>Dataset</th>
    <th>Aquisition Type</th>
    <th>Mixed</th>
    <th>Paraphrases Only</th>
  </tr>
  <tr>
    <td>APH</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/APH.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/APH_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>APT</td>
    <td>Machine</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/APT.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/APT_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>ETPC</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/ETPC.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/ETPC_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>MPC</td>
    <td>Machine</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/MPC.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/MPC_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>MSCOCO</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/MSCOCO.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/MSCOCO_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>PAWS-Wiki</td>
    <td>Machine</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/PAWSWiki.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/PAWSWiki_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>ParaNMT-50M</td>
    <td>Machine</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/ParaNMT.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/ParaNMT_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>ParaSCI</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/ParaSCI.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/ParaSCI_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>QQP</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/QQP.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/QQP_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>SAv2</td>
    <td>Machine</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/SAv2.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/SAv2_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>SaR</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/SaR.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/SaR_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>TURL</td>
    <td>Human</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/TURL.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/TURL_paraphrasedOnly.html">Live View</a></td>
  </tr>
  <tr>
    <td>*All Datasets*</td>
   <td>Mixed</td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/total.html">Live View</a></td>
    <td><a href="https://raw.githack.com/jonas-becker/pd-human-vs-machine-content/main/output/figures/total_paraphrasedOnly.html">Live View</a></td>
  </tr>
</table>
</details>

<details>
  <summary>Grid Search Results</summary>
    We performed a 2-fold randomized grid search of 25 iterations once per detection method. The grid search results can be seen in <td><a href="https://github.com/jonas-becker/pd-human-vs-machine-content/tree/main/output/detection/gridsearch">this directory</a></td>.
</details>

<details>
  <summary>One-on-one correlation graphs of detection methods</summary>
    For a detailed view at each one-on-one correlation, please refer to <td><a href="https://github.com/jonas-becker/pd-human-vs-machine-content/tree/main/output/evaluation/correlations">this directory</a></td>.
</details>

## Citation
If you use this repository or our paper for your research work, please cite us in the following way.

```
@misc{becker2023paraphrase,
      title={Paraphrase Detection: Human vs. Machine Content}, 
      author={Jonas Becker and Jan Philip Wahle and Terry Ruas and Bela Gipp},
      year={2023},
      eprint={2303.13989},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
