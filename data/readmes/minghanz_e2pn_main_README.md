
# E2PN: Efficient SE(3)-Equivariant Point Network (CVPR 2023)

[![Watch the video](https://img.youtube.com/vi/B4XDxd0h08I/hqdefault.jpg)](https://youtu.be/B4XDxd0h08I)


This repository contains the official code for the CVPR 2023 paper **E2PN: Efficient SE(3)-Equivariant Point Network** [[paper](https://openaccess.thecvf.com/content/CVPR2023/html/Zhu_E2PN_Efficient_SE3-Equivariant_Point_Network_CVPR_2023_paper.html)] [[poster and slides](https://cvpr2023.thecvf.com/virtual/2023/poster/21183)]. 


## Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Experiments](#experiments)
4. [Contacts](#contacts)

## Introduction

E2PN is a SE(3)-equivariant network architecture designed for deep point cloud analysis. It largely improves the efficiency in terms of memory consumption and running speed for equivariant point cloud feature learning. 

It mainly includes a SE(3)-equivariant convolution on $S^2\times \mathbb{R}^3$ which is a homogeneous space of SE(3), and a permutation layer to recover SE(3) information from the features in the homogeneous space. 

<!-- ![](https://github.com/nintendops/EPN_PointCloud/blob/main/media/spconv.png) -->



## Usage
Our code is developed based on an open-sourced existing work [EPN](https://github.com/nintendops/EPN_PointCloud). We use the same dependencies as the [EPN](https://github.com/nintendops/EPN_PointCloud) repository. 

The code has been tested on Python 3.7.12, PyTorch 1.11.0 and CUDA 11.3.1. The module and additional dependencies can be set up with 
```
cd vgtk
python setup.py build_ext --inplace
```

## Experiments

**Datasets**

The rotated Modelnet40 point cloud dataset is generated from the [Aligned Modelnet40 subset](https://github.com/lmb-freiburg/orion) and can be downloaded using this [link](https://drive.google.com/file/d/1xRoYjz2KCwkyIPf21E-WKIZkjLYabPgJ/view?usp=sharing).

The original 3DMatch training and evaluation dataset can be found [here](https://3dmatch.cs.princeton.edu/#keypoint-matching-benchmark). We followed [this repo](https://github.com/craigleili/3DLocalMultiViewDesc) to preprocess rgb frames into fused fragments and extract matching keypoints for training. The preprocessed data ready for training can be downloaded [here](https://drive.google.com/file/d/1ME42RjtrNJNz1zSTBrO2NtG89fsOkQLv/view?usp=sharing) (146GB). We also prepared to preprocessed 3DMatch evaluation dataset [here](https://drive.google.com/file/d/14ZGJZHuQLhg87En4C5po6bgTFn4tns4R/view?usp=sharing) (40GB), where local patches around testing keypoints have been precomputed.

<!-- **Pretrained Model**

Pretrained model can be downloaded using this [link](https://drive.google.com/file/d/1vy9FRGWQsuVi4nf--YIqg_8yHFiWWJhh/view?usp=sharing) -->

### ModelNet40 Classification

**Training**

The following lines can be used for the training of each model. In all experiments, `PATH_TO_LOG`, `PATH_TO_MODELNET40`, and `PATH_TO_3DMATCH_TRAIN` are constant and no need to change across experiments. 

```
# E2PN mode
python run_modelnet.py experiment --experiment-id cls_s2(free to choose) --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 \
model --flag permutation --kanchor 12 --feat-all-anchors --drop_xyz

# EPN mode
python run_modelnet.py experiment --experiment-id cls_so3 --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 \
train_loss --cls-attention-loss

# KPConv mode
python run_modelnet.py experiment --experiment-id cls_kp --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 \
model --flag max --kpconv --kanchor 1

# ESCNN mode
python run_modelnet_voxel.py experiment --experiment-id cls_v(free to choose) --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 \
train --sigma 0.03 model --freq 3 --test_batch_size 24
```

You can set `--debug-mode check_equiv` to make sure the model satisfies the equivariant condition before starting formal training. 

Running ESCNN models (an equivariant baseline based on steerable CNNs and voxel representation) requires installing corresponding packages, see [ESCNN](https://github.com/QUVA-Lab/escnn). You will also need `point_cloud_utils` package. 

**Evaluation**

Use the same command as training, except adding `--run-mode eval` and `-r PATH_TO_CKPT(full path to pth file)`. For example:

```
# E2PN mode
python run_modelnet.py experiment --experiment-id cls_s2 --run-mode eval \
--model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 -r PATH_TO_CKPT \
model --flag permutation --kanchor 12 --feat-all-anchors --drop_xyz
```

You can specify `--shift --jitter --dropout_pt` for random translation, noise, and point dropout as augmentation in training. Set `--train_rot` for different options of training rotational augmentation. Set `--test_aug` to use the training augmentation for testing and `--test_rot` to specify the type of rotations used in testing, or set `--group_test` to test under various conditions all at once. 

### ModelNet40 Shape Alignment
**Training**
```
# E2PN mode
python run_modelnet_rotation.py experiment --experiment-id rot_s2 --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 \
model --flag permutation --kanchor 12

# EPN mode
python run_modelnet_rotation.py experiment --experiment-id rot_so3 --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40

# KPConv mode
python run_modelnet_rotation.py experiment --experiment-id rot_kp --model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 \
model --kpconv --kanchor 1
```

You can set `--debug-mode check_equiv` to make sure the model satisfies the equivariant condition before starting formal training. 

**Evaluation**

Similarly, add `--run-mode eval` and `-r PATH_TO_CKPT(full path to pth file)`. For example:

```
# E2PN mode
python run_modelnet_rotation.py experiment --experiment-id rot_s2 --run-mode eval \
--model-dir PATH_TO_LOG -d PATH_TO_MODELNET40 -r PATH_TO_CKPT \
model --flag permutation --kanchor 12
```
To obtain reproducible evaluation result, set `-s SOME_INTEGER` as the random seed. 

### 3DMatch Keypoint Matching
**Training**
```
# E2PN mode
python run_3dmatch.py experiment --experiment-id inv_s2 --model-dir PATH_TO_LOG -d PATH_TO_3DMATCH_TRAIN \
train --npt 16 model --kanchor 12

# EPN mode
python run_3dmatch.py experiment --experiment-id inv_so3 --model-dir PATH_TO_LOG -d PATH_TO_3DMATCH_TRAIN \
train --npt 16

# KPConv mode
python run_3dmatch.py experiment --experiment-id inv_kp --model-dir PATH_TO_LOG -d PATH_TO_3DMATCH_TRAIN \
train --npt 16 \
model --kpconv --kanchor 1
```

**Evaluation**

Similarly, add `--run-mode eval` and `-r PATH_TO_CKPT(full path to pth file)`. For example:

```
# E2PN mode
python run_3dmatch.py experiment --experiment-id inv_s2 --run-mode eval \
--model-dir PATH_TO_LOG -d PATH_TO_3DMATCH_EVAL -r PATH_TO_CKPT \
model --kanchor 12
```

## Citation
If you find our project useful in your research, please consider citing:

```
@inproceedings{zhu2023e2pn,
  title={E2PN: Efficient SE (3)-equivariant point network},
  author={Zhu, Minghan and Ghaffari, Maani and Clark, William A and Peng, Huei},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={1223--1232},
  year={2023}
}
```
