# Simple Multigraph Convolution Networks (SMGCN)
Pytorch implementation of the paper [WWW'2024] ["Simple Multigraph Convolution Networks"](https://arxiv.org/abs/2403.05014)
![](imgs/smgcn.png)

## TL;DR
Previous methods for multigraph rather **lacks cross-view** interaction or are **too inefficient** to be used in practice. We propose a simple and efficient multigraph convolutional networks based on both edge-level and subgraph-level credible graph extraction from multigraph. We show that our method outperforms previous methods on several multigraph datasets and is more parameter efficient and theoretically sound.

![](imgs/TLDR.png)

## Usage
### Environment
We use torch_geometric and torch as the main framrwork to conduct our experiment. [Mamba](https://github.com/conda-forge/miniforge) is a variant of Conda, which is rewrited in C++. It is also okay to use just conda.
```bash
mamba create -n smgcn python==3.10
mamba install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
mamba install pyg -c pyg
mamba install scikit-learn numpy pandas
```

### Data preparation
We use the standard torch_geometric object to represent the multigraph. Run the `data.py` to download and preprocess the datasets. 
```bash
cd src/DBLP
python data.py
```
Take SMGCN (k=2) as an example, simply run the following command to train the model.
```bash
python SMGCNk=2.py
```

## Parameters Comparison
![](imgs/parameters_ACM.png)
