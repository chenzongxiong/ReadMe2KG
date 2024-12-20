# UniHD at TSAR-2022 Shared Task: Is Compute All We Need for Lexical Simplification?

This repository contains the modifications made by our team for the (winning) entry in the English shared task category.
We further include modifications made for Spanish and Portuguese, obtaining SotA in those languages as well.

**Find the arXiv version of our paper here: https://arxiv.org/abs/2301.01764**

In case you find these results useful, please consider citing our work in addition to the shared task paper (see below).

```
@article{aumiller-gertz-2023-unihd,
author = {Aumiller, Dennis and Gertz, Michael},
title = {{UniHD at TSAR-2022 Shared Task: Is Compute All We Need for Lexical Simplification?}},
journal = {CoRR},
volume = {abs/2301.01764},
eprinttype = {arXiv},
eprint = {2301.01764},
url = {https://arxiv.org/abs/2301.01764}
}
```


## Setup for Reproduction
To run the results for the respective subsets, you need to provide your own OpenAI API key in a file named `config.py`. A template can be found in `config.py.template`, which already contains the correct variable name and structure.  
Other required packages can be installed with `python3 -m pip install -r requirements.txt` from the main repository folder.

Obtaining predictions from the API should be possible by running `context_predictor.py` for English results, and the `_es.py` and `\_pt.py` files for Spanish and Portuguese predictions, respectively.

