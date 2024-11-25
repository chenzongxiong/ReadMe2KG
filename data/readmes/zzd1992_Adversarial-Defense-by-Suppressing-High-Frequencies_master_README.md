# Adversarial defense by suppressing high frequencies
We develop a **high frequency suppression module** based on discrete Fourier transform which is used for adversarial defense. It is **efficient, differentiable and controllable**. Together with adversarial training, we won the fifth place of the [IJCAI-2019 Alibaba Adversarial AI Challenge](https://security.alibaba.com/alibs2019) (AAAC). This project is a minimum implementation of our solution.

The motivation of our solution is that adversarial perturbations are dominated by high frequencies while information on clean images converges on low frequencies. Thus, if we suppress high frequencies of adversarial images, the effects of adversarial perturbations will be reduced while the basic information on clean images will be preserved. Our module is processed in frequency domain. See details in our [technical report](https://arxiv.org/abs/1908.06566) and presentation.

# Results on AAAC
There are about 110,000 images with 110 categories for electric business. The goal is to give a right classification of an image under adversarial perturbations which are generated by top-5 **black box attackers**. The score of a defense model for an image is measured as 0 if misclassified else L2 norm of perturbations.

| high frequency suppression | adversarial training | model ensemble | score   |
| :------:                   | :------:             | :------:       | ------: |
| no                         | no                   | no             | 2.04    |
| no                         | yes                  | no             | 9.99    |
| yes                        | no                   | no             | 14.97   |
| yes                        | yes                  | no             | 19.05   |
| yes                        | yes                  | yes            | 19.75   |

As we can see, our high frequency suppression module works well. It is even better than adversarial training on this challenge. The official leaderboard is [here](https://tianchi.aliyun.com/competition/entrance/231701/rankingList/5).

# How to use our code
### Requirements
PyTorch >= 0.4.0

### Prepare your data
First, modify the meta information in `cfg.py`. `root` means the root path of your data. `crop_size` is the size which images are cropped to during training. We suggest you resize your images into a fixed size before training.

Then, generate text files of the training data and validation data. Each line of the file records the relative path and the label of an image. The label is an integer started from 0. Here is an example of a line:
```
image_00000.jpg,0
```
### Run the scripts
Suppose your training data is recorded in `train.txt` and your validation data is recorded in `valid.txt`. Then train the base model (without adversarial training):
```bash
python train_base.py train.txt valid.txt
```
The model file will be saved. Suppose it is `base.pth`. Then train the final model (with adversarial training):
```bash
python train_adv.py train.txt valid.txt -pth base.pth
```
See the help of `train_base.py` and `train_adv.py` for more details. The default network is **ResNet-18**.

# Citation
If you find our method is useful, please cite our technical report:
```
@article{zhang2019adversarial,
title={Adversarial Defense by Suppressing High-frequency Components.},
author={Zhang, Zhendong and Jung, Cheolkon and Liang, Xiaolong},
journal={arXiv: Computer Vision and Pattern Recognition},
year={2019}}
```