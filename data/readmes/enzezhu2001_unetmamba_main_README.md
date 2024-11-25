# UNetMamba
## 👀Introduction

**UNetMamba** is the official PyTorch implementation of paper [UNetMamba: An Efficient UNet-Like Mamba for Semantic Segmentation of High-Resolution Remote Sensing Images](https://arxiv.org/abs/2408.11545). (IEEE GRSL undergoing review)

## 📂Folder Structure

Prepare the following folders to organize this repo:
```none
UNetMamba-main
├── UNetMamba
|   ├──config 
|   ├──tools
|   ├──unetmamba_model
|   ├──train.py
|   ├──loveda_test.py
|   ├──vaihingen_test.py
├── pretrain_weights (pretrained weights of backbones)
├── model_weights (model weights trained on ISPRS vaihingen, LoveDA, etc)
├── fig_results (the segmentation results)
├── data
│   ├── LoveDA
│   │   ├── Train
│   │   │   ├── Urban
│   │   │   │   ├── images_png (original)
│   │   │   │   ├── masks_png (original)
│   │   │   │   ├── masks_png_convert (converted masks generated by tools/loveda_mask_convert.py)
│   │   │   │   ├── masks_png_convert_rgb (rgb format converted masks generated by tools/loveda_mask_convert.py)
│   │   │   ├── Rural
│   │   │   │   ├── images_png 
│   │   │   │   ├── masks_png 
│   │   │   │   ├── masks_png_convert
│   │   │   │   ├── masks_png_convert_rgb
│   │   ├── Val (the same with Train)
│   │   ├── Test
│   │   ├── train_val (merge Train and Val)
│   ├── vaihingen (a total of 33 original images)
│   │   ├── test_images (9 original images, randomly selected)
│   │   ├── test_masks (9 original rgb masks)
│   │   ├── test_masks_eroded (9 eroded rgb masks, xxxx_noBoundary.tif)
│   │   ├── train_images (22 original images, randomly selected in remaining images)
│   │   ├── train_masks (22 original rgb masks)
│   │   ├── val_images (remaining 2 original images)
│   │   ├── val_masks (remaining 2 original rgb masks)
│   │   ├── val_masks_eroded (remaining 2 eroded rgb masks, xxxx_noBoundary.tif)
│   │   ├── train_1024 (train set at 1024*1024)
│   │   ├── test_1024 (test set at 1024*1024)
│   │   ├── val_1024 (validation set at 1024*1024)
│   │   ├── ...
```

## 🛠Install
```
conda create -n UNetMamba-main python=3.8
conda activate UNetMamba-main
pip install -r UNetMamba/requirements.txt
```
💁Tips: If you're having difficulty in installing "causal_conv1d" or "mamba_ssm", please refer to [causal_conv1d](https://github.com/Dao-AILab/causal-conv1d/releases) or [mamba_ssm](https://github.com/state-spaces/mamba/releases) to download the wheel files and then pip install them. 
For our UNetMamba, we installed both "causal_conv1d-1.2.0.post2+cu118torch2.0cxx11abiFALSE-cp38-cp38-linux_x86_64.whl" and "mamba_ssm-1.1.1+cu118torch2.0cxx11abiFALSE-cp38-cp38-linux_x86_64.whl". Moreover, UNetMamba is also compatible with the newest version of "causal_conv1d" and "mamba_ssm", please feel free to try😁.

## 🧩Pretrained Weights of Backbones

[pretrain_weights](https://pan.baidu.com/s/19TRZVfz6M9v0VYxiHB6mSA?pwd=82cj) 

## 🧩Pretrained Weights of UNetMamba

[model_weights](https://pan.baidu.com/s/1wVVI1MPY_fnVSYg_5bLIlQ?pwd=mdwe) 

## 💿Data Preprocessing

Download the datasets from the official website and split them as follows.

**1️⃣LoveDA** ([LoveDA official](https://github.com/Junjue-Wang/LoveDA))
```
python UNetMamba/tools/loveda_mask_convert.py --mask-dir data/LoveDA/Train/Rural/masks_png --output-mask-dir data/LoveDA/Train/Rural/masks_png_convert
python UNetMamba/tools/loveda_mask_convert.py --mask-dir data/LoveDA/Train/Urban/masks_png --output-mask-dir data/LoveDA/Train/Urban/masks_png_convert

python UNetMamba/tools/loveda_mask_convert.py --mask-dir data/LoveDA/Val/Rural/masks_png --output-mask-dir data/LoveDA/Val/Rural/masks_png_convert
python UNetMamba/tools/loveda_mask_convert.py --mask-dir data/LoveDA/Val/Urban/masks_png --output-mask-dir data/LoveDA/Val/Urban/masks_png_convert

python UNetMamba/tools/loveda_mask_convert.py --mask-dir data/LoveDA/train_val/Rural/masks_png --output-mask-dir data/LoveDA/train_val/Rural/masks_png_convert
python UNetMamba/tools/loveda_mask_convert.py --mask-dir data/LoveDA/train_val/Urban/masks_png --output-mask-dir data/LoveDA/train_val/Urban/masks_png_convert
```

**2️⃣Vaihingen** ([Vaihingen official](https://www.isprs.org/education/benchmarks/UrbanSemLab/Default.aspx))

Generate the train set.
```
python UNetMamba/tools/vaihingen_patch_split.py 
--img-dir "data/vaihingen/train_images" --mask-dir "data/vaihingen/train_masks" 
--output-img-dir "data/vaihingen/train_1024/images" --output-mask-dir "data/vaihingen/train_1024/masks" 
--mode "train" --split-size 1024 --stride 1024
```
Generate the validation set. (Tip: the eroded one.)
```
python UNetMamba/tools/vaihingen_patch_split.py 
--img-dir "data/vaihingen/val_images" --mask-dir "data/vaihingen/val_masks_eroded" 
--output-img-dir "data/vaihingen/val_1024/images" --output-mask-dir "data/vaihingen/val_1024/masks"
--mode "val" --split-size 1024 --stride 1024 --eroded
```
Generate the test set. (Tip: the eroded one.)
```
python UNetMamba/tools/vaihingen_patch_split.py 
--img-dir "data/vaihingen/test_images" --mask-dir "data/vaihingen/test_masks_eroded" 
--output-img-dir "data/vaihingen/test_1024/images" --output-mask-dir "data/vaihingen/test_1024/masks"
--mode "val" --split-size 1024 --stride 1024 --eroded
```
Generate the masks_1024_rgb (RGB format ground truth labels) for visualization.
```
python UNetMamba/tools/vaihingen_patch_split.py 
--img-dir "data/vaihingen/val_images" --mask-dir "data/vaihingen/val_masks" 
--output-img-dir "data/vaihingen/val_1024/images" --output-mask-dir "data/vaihingen/val_1024/masks_rgb" 
--mode "val" --split-size 1024 --stride 1024 --gt

python UNetMamba/tools/vaihingen_patch_split.py 
--img-dir "data/vaihingen/test_images" --mask-dir "data/vaihingen/test_masks" 
--output-img-dir "data/vaihingen/test_1024/images" --output-mask-dir "data/vaihingen/test_1024/masks_rgb" 
--mode "val" --split-size 1024 --stride 1024 --gt
```

## 🏋Training

"-c" means the path of the config, use different **config** to train different models in different datasets.

```
python UNetMamba/train.py -c UNetMamba/config/loveda/unetmamba.py
python UNetMamba/train.py -c UNetMamba/config/vaihingen/unetmamba.py
```

## 🎯Testing

"-c" denotes the path of the config, Use different **config** to test different models in different datasets

"-o" denotes the output path 

"-t" denotes the test time augmentation (TTA), can be [None, 'lr', 'd4'], default is None, 'lr' is flip TTA, 'd4' is multiscale TTA

"--rgb" denotes whether to output masks in RGB format

**1️⃣LoveDA** ([Online Testing](https://codalab.lisn.upsaclay.fr/competitions/421))
```
python UNetMamba/loveda_test.py -c UNetMamba/config/loveda/unetmamba.py -o fig_results/loveda/unetmamba_test
python UNetMamba/loveda_test.py -c UNetMamba/config/loveda/unetmamba.py -o fig_results/loveda/unetmamba_test -t 'd4'
python UNetMamba/loveda_test.py -c UNetMamba/config/loveda/unetmamba.py -o fig_results/loveda/unetmamba_rgb -t 'd4' --rgb --val
```

**2️⃣Vaihingen**
```
python UNetMamba/vaihingen_test.py -c UNetMamba/config/vaihingen/unetmamba.py -o fig_results/vaihingen/unetmamba_test
python UNetMamba/vaihingen_test.py -c UNetMamba/config/vaihingen/unetmamba.py -o fig_results/vaihingen/unetmamba_test -t 'lr'
python UNetMamba/vaihingen_test.py -c UNetMamba/config/vaihingen/unetmamba.py -o fig_results/vaihingen/unetmamba_rgb --rgb
```

## 🍀Citation

If you find this project useful in your research, please consider citing：
[UNetMamba: An Efficient UNet-Like Mamba for Semantic Segmentation of High-Resolution Remote Sensing Images](https://arxiv.org/abs/2408.11545).
```
@article{zhu2024unetmamba,
  title={UNetMamba: An Efficient UNet-Like Mamba for Semantic Segmentation of High-Resolution Remote Sensing Images},
  author={Zhu, Enze and Chen, Zhan and Wang, Dingkai and Shi, Hanru and Liu, Xiaoxuan and Wang, Lei},
  journal={arXiv preprint arXiv:2408.11545},
  year={2024}
}
```

## ❤Acknowledgement

- [GeoSeg](https://github.com/WangLibo1995/GeoSeg)
- [SSRS](https://github.com/sstary/SSRS)
- [mamba](https://github.com/state-spaces/mamba)
- [VMamba](https://github.com/MzeroMiko/VMamba)
- [causal-conv1d](https://github.com/Dao-AILab/causal-conv1d)
- [LoveDA](https://github.com/Junjue-Wang/LoveDA)
- [Swin-UMamba](https://github.com/JiarunLiu/Swin-UMamba)
- [CM-UNet](https://github.com/XiaoBuL/CM-UNet)