Our predictions submitted to the workshop can be found either in the subfolder `en/`, or the fiel `UniHD.zip`. Later additions of the Spanish and Portuguese predictions are in the respective folders `es/` (for Spanish) and `pt/` (Portuguese).  
An exact reproduction of the system outputs may not be possible, as the generation temperature and other, server-side factors, such as the random seed, can potentially lead to differing predictions. In our experience, there is no possibility of fixing a particular prediction to occur with 100% likelihood.
We also do not make any promises that the used prompt templates work with later models. In our experiments, we used the (relatively "outdated" `text-davinci-002` model, which may respond differently to prompt variants than later additions.

# Original README: TSAR-2022-Shared-Task Datasets and Evaluation Scripts
TSAR2022 Shared Task on Lexical Simplification for English (en), Spanish (es) and Portuguese (pt) - Datasets and Evaluation scripts

Please look at the website of the Shared Task for more details about the Evaluation Benchmark, Guidelines, Registration Form, etc...
<br/>[TSAR-2022 Shared-Task website](https://taln.upf.edu/pages/tsar2022-st/)

## Datasets

There is no training dataset for the TSAR-2022 Shared Task. 
However, a sample of 10 or 12 instances with gold standard annotations is provided here as a trial/sample dataset.
<br/> 
<br/> 
Format of the files:
- Format of the *trial_none* and *test_none* files: <span style="font-weight:normal">Sentence&lt;TAB&gt;ComplexWord</span>
- Format of the *trial_gold* and *test_gold* files: <span style="font-weight:normal">Sentence&lt;TAB&gt;ComplexWord&lt;TAB&gt;Annotation1&lt;TAB&gt;Annotation2&lt;TAB&gt;...&lt;TAB&gt;AnnotationN</span>


### Trial dataset
The trial dataset consists of a set of 10 instances (for English and Portuguese) and 12 instances (for Spanish) of a sentence, a target complex word.
The *trial_none* files contain only the instances and the *trial_gold* files contain the instances and set of gold annotations.

- /datasets/trial/tsar2022_en_trial_none.tsv
- /datasets/trial/tsar2022_en_trial_gold.tsv
- /datasets/trial/tsar2022_es_trial_none.tsv
- /datasets/trial/tsar2022_es_trial_gold.tsv
- /datasets/trial/tsar2022_pt_trial_none.tsv
- /datasets/trial/tsar2022_pt_trial_gold.tsv

<br/>



### Test dataset 

The *test_none* files (used for the evaluation benchmark) contain the instances with the sentences and target complex words.

- English test_none dataset (373 instances)<br/> 
/datasets/test/tsar2022_en_test_none.tsv  

- Spanish test_none dataset (368 instances)<br/> 
/datasets/test/tsar2022_es_test_none.tsv  

- Portuguese test_none dataset (374 instances)<br/> 
/datasets/test/tsar2022_pt_test_none.tsv

The *test_gold* files contain the sentences, target complex words, and gold annotations<br/> 

- English test_gold dataset (373 instances)<br/> 
/datasets/test/tsar2022_en_test_gold.tsv  

- Spanish test_gold dataset (368 instances)<br/> 
/datasets/test/tsar2022_es_test_gold.tsv  

- Portuguese test_gold dataset (374 instances)<br/> 
/datasets/test/tsar2022_pt_test_gold.tsv


## Results of the Evaluation Benchmark

The official results for each language (en, es, and pt) can be found in this directory:<br/> 
/results/official

The following 10 metrics are reported in the official results:
-  MAP@1/Potential@1/Precision@1
-  MAP@3
-  MAP@5
-  MAP@10
-  Potential@3
-  Potential@5
-  Potential@10
-  Accuracy@1@top_gold_1
-  Accuracy@2@top_gold_1
-  Accuracy@3@top_gold_1 


The extended results for each language (en, es, and pt) can be found in this directory:<br/> 
/results/extended<br/> 

The following metrics are reported in the extended results:
-  Potential@K  K={1..10} 
-  MAP@K  K={1..10}
-  Precision@K  K={1..10}  (macro-average)
-  Recall@K  K={1..10}     (macro-average)
-  Accuracy@K@top_gold_1   K={1..10} 



## Evaluation Scripts 

### tsar_eval.py

This script evaluates the following metric:

    -  MAP@1/Potential@1/Precision@1
    -  MAP@3
    -  MAP@5
    -  MAP@10
    -  Potential@3
    -  Potential@5
    -  Potential@10
    -  Accuracy@1@top_gold_1
    -  Accuracy@2@top_gold_1
    -  Accuracy@3@top_gold_1  
      
Script options and help

```console
Evaluation Script for the TSAR-2022 Lexical Simplification Shared Task

Usage: tsar_eval.py <options>

Options:
  -h, --help            show this help message and exit
  --gold_file=<PATH>    The path to the file with the gold annotated instances
  --predictions_file=<PATH>
                        The path to file with the predictions
  --output_file=<PATH>  path to the output file
  --verbose             Verbose output mode
```


usage example

```console
python3 ./tsar_eval.py --gold_file ./gold/tsar_es_gold.tsv --predictions_file ./predicted/TEAMNAME_TRACKNAME_RUNNAME.tsv  --output_file ./results/TEAMNAME_TRACKNAME_RUNNAME.tsv.eval
```

## Dataset Compilation and Baselines

A paper describing the compilation of the datasets for English, Portuguese and Spanish that includes several experiments with 
two state-of-the-art approaches for Lexical Simplification has been published at this link:
https://www.frontiersin.org/articles/10.3389/frai.2022.991242

[Lexical Simplification Benchmarks for English, Portuguese, and Spanish](https://www.frontiersin.org/articles/10.3389/frai.2022.991242).<br/>
Sanja Štajner, Daniel Ferrés, Matthew Shardlow, Kai North, Marcos Zampieri and  Horacio Saggion.<br/>
Front. Artif. Intell. Sec. Natural Language Processing. <br/>
doi: 10.3389/frai.2022.991242

Preprint available at ArXiV: [https://arxiv.org/abs/2209.05301](https://arxiv.org/abs/2209.05301)


## License

The python scripts follow [AGPL 3.0v license](LICENSE).
The datasets (under the /datasets directory) are licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License [CC-BY-NC-SA-4.0](CC-BY-NC-SA-4.0).

## Contact
https://taln.upf.edu/pages/tsar2022-st/#contact


