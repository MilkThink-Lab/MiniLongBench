# <img src="figure/logo.png" width="40" height="40"> MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models

[![Project Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)]()
![GitHub](https://img.shields.io/github/license/gbup-group/DIANet.svg)


This repository is the official codebase of our paper "MiniLongBench: The Low-cost Long Context Understanding Benchmark for Large Language Models" 

The proposed MiniLongBench is a low-cost benchmark for evaluating the Long Context Understanding (LCU) capabilities of LLMs, featuring a compact yet diverse test set of only **237 samples** spanning 6 major task categories and 21 distinct tasks.

Through empirical analysis of over 60 LLMs, MiniLongBench reduces the average evaluation cost to only 4.5% of the original while maintaining an average rank correlation coefficient of 0.97 with LongBench results.


## 🎉 News

2025-05 - We released MiniLongBench dataset in [[Baidu Drive]](https://pan.baidu.com/s/1h2xeM2iEPJmdp9H-ZQpaMA?pwd=m1ce) [[Google Drive]](https://drive.google.com/drive/folders/1LnIk4zKQMjBKX7oFr1-FHUzpsmPISAIQ?usp=sharing) [[Hugging Face]](https://huggingface.co/datasets/linggm/RouterEval). 👈🎉Please try it! 



## ⚙️ Environment Setup
Create a Python virtual environment and install all the packages listed in the ```requirements.txt```.
```bash
conda create -n MiniLongBench python=3.11
conda activate MiniLongBench
pip install -r requirements.txt
```

## 🧪 Testing on MiniLongBench
### Obtain LLM's output on MiniLongBench
### Calculate scores across the 237 test samples.
### Calculate scores on MiniLongBench 

There are two evaluation methods for MiniLongBench.

1. **Predict the scores of LLMs on the full LongBench benchmark (`eval_by_pred.ipynb`):**
   - This notebook show how to obtain MiniLongBench socres by predicting the scores of LLMs on the full LongBench benchmark

2. **Directly calculate the scores of LLMs on MiniLongBench (`eval_directly.ipynb`):**
   - This notebook show how to obtain MiniLongBench socres directly



## 🛠️ Reproducing the MiniLongBench 







