---
title: 'AeroPath: automatic airway segmentation using deep learning'
colorFrom: indigo
colorTo: indigo
sdk: docker
app_port: 7860
emoji: 🫁
pinned: false
license: mit
app_file: demo/app.py
---

<div align="center">
<h1 align="center">🫁 AeroPath 🤗</h1>
<h3 align="center">An airway segmentation benchmark dataset with challenging pathology</h3>

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/raidionics/AeroPath/blob/main/LICENSE.md)
[![CI/CD](https://github.com/raidionics/AeroPath/actions/workflows/deploy.yml/badge.svg)](https://github.com/raidionics/AeroPath/actions/workflows/deploy.yml)
<a target="_blank" href="https://huggingface.co/spaces/andreped/AeroPath"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>
<a href="https://colab.research.google.com/gist/andreped/6070d1d2914a9ce5847d4b3e687188b7/aeropath-load-dataset-example.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10069288.svg)](https://doi.org/10.5281/zenodo.10069288)
[![paper](https://img.shields.io/badge/arXiv-preprint-D12424)](https://arxiv.org/abs/2311.01138)

**AeroPath** was developed by SINTEF Medical Image Analysis to accelerate medical AI research.

</div>

## [Brief intro](https://github.com/raidionics/AeroPath#brief-intro)

This repository contains the AeroPath dataset described in ["_AeroPath: An airway segmentation benchmark dataset with challenging pathology_"](https://arxiv.org/abs/2311.01138).  A web application was also developed in the study, to enable users to easily test our deep learning model on their own data. The application was developed using [Gradio](https://www.gradio.app) for the frontend and the segmentation is performed using the [Raidionics](https://raidionics.github.io/) backend.

The dataset is made openly available at [Zenodo](https://zenodo.org/records/10069289) and [the Hugging Face Hub](https://huggingface.co/datasets/andreped/AeroPath). Click any of the two hyperlinks to access the dataset.

## [Dataset](https://github.com/raidionics/AeroPath#data) <a href="https://colab.research.google.com/gist/andreped/6070d1d2914a9ce5847d4b3e687188b7/aeropath-load-dataset-example.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

### [Accessing dataset](https://github.com/raidionics/AeroPath#accessing-dataset)

The dataset contains 27 CTs with corresponding airways and lung annotations. The folder structure is described below.

The easiest way to access the data is in Python with Hugging Face's [datasets](https://pypi.org/project/datasets/) package:
```
from datasets import load_dataset

# downloads data from Zenodo through the Hugging Face hub
# - might take several minutes (~5 minutes in CoLab)
dataset = load_dataset("andreped/AeroPath")
print(dataset)

# list paths of all available patients and corresponding features (ct/airways/lungs)
for d in dataset["test"]:
  print(d)
```

A detailed interactive demo on how to load and work with the data can be seen on CoLab. Click the CoLab badge <a href="https://colab.research.google.com/gist/andreped/6070d1d2914a9ce5847d4b3e687188b7/aeropath-load-dataset-example.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> to see the notebook or alternatively click [here](https://github.com/raidionics/AeroPath/blob/main/notebooks/aeropath-load-dataset-example.ipynb) to see it on GitHub.

### [Dataset structure](https://github.com/raidionics/AeroPath#dataset-structure)

```
└── AeroPath.zip
    ├── README.md
    └──  AeroPath/
        ├── 1/
        │   ├── 1_CT_HR.nii.gz
        │   ├── 1_CT_HR_label_airways.nii.gz
        │   └── 1_CT_HR_label_lungs.nii.gz
        ├── [...]
        └── 27/
            ├── 27_CT_HR.nii.gz
            ├── 27_CT_HR_label_airways.nii.gz
            └── 27_CT_HR_label_lungs.nii.gz
```

## [Demo](https://github.com/raidionics/AeroPath#demo) <a target="_blank" href="https://huggingface.co/spaces/andreped/AeroPath"><img src="https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-yellow.svg"></a>

To access the live demo, click on the `Hugging Face` badge above. Below is a snapshot of the current state of the demo app.

<img width="1400" alt="Screenshot 2023-10-31 at 01 34 47" src="https://github.com/raidionics/AeroPath/assets/29090665/bd2db9ff-b188-4f90-aa96-4723b8e7597c">

## [Continuous integration](https://github.com/raidionics/AeroPath#continuous-integration)

| Build Type | Status |
| - | - |
| **HF Deploy** | [![Deploy](https://github.com/raidionics/AeroPath/workflows/Deploy/badge.svg)](https://github.com/raidionics/AeroPath/actions) |
| **File size check** | [![Filesize](https://github.com/raidionics/AeroPath/workflows/Check%20file%20size/badge.svg)](https://github.com/raidionics/AeroPath/actions) |
| **Formatting check** | [![Filesize](https://github.com/raidionics/AeroPath/workflows/Linting/badge.svg)](https://github.com/raidionics/AeroPath/actions) |

## [Development](https://github.com/raidionics/AeroPath#development)

### [Docker](https://github.com/raidionics/AeroPath#docker)

Alternatively, you can deploy the software locally. Note that this is only relevant for development purposes. Simply dockerize the app and run it:

```
docker build -t aeropath .
docker run -it -p 7860:7860 aeropath
```

Then open `http://127.0.0.1:7860` in your favourite internet browser to view the demo.

### [Python](https://github.com/raidionics/AeroPath#python)

It is also possible to run the app locally without Docker. Just setup a virtual environment and run the app.
Note that the current working directory would need to be adjusted based on where `AeroPath` is located on disk.

```
git clone https://github.com/raidionics/AeroPath.git
cd AeroPath/

virtualenv -python3 venv --clear
source venv/bin/activate
pip install -r ./demo/requirements.txt

python demo/app.py --cwd ./
```

## [Citation](https://github.com/raidionics/AeroPath#citation)

If you found the dataset and/or web application relevant in your research, please cite the following reference:
```
@misc{støverud2023aeropath,
  title={{AeroPath: An airway segmentation benchmark dataset with challenging pathology}}, 
  author={Karen-Helene Støverud and David Bouget and Andre Pedersen and Håkon Olav Leira and Thomas Langø and Erlend Fagertun Hofstad},
  year={2023},
  eprint={2311.01138},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```

The dataset is hosted at Zenodo, so you should also cite the following:
```
@dataset{hofstad2023aeropathzenodo,
  title        = {{AeroPath: An airway segmentation benchmark dataset with challenging pathology}},
  author       = {Hofstad, Erlend and Bouget, David and Pedersen, André},
  month        = nov,
  year         = 2023,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.10069289},
  url          = {https://doi.org/10.5281/zenodo.10069289}
}
```

The web application is using the [Raidionics]() backend, thus, also consider citing:
```
@article{bouget2023raidionics,
    title = {Raidionics: an open software for pre-and postoperative central nervous system tumor segmentation and standardized reporting},
    author = {Bouget, David and Alsinan, Demah and Gaitan, Valeria and Holden Helland, Ragnhild and Pedersen, André and Solheim, Ole and Reinertsen, Ingerid},
    year = {2023},
    month = {09},
    pages = {},
    volume = {13},
    journal = {Scientific Reports},
    doi = {10.1038/s41598-023-42048-7},
}
```

## [License](https://github.com/raidionics/AeroPath#license)

The code in this repository is released under [MIT license](https://github.com/raidionics/AeroPath/blob/main/LICENSE.md).
