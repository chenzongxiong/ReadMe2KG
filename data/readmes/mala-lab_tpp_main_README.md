# TPP
Code for Replay-and-Forget-Free Graph Class-Incremental Learning: A Task Profiling and Prompting Approach ([TPP](https://arxiv.org/pdf/2410.10341)) (NeurIPS 2024).

## Abstract

Class-incremental learning (CIL) aims to continually learn a sequence of tasks, with each task consisting of a set of unique classes. Graph CIL (GCIL) follows the same setting but needs to deal with graph tasks (e.g., node classification in a graph). The key characteristic of CIL lies in the absence of task identifiers (IDs) during inference, which causes a significant challenge in separating classes from different tasks (i.e., inter-task class separation). Being able to accurately predict the task IDs can help address this issue, but it is a challenging problem. In this paper, we show theoretically that accurate task ID prediction on graph data can be achieved by a Laplacian smoothing-based graph task profiling approach, in which each graph task is modeled by a task prototype based on Laplacian smoothing over the graph. It guarantees that the task prototypes of the same graph task are nearly the same with a large smoothing step, while those of different tasks are distinct due to differences in graph structure and node attributes. Further, to avoid the catastrophic forgetting of the knowledge learned in previous graph tasks, we propose a novel graph prompting approach for GCIL which learns a small discriminative graph prompt for each task, essentially resulting in a separate classification model for each task. The prompt learning requires the training of a single graph neural network (GNN) only once on the first task, and no data replay is required thereafter, thereby obtaining a GCIL model being both replay-free and forget-free. Extensive experiments on four GCIL benchmarks show that i) our task prototype-based method can achieve 100\% task ID prediction accuracy on all four datasets, ii) our GCIL model significantly outperforms state-of-the-art competing methods by at least 18\% in average CIL accuracy, and iii) our model is fully free of forgetting on the four datasets.
![Framework](framework.png)

## Get Started
To run the code, the following packages are required to be installed:

-python==3.8.19

-torch==1.13.1

-dgl==1.0.1+cu117

## Train
To get the results on CoraFull and Arxiv, just run the following command:

     sh run.sh

## Acknowledgment
This code is implemented based on [CGLB](https://github.com/QueuQ/CGLB/tree/master). Please refer to CGLB for more baselines and implementation details.

## Citation
Please acknowledge our work via the following bibliography if you find our work/code useful:
```bibtex
@article{niu2024replay,
  title={Replay-and-Forget-Free Graph Class-Incremental Learning: A Task Profiling and Prompting Approach},
  author={Niu, Chaoxi and Pang, Guansong and Chen, Ling and Liu, Bing},
  journal={arXiv preprint arXiv:2410.10341},
  year={2024}
}