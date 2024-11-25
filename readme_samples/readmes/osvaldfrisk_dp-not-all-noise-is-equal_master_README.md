# Not all noise is accounted equally

This repository contains the code to reproduce the experiments of

[**Not all noise is accounted equally: How differentially private learning benefits from large sampling rates**](https://arxiv.org/abs/2110.06255)

*Friedrich Dörmann, Osvald Frisk, Lars Nørvang Andersen, Christian Fischer Pedersen*

Published as conference paper at 2021 IEEE International Workshop on Machine Learning for Signal Processing, Oct. 25–28, 2021, Gold Coast, Australia.

## How to reproduce the results

To reproduce the results from the experiments section

- Clone the repo
- Install the dependencies
- Run `src/main.py`

Parameters for main file:

- `--dataset`: "MNIST", "FashionMNIST" or "CIFAR10"
- `--parameter-set`: 1, 2 or 3

These configurations correspond to the 3 experiments with the respective datasets, as seen in Table 2 of the paper.
