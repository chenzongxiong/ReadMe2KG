# Vakyansh Open Source Models


1. [ Pretrained ASR Models ](#pretrained-asr-models)
2. [ Finetuned ASR Models ](#finetuned-asr-models)
3. [ Language Models ](#language-models)
4. [ Punctuation Models ](#punctuation-models)
5. [ TTS Models ](#tts-models)
6. [ Gender Classification Model ](#gender-classification-model)
7. [ Language Identification Models ](#language-identification-models)
8. [ Interspeech 2021 ASR Models ](#interspeech-2021-asr-models)


<a name="pam"></a>
## Pretrained ASR Models

**[wav2vec2-code](https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation)** | **[nemo-code](https://github.com/Open-Speech-EkStep/vakyansh-nemo-experimentation)** 

| Pretrained Model | Description | Architecture | Hours |
|------------------|----------|----|---------|
| [Vakyansh-Conformer-SSL](https://storage.googleapis.com/vakyansh-open-models/pretrained_models/vakyansh-conformer-ssl/ssl_conformer_large_e178.nemo) | This model was pre-trained using Nemo toolkit  with 34,000 hours unlabeled audio in 39 Indian languages. This includes 15,000 hours of news recordings available on the internet, 10,000 hours of YouTube audios and other audio data. In addition, 9,000 hours of Indian English audio data was taken from NPTEL lectures open sourced by AI4Bharat. <br> This model was trained in collaboration with NVIDIA (NVIDIA Graphics Pvt Ltd). We thank NVIDIA for providing the compute resources to train this model. | Conformer-Large | 34,000 |
| [CLSRIL-23](https://storage.googleapis.com/vakyansh-open-models/pretrained_models/clsril-23/CLSRIL-23.pt) | Cross Lingual Speech Representations for Indic Languages, Contains 10,000 hours of training data from 23 Indic Languages. <br> [Citation: https://arxiv.org/abs/2107.07402 ](https://arxiv.org/abs/2107.07402 ) | wav2vec2-Base | 10,000               | 
| [hindi_pretrained_4kh](https://storage.googleapis.com/vakyansh-open-models/pretrained_models/hindi/hindi_pretrained_4kh.pt) | Trained on 4200 hours of Hindi Data| wav2vec2-Base |  4,200             |  
| [kannada_pretrained_1400h](https://storage.googleapis.com/vakyansh-open-models/pretrained_models/kannada/kannada_pretrained_1400h.pt) | Trained on 1400 hours of Kannada data| wav2vec2-XLSR | 1,400             | 



<br><br>

<a name="fam"></a>

## Finetuned ASR Models

### Conformer based models
**[Repo](https://github.com/Open-Speech-EkStep/vakyansh-nemo-experimentation)**

| Language | Pretrained Model | Finetuned Model | Finetuned Hours | Arch |
|----|--------|----|-----|---|
| Hindi | Vakyansh Conformer SSL | [hindi_large_ssl_2500](https://storage.googleapis.com/vakyansh-open-models/conformer_models/hindi/filtered_v1_ssl_2022-07-08_19-43-25/Conformer-CTC-BPE-Large.nemo) | 2,500 h | Large |
| Indian English | Vakyansh Conformer SSL | [indian_en_large_ssl_700](https://storage.googleapis.com/vakyansh-open-models/conformer_models/english/2022-09-13_15-50-48/Conformer-CTC-BPE-Large.nemo) | 700 h | Large |
| Kannada | Vakyansh Conformer SSL | [kannada_large_ssl_1000](https://storage.googleapis.com/vakyansh-open-models/conformer_models/kannada/iisc_noa_2022-08-30_22-45-15/Conformer-CTC-BPE-Large.nemo) | 1,000 h | Large |
| Punjabi | Vakyansh Conformer SSL | [punjabi_large_ssl_500](https://storage.googleapis.com/vakyansh-open-models/conformer_models/punjabi/sme_noa_2022-08-23_19-56-08/Conformer-CTC-BPE-Large.nemo) | 500 h | Large |
| Tamil | Vakyansh Conformer SSL | [tamil_large_ssl_900](https://storage.googleapis.com/vakyansh-open-models/conformer_models/tamil/iisc_noa_2022-09-03_14-06-50/Conformer-CTC-BPE-Large.nemo) | 900 h | Large |

<br><hr>
### wav2vec2 based models

**[Repo](https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation)**

**Citation:** https://arxiv.org/abs/2203.16512 

| Language | Pretrained Model | Finetuned Model | Dictionary | Single Model for Inference | Finetuned Hours | TS model |
|----|--------|----|-----|-------------------|-------|---|
| Hindi | CLSRIL-23 | [him_4200](https://storage.googleapis.com/vakyansh-open-models/models/hindi/hi-IN/him_4200.pt ) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/hindi/hi-IN/dict.ltr.txt ) | [hindi_infer](https://storage.googleapis.com/vakyansh-open-models/models/hindi/hi-IN/hindi_infer.pt) | 4200 h | [hindi_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/hindi.zip)
| Indian English | CLSRIL-23 | [enm_700](https://storage.googleapis.com/vakyansh-open-models/models/english/en-IN/enm_700.pt ) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/english/en-IN/dict.ltr.txt) | [english_infer]( https://storage.googleapis.com/vakyansh-open-models/models/english/en-IN/english_infer.pt ) | 700 h | [english_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/english.zip)
| Kannada | CLSRIL-23 | [knm_560](https://storage.googleapis.com/vakyansh-open-models/models/kannada/kn-IN/knm_560.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/kannada/kn-IN/dict.ltr.txt) | [kannada_infer](https://storage.googleapis.com/vakyansh-open-models/models/kannada/kn-IN/kannada_infer.pt ) | 560 h | [kannada_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/kannada.zip)
| Tamil | CLSRIL-23 | [tam_250](https://storage.googleapis.com/vakyansh-open-models/models/tamil/ta-IN/tam_250.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/tamil/ta-IN/dict.ltr.txt) | [tamil_infer](https://storage.googleapis.com/vakyansh-open-models/models/tamil/ta-IN/tamil_infer.pt ) | 250 h |  [tamil_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/tamil.zip)
| Bengali | CLSRIL-23 | [bnm_200](https://storage.googleapis.com/vakyansh-open-models/models/bengali/bn-IN/bnm_200.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/bengali/bn-IN/dict.ltr.txt) | [bengali_infer](https://storage.googleapis.com/vakyansh-open-models/models/bengali/bn-IN/bengali_infer.pt ) | 200 h | [bengali_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/bengali.zip) |
| Nepali | CLSRIL-23 | [nem_130](https://storage.googleapis.com/vakyansh-open-models/models/nepali/ne-IN/nem_130.pt ) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/nepali/ne-IN/dict.ltr.txt) | [nepali_infer]( https://storage.googleapis.com/vakyansh-open-models/models/nepali/ne-IN/nepali_infer.pt ) | 130 h | [nepali_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/nepali.zip)
| Telugu | CLSRIL-23 | [tem_100](https://storage.googleapis.com/vakyansh-open-models/models/telugu/te-IN/tem_100.pt ) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/telugu/te-IN/dict.ltr.txt ) | [telugu_infer](https://storage.googleapis.com/vakyansh-open-models/models/telugu/te-IN/telugu_infer.pt ) | 100 h | [telugu_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/telugu.zip)
| Gujarati | CLSRIL-23 | [gum_100](https://storage.googleapis.com/vakyansh-open-models/models/gujarati/gu-IN/gum_100.pt ) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/gujarati/gu-IN/dict.ltr.txt ) | [gujarati_infer](https://storage.googleapis.com/vakyansh-open-models/models/gujarati/gu-IN/gujarati_infer.pt ) | 100 h | [gujarati_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/gujarati.zip)
| Marathi | CLSRIL-23 | [mrm_100](https://storage.googleapis.com/vakyansh-open-models/models/marathi/mr-IN/mrm_100.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/marathi/mr-IN/dict.ltr.txt) |  [marathi_infer](https://storage.googleapis.com/vakyansh-open-models/models/marathi/mr-IN/marathi_infer.pt) | 100 h | [marathi_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/marathi.zip)
| Odia | CLSRIL-23 | [orm_100](https://storage.googleapis.com/vakyansh-open-models/models/odia/or-IN/orm_100.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/odia/or-IN/dict.ltr.txt) | [odia_infer](https://storage.googleapis.com/vakyansh-open-models/models/odia/or-IN/odia_infer.pt) | 100 h | [odia_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/odia.zip)
| Sanskrit | CLSRIL-23 | [sam_60](https://storage.googleapis.com/vakyansh-open-models/models/sanskrit/sa-IN/sam_60.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/sanskrit/sa-IN/dict.ltr.txt) | [sanskrit_infer](https://storage.googleapis.com/vakyansh-open-models/models/sanskrit/sa-IN/sanskrit_infer.pt) | 60 h | [sanskrit_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/sanskrit.zip)
| Maithili | CLSRIL-23 | [maim_50](https://storage.googleapis.com/vakyansh-open-models/models/maithili/mai-IN/maim_50h.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/maithili/mai-IN/dict.ltr.txt) | [maithili_infer](https://storage.googleapis.com/vakyansh-open-models/models/maithili/mai-IN/maithili_infer.pt) | 50 h | [maithili_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/maithili.zip)
| Urdu | CLSRIL-23 | [urm_60h](https://storage.googleapis.com/vakyansh-open-models/models/urdu/ur-IN/urm_60h.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/urdu/ur-IN/dict.ltr.txt) | [urdu_infer](https://storage.googleapis.com/vakyansh-open-models/models/urdu/ur-IN/urm_infer.pt) | 60h | [urdu_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/urdu.zip)
| Punjabi | CLSRIL-23 | [pam_10h](https://storage.googleapis.com/vakyansh-open-models/models/punjabi/pa-IN/pam_10h.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/punjabi/pa-IN/dict.ltr.txt) | [punjabi_infer](https://storage.googleapis.com/vakyansh-open-models/models/punjabi/pa-IN/punjabi_infer.pt) |  10 h | [punjabi_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/punjabi.zip)
| Dogri | CLSRIL-23 | [doi_55h](https://storage.googleapis.com/vakyansh-open-models/models/dogri/doi-IN/doim_55h.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/dogri/doi-IN/dict.ltr.txt) | [dogri_infer](https://storage.googleapis.com/vakyansh-open-models/models/dogri/doi-IN/dogri_infer.pt) | 55 h | [dogri_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/dogri.zip)
| Malayalam | CLSRIL-23 | [mlm_8h](https://storage.googleapis.com/vakyansh-open-models/models/malayalam/ml-IN/mlm_8h.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/malayalam/ml-IN/dict.ltr.txt) | [malayalam_infer](https://storage.googleapis.com/vakyansh-open-models/models/malayalam/ml-IN/malayalam_infer.pt) | 8 h | [malayalam_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/malayalam.zip)
| Bhojpuri | CLSRIL-23 | [bhom_60h](https://storage.googleapis.com/vakyansh-open-models/models/bhojpuri/bho-IN/bhom_60h.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/bhojpuri/bho-IN/dict.ltr.txt) | [bhojpuri_infer](https://storage.googleapis.com/vakyansh-open-models/models/bhojpuri/bho-IN/bhojpuri_infer.pt) | 60 h | [bhojpuri_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/bhojpuri.zip)
| Assamese | CLSRIL-23 | [asm_8h](https://storage.googleapis.com/vakyansh-open-models/models/assamese/asm_8.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/models/assamese/dict.ltr.txt) | [assamese_infer](https://storage.googleapis.com/vakyansh-open-models/models/assamese/assamese_infer.pt) | 8 h | [assamese_ts](https://storage.googleapis.com/vakyansh-open-models/torchscript_models/assamese.zip)

<br><br>


<a name="lm"></a>

## Language Models

**[Repo](https://github.com/Open-Speech-EkStep/vakyansh-wav2vec2-experimentation)**

Language models  integrate with finetuned models. 

| Language | Type | Lexicon | LM | Text Corpus | 
|----|--------|---------|------|------|
| Hindi | kenlm 5-gram | [hindi_lexicon]( https://storage.googleapis.com/vakyansh-open-models/models/hindi/hi-IN/lexicon.lst ) | [hindi_lm](https://storage.googleapis.com/vakyansh-open-models/models/hindi/hi-IN/lm.binary) | [hindi_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/hindi.zip)
| Indian English | kenlm 5-gram | [english_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/english/en-IN/lexicon.lst ) | [english_lm](https://storage.googleapis.com/vakyansh-open-models/models/english/en-IN/lm.binary) | [english_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/english.zip)
| Kannada | kenlm 5-gram | [kannada_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/kannada/kn-IN/lexicon.lst) | [kannada_lm](https://storage.googleapis.com/vakyansh-open-models/models/kannada/kn-IN/lm.binary ) | [kannada_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/kannada.zip)
| Tamil | kenlm 5-gram | [tamil_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/tamil/ta-IN/lexicon.lst) | [tamil_lm](https://storage.googleapis.com/vakyansh-open-models/models/tamil/ta-IN/lm.binary) | [tamil_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/tamil.zip)
| Bengali | kenlm 5-gram | [bengali_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/bengali/bn-IN/lexicon.lst) | [bengali_lm](https://storage.googleapis.com/vakyansh-open-models/models/bengali/bn-IN/lm.binary ) | [bengali_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/bengali.zip)
| Nepali | kenlm 5-gram | [nepali_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/nepali/ne-IN/lexicon.lst ) | [nepali_lm](https://storage.googleapis.com/vakyansh-open-models/models/nepali/ne-IN/lm.binary ) | [nepali_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/nepali.zip)
| Telugu | kenlm 5-gram | [telugu_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/telugu/te-IN/lexicon.lst) | [telugu_lm](https://storage.googleapis.com/vakyansh-open-models/models/telugu/te-IN/lm.binary) | [telugu_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/telugu.zip)
| Gujarati | kenlm 5-gram | [gujarati_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/gujarati/gu-IN/lexicon.lst ) | [gujarati_lm](https://storage.googleapis.com/vakyansh-open-models/models/gujarati/gu-IN/lm.binary) | [gujarati_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/gujarati.zip)
| Marathi | kenlm 5-gram | [marathi_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/marathi/mr-IN/lexicon.lst) | [marathi_lm](https://storage.googleapis.com/vakyansh-open-models/models/marathi/mr-IN/lm.binary) | [marathi_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/marathi.zip)
| Odia | kenlm 5-gram | [odia_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/odia/or-IN/lexicon.lst) | [odia_lm](https://storage.googleapis.com/vakyansh-open-models/models/odia/or-IN/lm.binary) | [odia_lm](https://storage.googleapis.com/vakyansh-open-models/language_model_text/odia.zip)
| Sanskrit | kenlm 5-gram | [sanskrit_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/sanskrit/sa-IN/lexicon.lst) | [sanskrit_lm](https://storage.googleapis.com/vakyansh-open-models/models/sanskrit/sa-IN/lm.binary) | [sanskrit_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/sanskrit.zip)
| Maithili | kenlm 5-gram | [maithili_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/maithili/mai-IN/lexicon.lst) | [maithili_lm](https://storage.googleapis.com/vakyansh-open-models/models/maithili/mai-IN/lm.binary) | [maithili_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/maithili.zip)
| Urdu | kenlm 5-gram | [urdu_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/urdu/ur-IN/lexicon.lst) | [urdu_lm](https://storage.googleapis.com/vakyansh-open-models/models/urdu/ur-IN/lm.binary) | [urdu_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/urdu.zip)
| Punjabi | kenlm 5-gram | [punjabi_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/punjabi/pa-IN/lexicon.lst) | [punjabi_lm](https://storage.googleapis.com/vakyansh-open-models/models/punjabi/pa-IN/lm.binary) | [punjabi_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/punjabi.zip)
| Dogri | kenlm 5-gram | [dogri_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/dogri/doi-IN/lexicon.lst) | [dogri_lm](https://storage.googleapis.com/vakyansh-open-models/models/dogri/doi-IN/lm.binary) | [dogri_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/dogri.zip)
| Malayalam | kenlm 5-gram | [malayalam_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/malayalam/ml-IN/lexicon.lst) | [malayalam_lm](https://storage.googleapis.com/vakyansh-open-models/models/malayalam/ml-IN/lm.binary) | [malayalam_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/malayalam.zip)
| Bhojpuri | kenlm 5-gram | [bhojpuri_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/bhojpuri/bho-IN/lexicon.lst) | [bhojpuri_lm](https://storage.googleapis.com/vakyansh-open-models/models/bhojpuri/bho-IN/lm.binary) | [bhojpuri_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/bhojpuri.zip)
| Rajasthani | kenlm 5-gram | [rajasthani_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/rajasthani/raj-IN/lexicon.lst) | [rajasthani_lm](https://storage.googleapis.com/vakyansh-open-models/models/rajasthani/raj-IN/lm.binary) | [rajasthani_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/rajasthani.zip)
| Assamese | kenlm 5-gram | [assamese_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/assamese/lexicon.lst) | [assamese_lm](https://storage.googleapis.com/vakyansh-open-models/models/assamese/lm.binary) | [assamese_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/assamese.zip)
| Hinglish | kenlm 5-gram | [hinglish_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/hinglish/lexicon.lst) | [hinglish_lm](https://storage.googleapis.com/vakyansh-open-models/models/hinglish/lm.binary) | [hinglish_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/hinglish.zip)


**Dataset Credits: We thanks AI4Bharat for open sourcing the Indic-Corp dataset. [Link](https://indicnlp.ai4bharat.org/corpora/)**. We modified the original data by tokenizing and removing duplicates.


### Domain Specific Language Models
| Language | Type | Domain | Lexicon | LM | Text Corpus | 
|----|--------|---------|------|---|------|
| English | kenlm 5-gram | Biomedical | [bio_lexicon](https://storage.googleapis.com/vakyansh-open-models/models/english/bio-lm/lexicon.lst ) | [bio_lm](https://storage.googleapis.com/vakyansh-open-models/models/english/bio-lm/lm.binary) | [bio_lm_eng_text](https://storage.googleapis.com/vakyansh-open-models/language_model_text/biomedical_data_english.zip)

<br><br>

<a name="pm"></a>
## Punctuation Models

**[Training Repo](https://github.com/Open-Speech-EkStep/punctuation-ITN/tree/wandb-v1/sequence_labelling)**

**[Inference Repo](https://github.com/Open-Speech-EkStep/indic-punct)**

| Language | Model | Data | 
|----------|-------|-------|
| Hindi | [hi.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/hi.zip)| [hindi_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/hindi_new.zip)|
| Assamese | [as.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/as.zip)| [assamese_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/assamese.zip) |
| Bengali | [bn.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/bn.zip)| [bengali_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/bengali.zip)|
| Gujarati | [gu.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/gu.zip)| [gujarati_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/gujarati.zip)|
| Kannada | [kn.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/kn.zip)| [kannada_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/kannada.zip)|
| Malayalam | [ml.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/ml.zip)| [malayalam_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/malayalam.zip)|
| Marathi | [mr.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/mr.zip)| [marathi_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/marathi.zip)|
| Odia | [or.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/or.zip)| [odia_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/oria.zip)|
| Punjabi | [pa.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/pa.zip)| [punjabi_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/punjabi.zip)|
| Tamil | [ta.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/ta.zip)| [tamil_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/tamil.zip)|
| Telugu | [te.zip](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/te.zip)| [telugu_data](https://storage.googleapis.com/vakyansh-open-models/punctuation_models/training_data/telugu.zip)|


**Dataset Credits: We thank AI4Bharat for open sourcing the Indic-Corp dataset. [Link](https://indicnlp.ai4bharat.org/corpora/)**. We modified the original data by tokenizing and removing duplicates.

<br><br>

<a name="tts"></a>
## TTS Models 
Below models are trained using [Glow TTS](https://github.com/jaywalnut310/glow-tts) and [hifi GAN](https://github.com/jik876/hifi-gan) combination. 

**[Repo](https://github.com/Open-Speech-EkStep/vakyansh-tts)**

| Language | Language Code | Gender | glow ckpt | hifi-gan ckpt | 
| ------- | --- | -- | ---- | ------------ |
| Hindi | hi |Female | [hi_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/glow.zip) | [hi_0_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/hifi.zip) |
| Hindi | hi | Male | [hi_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/male_voice_1/glow.zip) | [hi_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/male_voice_1/hifi.zip) |
| Kannada | kn | Female | [kn_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/kannada/kn-IN/female_voice_0/fe_glow.zip) | [kn_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/kannada/kn-IN/ma_fe_hifi/ma_fe_hifi.zip) |
| Kannada | kn | Male | [kn_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/kannada/kn-IN/male_voice_1/ma_glow.zip) | [kn_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/kannada/kn-IN/ma_fe_hifi/ma_fe_hifi.zip)  |
| Tamil | ta |Female | [ta_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/tamil/ta-IN/female_voice_0/glow.zip) | [ta_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/tamil/ta-IN/ma_fe_hifi/hifi.zip) |
| Tamil | ta |Male | [ta_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/tamil/ta-IN/male_voice_1/glow.zip) | [ta_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/tamil/ta-IN/ma_fe_hifi/hifi.zip)  |
| Telugu | te | Female | [te_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/telugu/te-IN/female_voice_0/glow.zip) | [te_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/telugu/te-IN/ma_fe_hifi/hifi.zip) |
| Telugu | te | Male | [te_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/telugu/te-IN/male_voice_1/glow.zip) | [te_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/telugu/te-IN/ma_fe_hifi/hifi.zip)  |
| Odia | or | Female | [or_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/odia/or-IN/female_voice_0/glow.zip) | [or_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/odia/or-IN/ma_fe_hifi/hifi.zip) |
| Odia | or | Male | [or_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/odia/or-IN/male_voice_1/glow.zip) | [or_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/odia/or-IN/ma_fe_hifi/hifi.zip)  |
| Malayalam | ml | Female | [ml_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/malayalam/ml-IN/female_voice_0/glow.zip) | [ml_0_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/malayalam/ml-IN/female_voice_0/hifi.zip) |
| Malayalam | ml | Male | [ml_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/malayalam/ml-IN/male_voice_1/glow.zip) | [ml_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/malayalam/ml-IN/male_voice_1/hifi.zip) |
| Marathi | mr | Female | [mr_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/marathi/mr-IN/female_voice_0/glow.zip) | [mr_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/marathi/mr-IN/female_voice_0/hifi.zip) |
| Gujarati | gu | Male | [gu_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/gujarati/gu-IN/male_voice_1/glow.zip) | [gu_0_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/gujarati/gu-IN/male_voice_1/hifi.zip) |
| Bengali | bn | Female | [bn_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/bengali/bn-IN/female_voice_0/glow.zip) | [bn_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/bengali/bn-IN/female_voice_0/hifi.zip) |
| Bengali | bn | Male | [bn_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/bengali/bn-IN/male_voice_1/glow.zip) | [bn_0_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/bengali/bn-IN/male_voice_1/hifi.zip) |
| English | en | Female | [en_0_glow](https://storage.googleapis.com/vakyansh-open-models/tts/english/en-IN/female_voice_0/glow.zip) | [en_0_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/female_voice_0/hifi.zip) |
| English | en | Male | [en_1_glow](https://storage.googleapis.com/vakyansh-open-models/tts/english/en-IN/male_voice_1/glow.zip) | [en_1_hifi](https://storage.googleapis.com/vakyansh-open-models/tts/hindi/hi-IN/male_voice_1/hifi.zip) |


**Dataset Credits: We thanks IITM for open sourcing Indic-TTS dataset. [Link](https://www.iitm.ac.in/donlab/tts/database.php)**

<br><br>


<a name="gcm"></a>
## Gender Classification Model
**[Repo](https://github.com/Open-Speech-EkStep/ekstep-gender-classification)**

| Type | Model Type | Model | 
|----------|----|---|
|  Gender Classification | SVC | [Model](https://storage.googleapis.com/vakyansh-open-models/gender_classification/model/clf_svc.sav) |

<br><br>
<a name="lim"></a>
## Language Identification Models
**[Repo](https://github.com/Open-Speech-EkStep/ekstep-language-identification)**

| Type | Model | 
|----------|-------|
|  Hindi_vs_Others |[Model](https://storage.googleapis.com/vakyansh-open-models/language_identification/Hindi_vs_Other/hindi_vs_others.pt) |
|  Tamil_vs_Others |[Model](https://storage.googleapis.com/vakyansh-open-models/language_identification/Tamil_vs_Other/tamil_vs_others.pt) |

<br><br>

<a name="iam"></a>
## Interspeech 2021 ASR Models

[Comp Link](https://navana-tech.github.io/MUCS2021/)

| Language | Pretrained Model | Finetuned Model | Dictionary | Single Model for Inference |
|----|--------|----|-----|-------------------|
| Telugu | CLSRIL-23 | [te_40h_interspeech ](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/telugu/te-IN/te_40h_interspeech.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/telugu/te-IN/dict.ltr.txt ) | [telugu_infer_interspeech](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/telugu/te-IN/telugu_infer_interspeech.pt) | 
| Tamil | CLSRIL-23 | [ta_40h_interspeech ](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/tamil/ta-IN/ta_40h_interspeech.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/tamil/ta-IN/dict.ltr.txt) | [tamil_infer_interspeech](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/tamil/ta-IN/tamil_infer_interspeech.pt) | 
| Gujarati | CLSRIL-23 | [gu_40h_interspeech ](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/gujarati/gu-IN/gu_40h_interspeech.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/gujarati/gu-IN/dict.ltr.txt) | [gujarati_infer_interspeech](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/gujarati/gu-IN/gujarati_infer_interspeech.pt) | 
| Hinglish | CLSRIL-23 | [hinglish_interspeech](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/hinglish/hinglish_interspeech.pt) | [dict](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/hinglish/dict.ltr.txt) | [hinglish_infer_interspeech](https://storage.googleapis.com/vakyansh-open-models/interspeech_models/hinglish/hinglish_infer_interspeech.pt) | 



<br><br>

## Citation 


If you use any of our resources, please cite the following article:
```
@misc{chadha2022vakyansh,
    title={Vakyansh: ASR Toolkit for Low Resource Indic languages},
    author={Harveen Singh Chadha and Anirudh Gupta and Priyanshi Shah and Neeraj Chhimwal and Ankur Dhuriya and Rishabh Gaur and Vivek Raghavan},
    year={2022},
    eprint={2203.16512},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}

```

If you use the pretrained model (CLSRIL-23) please cite the following article:
```
@misc{gupta2021clsril23,
      title={CLSRIL-23: Cross Lingual Speech Representations for Indic Languages}, 
      author={Anirudh Gupta and Harveen Singh Chadha and Priyanshi Shah and Neeraj Chimmwal and Ankur Dhuriya and Rishabh Gaur and Vivek Raghavan},
      year={2021},
      eprint={2107.07402},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

<hr>

