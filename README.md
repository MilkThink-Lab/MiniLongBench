# <img src="figure/logo.png" width="40" height="40"> [ACL 25] MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models

[![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)]()
![GitHub](https://img.shields.io/github/license/gbup-group/DIANet.svg)


This repository is the official codebase of our paper "MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models" 

The proposed MiniLongBench is a low-cost benchmark for evaluating the Long Context Understanding (LCU) capabilities of LLMs, featuring a compact yet diverse test set of only **237 samples** spanning 6 major task categories and 21 distinct tasks.

Through empirical analysis of over 60 LLMs, MiniLongBench reduces the average evaluation cost to only 4.5% of the original while maintaining an average rank correlation coefficient of 0.97 with LongBench results.


## 🎉 News

2025-05 - We released MiniLongBench dataset in [[Baidu Drive]](https://pan.baidu.com/s/1vUq3C5JR3ICo_g8_JXxJ0w?pwd=6erx) [[Google Drive]](https://drive.google.com/drive/folders/1Ps1_VoI1ExI1ZvVbBSCEKBuJGUlTeMmA?usp=sharing) [[Hugging Face]](https://huggingface.co/datasets/linggm/MiniLongBench). 👈🎉Please try it! 

2025-05 - Our paper "MiniLongBench" has been accepted to the main track of ACL! [[Paper]](https://huggingface.co/datasets/linggm/MiniLongBench)👈🎉Please read it! 


## ⚙️ Environment Setup
Create a Python virtual environment and install all the packages listed in the ```requirements.txt```.
```bash
conda create -n MiniLongBench python=3.11
conda activate MiniLongBench
pip install -r requirements.txt
```

To reproduce the construction of MiniLongBench, please install an apapted version of [[py-irt]](https://github.com/linggm3/py-irt).
```bash
pip install poetry
git clone https://github.com/linggm3/py-irt.git
cd py-irt
poetry install
```


## 🧪 Testing on MiniLongBench
### Obtain LLM's output on MiniLongBench
Download MiniLongBench  [[Baidu Drive]](https://pan.baidu.com/s/1vUq3C5JR3ICo_g8_JXxJ0w?pwd=6erx) [[Google Drive]](https://drive.google.com/drive/folders/1Ps1_VoI1ExI1ZvVbBSCEKBuJGUlTeMmA?usp=sharing) [[Hugging Face]](https://huggingface.co/datasets/linggm/MiniLongBench)

Obtain LLM responses on OpenCompass:

* Evaluate the LLM across all 237 test samples in MiniLongBench
* Generate outputs in the format: pred_data/example


### Calculate scores across the all test samples.

To generate and store the evaluation scores on 237 test samples:

```bash
python minilongbench_scorer.py
```


### Calculate scores on MiniLongBench 
There are two evaluation methods for MiniLongBench.

1. Predict the scores of LLMs on the full LongBench benchmark (`eval_new_llm_by_pred.ipynb`):
   - This notebook show how to obtain MiniLongBench socres by predicting the scores of LLMs on the full LongBench benchmark

2. Directly calculate the scores of LLMs on MiniLongBench (`eval_new_llm_directly.ipynb`):
   - This notebook show how to obtain MiniLongBench socres directly



## 🛠️ Reproducing the MiniLongBench 
### Representation Learning
`representation_learning.ipynb` 展示了读取LongBench的评分数据，进行数据预处理，学习LLM和test sample的表征

### Sample Clustering
`sample_clustering.ipynb` 展示了对test sample的表征进行聚类，从而取出簇中心作为代表性测例

### Evaluation
There are two evaluation methods for MiniLongBench.

1. Predict the scores of LLMs on the full LongBench benchmark (`eval_by_pred.ipynb`):
2. Directly calculate the scores of LLMs on MiniLongBench (`eval_directly.ipynb`):




