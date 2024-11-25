
# Adaptive Masked Proxies for Few Shot Segmentation

Implementation used in our paper:
* Adaptive Masked Proxies for Few Shot Segmentation

* [Extended Version](https://arxiv.org/pdf/1902.11123v2.pdf): Accepted in ICCV'19 for the Extended version.

* [Workshop Paper](https://openreview.net/forum?id=SkeoV4yZUV): Accepted in Learning from Limited Labelled Data Workshop in Conjunction with ICLR'19.

## Description
Deep learning has thrived by training on large-scale datasets. However, for continual learning in applications such as robotics, it is critical to incrementally update its model in a sample efficient manner. We propose a novel method that constructs the new class weights from few labelled samples in the support set without back-propagation, relying on our adaptive masked proxies approach. It utilizes multi-resolution average pooling on the output embeddings masked with the label to act as a positive proxy for the new class, while fusing it with the previously learned class signatures. Our proposed method is evaluated on PASCAL-5i dataset and outperforms the state of the art in the 5-shot semantic segmentation. Unlike previous methods, our proposed approach does not require a second branch to estimate parameters or prototypes, which enables it to be used with 2-stream motion and appearance based segmentation networks. The proposed adaptive proxies allow the method to be used with a continuous data stream. Our online adaptation scheme is evaluated on the DAVIS and FBMS video object segmentation benchmark. We further propose a novel setup for evaluating continual learning of object segmentation which we name incremental PASCAL (iPASCAL) where our method has shown to outperform the baseline method.

<div align="center">
<img src="https://github.com/MSiam/AdaptiveMaskedProxies/blob/master/figures/adapproxy.png" width="70%" height="70%"><br><br>
</div>

## Qualitative Evaluation on PASCAL-5i
1-way 1-shot segmentation
 <div class="row">
  <div class="column">
 <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/sprt_1.png" alt="" width="30%" height="30%">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/sprt_2.png" alt="" width="30%" height="30%">
   <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/sprt_6.png" alt="" width="30%" height="30%">
  </div>
  <div class="column">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/pred_1.png" alt="" width="30%" height="30%">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/pred_2.png" alt="" width="30%" height="30%">   
   <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/pred_6.png" alt="" width="30%" height="30%">
 </div>
</div> 

## Qualitative Evaluation on LfW
2-way 1-shot segmentation
 <div class="row">
  <div class="column">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_sprt_img1.png" alt="" width="20%" height="20%">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_sprt_img2.png" alt="" width="20%" height="20%">   
   <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_sprt_img3.png" alt="" width="20%" height="20%">
  </div>
  <div class="column">
 <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_sprt_gt1.png" alt="" width="20%" height="20%">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_sprt_gt2.png" alt="" width="20%" height="20%">
   <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_sprt_gt5.png" alt="" width="20%" height="20%">
  </div>
 <div class="column">
 <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_img1.png" alt="" width="20%" height="20%">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_img2.png" alt="" width="20%" height="20%">
   <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_img3.png" alt="" width="20%" height="20%">
  </div>
 <div class="column">
 <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_pred_img1.png" alt="" width="20%" height="20%">
    <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_pred_img2.png" alt="" width="20%" height="20%">
   <img src="https://raw.githubusercontent.com/MSiam/AdaptiveMaskedProxies/master/figures/lfw_pred_img3.png" alt="" width="20%" height="20%">
  </div>
</div> 

## Environment setup

Current Code is tested on torch 0.4.1 and torchvision 0.2.0. and python 3.6.9

```
virtualenv --system-site-packages -p python3 ./venv
source venv/bin/activate
pip install -r requirements.txt
```

## Pre-Trained Weights

Download trained weights [here](https://drive.google.com/drive/folders/1wJXetJCGkT_xej8Jr8Mrj9vJUHN8EtJu?usp=sharing) fcn8s_pasal_normalize_training.zip

## Python Notebook Demo
To use with google Colab upload notebook with the following url
[Demo](https://github.com/MSiam/AdaptiveMaskedProxies/blob/master/AdapProxy.ipynb)

## Training
* Copy dataset/train_aug.txt to PASCALVOC_PATH/ImageSets/Segmentation/ to ensure no overlap between val and train data
* Modify config.json to point to path for SBD
* Run the following:
```
python train.py --config configs/fcn8s_pascal.yaml
```

## Test few shot setting 
* Unzip fcn8s_pasal_normalize_training.zip Which has all updated weights after fixing CosineSimLayer

```
python fewshot_imprinted.py --binary BINARY_FLAG --config configs/fcn8s_pascal_imprinted.yml --model_path MODEL_PATH --out_dir OUT_DIR
```
* MODEL_PATH: path for model trained on same fold testing upon.
* OUT_DIR: output directory to save visualization if needed. (optional)
* BINARY_FLAG: 1: evaluate binary with OSLSM method, 2: evaluates binary using coFCN method.

## Updated Results
The updated results after using CosineSimLayer during training that normalizes both features and weights

Fold | 0 | 1 | 2 | 3 | mIoU
-----|-- |---|---|---|-----
AMP - 1shot | 39.6 | 52.1 | 46.7 | 34.6 | 43.3
AMP - 5shot | 44.5 | 57.3 | 50.8 | 41.4 | 48.5

## Configuration
* arch: dilated_fcn8s | fcn8s | reduced_fcn8s
* lower_dim: True (uses 256 nchannels in last layer) | False (uses 4096)
* weighted_mask: True (uses weighted avg pooling based on distance transform)| False (uses mased avg pooling)
* use_norm: True (normalize embeddings during inference)| False
* use_normalize_train: True
* use_scale: False: True (Learn scalar hyperaparameter) | False
* dataset: pascal5i (few shot OSLSM setting)| pascal
* fold: 0 | 1 | 2 | 3
* k_shot: 1 | 5

## Visualize predictions and support set
```
python vis_preds.py VIS_FOLDER
```

## Guide to Reproducing Experiments in the paper
Check [Experiments.md](https://github.com/MSiam/AdaptiveMaskedImprinting/blob/master/Experiments.md)
Results reported in the short version paper were using the Foregound IoU and the dataloader provided random pairs that weren't exactly same as the ones used by OSLSM.
While the corrected results in the extended version reported using Foreground IoU per class and using the pairs generated by OSLSM code exactly.

To reproduce results using our dataloader instead of reading random pairs generated from OSLSM code check prev_results branch.

## Related Repos:
* Based on semantic segmentation repo:
[SemSeg](https://github.com/meetshah1995/pytorch-semseg)
* Pascal5i loader based on OSLSM repo loader:
[OSLSM](https://github.com/lzzcd001/OSLSM)

## References

Please cite our paper if you find it useful in your research

```
@InProceedings{Siam_2019_ICCV,
author = {Siam, Mennatullah and Oreshkin, Boris N. and Jagersand, Martin},
title = {AMP: Adaptive Masked Proxies for Few-Shot Segmentation},
booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
month = {October},
year = {2019}
} 
```

