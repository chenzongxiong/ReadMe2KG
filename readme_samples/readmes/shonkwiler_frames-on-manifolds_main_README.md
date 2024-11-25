# Frames on Manifolds

The purpose of this repository is to disseminate the numerical experiments reported in the following paper:

* Samuel A. Ballas, Tom Needham, and Clayton Shonkwiler. [On the existence of Parseval frames for vector bundles](https://arxiv.org/abs/2312.13488). Preprint, 2023. [arXiv:2312.13488 [math.DG]](https://arxiv.org/abs/2312.13488).

The numerical experiments are performed in the [Mathematica](https://www.wolfram.com/mathematica/) notebook [`vf.nb`](vf.nb). If you do not have Mathematica installed, this can be opened (but not evaluated) with the free [Wolfram Player](https://www.wolfram.com/player/).

Note that the notebook evaluates simplex noise using [lmas](https://github.com/lmas)’s [Python port](https://github.com/lmas/opensimplex) of Kurt Spencer’s [original code](https://github.com/KdotJPG/OpenSimplex2). To use this functionality, you’ll need to run `pip install opensimplex`.

This work was supported by the National Science Foundation ([DMS–2107808](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2107808) and [DMS–2107700](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2107700)).
