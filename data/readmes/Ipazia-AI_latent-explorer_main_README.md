![Logo](https://github.com/Ipazia-AI/latent-explorer/raw/main/images/logo.png)

[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]
[![Static Badge](https://img.shields.io/badge/pyPI-latent--explorer-red)](https://pypi.org/project/latent-explorer)
[![Dynamic TOML Badge](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fgithub.com%2FIpazia-AI%2Flatent-explorer%2Fraw%2Fmain%2Fpyproject.toml&query=%24.project.version&label=release&color=green)](https://github.com/Ipazia-AI/latent-explorer/releases)
[![Static Badge](https://img.shields.io/badge/website-online-green)](https://github.com/Ipazia-AI)
[![Static Badge](https://img.shields.io/badge/DOI-10.48550%2FarXiv.2404.03623-orange)](
https://doi.org/10.48550/arXiv.2404.03623)


Latent-Explorer is the Python implementation of the framework proposed in the paper [*Unveiling LLMs: The Evolution of Latent Representations in a Dynamic Knowledge Graph*](https://arxiv.org/abs/2404.03623) to appear in the 1<sup>st</sup> [Conference of Language Modeling](https://colmweb.org/index.html) (COLM).

## Overview
This framework decodes factual knowledge embedded in token representations from a vector space into a set of ground predicates, exhibiting its layer-wise evolution through a dynamic knowledge graph. 
It employs separate model inferences, with the technique of activation patching, to interpret the semantics embedded within the latent representations of the original inference.
This framework can be employed to study the vector space of LLMs to address several research questions, including:
(i) which factual knowledge LLMs use in claim verification,
(ii) how this knowledge evolves throughout the model's inference, and
(iii) whether any distinctive patterns exist in this evolution.

![Framework](https://github.com/Ipazia-AI/latent-explorer/raw/main/images/framework.png)

![Contribution](https://github.com/Ipazia-AI/latent-explorer/raw/main/images/contribution.png)


## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the Python package

```bash
pip install latent-explorer
```

or download the [repository](https://github.com/Ipazia-AI/latent-explorer) and install the package with 
` pip install -e . `

## Demo
The folder `tutorial` includes a script showcasing the pipeline [`tutorial/script.py`](./tutorial/script.py)

## Usage

### Import the package
```python
import latent_explorer
```

### Initialize the application with the LLM and the inputs
```python
explorer = latent_explorer.LatentExplorer(
  model_name = "meta-llama/llama-2-7b-chat-hf", 
  inputs = ["The capital of France is Paris"]
)
```
### Prepare the textual prompts
```python
explorer.generate_prompts(verbose = True)
```

### Perform the inference and get the hidden states
```python
explorer.inference(parse_output = True, output_hidden_states = True)
```

### Probe each hidden states
```python
results = explorer.probe_hidden_states()
```

### Save the textual results
```python
latent_explorer.utils.save_results(results, folder_path = "outputs")
```

### Generate the dynamic knowledge graphs
```python
tg = latent_explorer.TempoGrapher(results)
```

### Get the graphs
```python
graphs = tg.get_graphs()
```

### Generate and save the graphical figures
```python
tg.save_graphs(folder_path = "outputs")
```

## Language models available
This package inherits all of the LLMs supported by the [LitGPT](https://github.com/Lightning-AI/litgpt/blob/main/tutorials/download_model_weights.md) package.
This framework works with instruction-tuned language models, such as those named with the suffixes "inst", "instruct", or "chat". 

```python
models = latent_explorer.utils.all_supported_models()
```

## Computational resources
Since this framework performs multiple language model inferences, using a GPU is recommended ([see CUDA](https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html)). This framework has been tested with using two GPU-based configurations: (1x) *NVIDIA® A100-40GB*, and (4x) *NVIDIA® T4 Tensor Core - 16GB*.   

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements
This implementation is powered by [LitGPT](https://github.com/Lightning-AI/litgpt), conceptualised, designed and developed by [Marco Bronzini](https://www.linkedin.com/in/bronzinimarco).
This work has been funded by [Ipazia S.p.A.](https://ipazia.com)

## Citation
If you use this package or its code in your research, please cite the following work:

```bibtex
@inproceedings{bronzini2024unveiling,
  title     = {Unveiling LLMs: The evolution of latent representations in a dynamic knowledge graph},
  author    = {Bronzini, Marco and Nicolini, Carlo and Lepri, Bruno and Staiano, Jacopo and Passerini, Andrea},
  booktitle = {First Conference on Language Modeling},
  year      = {2024},
  url       = {https://openreview.net/forum?id=dWYRjT501w}
}
```

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg