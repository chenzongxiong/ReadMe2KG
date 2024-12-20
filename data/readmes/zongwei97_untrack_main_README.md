# UnTrack CVPR 2024

Official implementation of "Single-Model and Any-Modality for Video Object Tracking" CVPR 2024 ([arxiv](https://arxiv.org/abs/2311.15851))

We propose Un-Track, a Unified Tracker of a single set of parameters for any modality, which learns their common latent space with only the RGB-X pairs. This unique shared representation seamlessly binds all modalities together, enabling effective unification and accommodating any missing modality, all within a single transformer-based architecture and without the need for modality-specific fine-tuning. 

# Results

Our ckpt can be found here ([Google Drive](https://drive.google.com/file/d/13GqlmhCKDl6jWJFvAsijuhOXD3kGJqqv/view?usp=sharing))

Put the ckpt into the "models" folder. 

You should then be able to obtain our UnTrack results, which can also be downloaded here ([Google Drive](https://drive.google.com/file/d/1ruCYxvXnmtmfQQxV4t_JAsU9bneyPqIT/view?usp=sharing))

A comparison against [ViPT](https://github.com/jiawen-zhu/ViPT) (SOTA specialized method) and [SeqTrack](https://github.com/microsoft/VideoX/tree/master/SeqTrack) (SOTA Tracker) can found in the following video:

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/MNvKQCeMLxg/0.jpg)](https://www.youtube.com/watch?v=MNvKQCeMLxg)



## Notes

Our shared embedding is somehow similar to a Mixture of Experts (MoE) model. 

The difference is that we manually force the network to pick the best expert, according to the sensor prior, for feature processing. 

We have also developed a generalist and blind tracker, where the MoE is formally introduced and dynamically assigns the most appropriate expert for feature processing. 

More details can be found in the [[Preprint](https://arxiv.org/pdf/2405.17773)] or [[GitHub](https://github.com/supertyd/XTrack)]

# Acknowledgments
This repository is heavily based on [ViPT](https://github.com/jiawen-zhu/ViPT) and [OSTrack](https://github.com/botaoye/OSTrack). Thanks to their great work!
