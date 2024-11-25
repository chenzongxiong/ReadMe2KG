# [Perception-Guided Quality Metric of 3D Point Clouds Using Hybrid Strategy (TIP2024)](https://arxiv.org/abs/2407.03885)
by Yujie Zhang, Qi Yang,  Yiling Xu, Shan Liu

This respository is about a full-reference point cloud quality metric based on a hybrid strategy. The key idea is that **the human visual system (HVS) dynamically tackles visual information according to different distortion levels (i.e., distortion detection for high-quality samples and appearance perception for low-quality samples)**.

## Introduction
![image text](https://github.com/zhangyujie-1998/PHM/blob/main/fig/framwork.png)

Full-reference point cloud quality assessment (FR-PCQA) aims to infer the quality of distorted point clouds with available references. Most of the existing FR-PCQA metrics ignore the fact that the human visual system (HVS) dynamically tackles visual information according to different distortion levels (i.e., distortion detection for high-quality samples and appearance perception for low-quality samples) and measure point cloud quality using unified features.  To bridge the gap, in this paper, we propose a perception-guided hybrid metric (PHM) that adaptively leverages two visual strategies with respect to distortion degree to predict point cloud quality: to measure visible difference in high-quality samples, PHM takes into account the masking effect and employs texture complexity as an effective compensatory factor for absolute difference; on the other hand, PHM leverages spectral graph theory to evaluate appearance degradation in low-quality samples. Variations in geometric signals on graphs and changes in the spectral graph wavelet coefficients are utilized to characterize geometry and texture appearance degradation, respectively. Finally, the results obtained from the two components are combined in a non-linear method to produce an overall quality score of the tested point cloud. The results of the experiment on five independent databases show that PHM achieves state-of-the-art (SOTA) performance and offers significant performance improvement in multiple distortion environments.
## Demo
We provide a demo that evaluate the quality of "longdress_vpcc_r01.ply" in the ```data``` folder. You need first to unzip the "gspbox.zip" to get the ```gspbox``` folder. Then you can run the code in the Matlab
```
>> demo.m
```
It is expected to output
```
>> PHM score is: %d
```

## Results
- Datasets
1. [SJTU-PCQA](https://smt.sjtu.edu.cn/database/point-cloud-subjective-assessment-database/)
2. [WPC](https://github.com/qdushl/Waterloo-Point-Cloud-Database)
3. [LS-PCQA](https://smt.sjtu.edu.cn/database/large-scale-point-cloud-quality-assessment-dataset-ls-pcqa/)
4. [M-PCCD](https://www.epfl.ch/labs/mmspg/downloads/quality-assessment-for-point-cloud-compression/)
5. [ICIP2020](https://emergimg.di.ubi.pt/icip2020PC.html)


- Quantitative comparison
![image text](https://github.com/zhangyujie-1998/PHM/blob/main/fig/result.png)


- Results reproduction

The experiment results are related to the sampled seeds used for space segmentation. If you want to reproduce the results in our paper, you can directly utilize the seeds in the ```sample``` folder. We provide the corresponding seed (generated by farthest point sampling) for each reference on the above five databases. You can also refer to the ```demo_fps.m``` file to generate seeds for new datasets.


## Citation
If you find this work is helpful, please consider citing:
```
@article{zhang2024perception,
  title={Perception-Guided Quality Metric of 3D Point Clouds Using Hybrid Strategy},
  author={Zhang, Yujie and Yang, Qi and Xu, Yiling and Liu, Shan},
  journal={arXiv preprint arXiv:2407.03885},
  year={2024}
}
```