## CycleGAN Face-off

This is a modified version of CycleGAN for the paper "CycleGAN Face-off" by Xiaohan Jin, Ye Qi and Shangxuan Wu.

[Paper](https://arxiv.org/abs/1712.03451). Note that this is not the repo for the video in [here](https://www.youtube.com/watch?v=Fea4kZq0oFQ).

This repo contains the code which adds:
1. SSIM loss. Usage: adding `--with_ssim` in your training script.
1. Better testing script for generating a whole video. Usage: `python generate_fake_sequence.py`
1. Training scripts for some of the experiments like Shangxuan <-> Russ etc.
1. For weighted loss of facial mask, please use [this repo](https://github.com/Sharon-Jin/pytorch-CycleGAN-and-pix2pix).
1. For double_d setting, please use [this_repo](https://github.com/CharlotteKay/pytorch-CycleGAN-and-pix2pix).
1. Adding make_video folder for making a comparison video (such as make_video/jin/output_with_sould.mkv). Usage: `python jin.py`. The result video is [here](https://github.com/ShangxuanWu/pytorch-CycleGAN-and-pix2pix/blob/master/make_video/qi/demo.mkv).
1.  Adding draw_plot folder for analysing plots for the log files. Usage: `python draw_plot.py`. The result plot is [here](https://github.com/ShangxuanWu/pytorch-CycleGAN-and-pix2pix/blob/master/draw_plot/Cyc_A.png).
