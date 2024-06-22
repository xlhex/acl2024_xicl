# Using Natural Language Explanations to Improve Robustness of In-context Learning

## Descriptions
This repo contains source code and pre-processed corpora for "Using Natural Language Explanations to Improve Robustness of In-context Learning" (accepted to ACL2024)


## Abstract

>Recent studies demonstrated that large language models (LLMs) can excel in many tasks via in-context learning (ICL). However, recent works show that ICL-prompted models tend to produce inaccurate results when presented with adversarial inputs. In this work, we investigate whether augmenting ICL with natural language explanations (NLEs) improves the robustness of LLMs on adversarial datasets covering natural language inference and paraphrasing identification. We prompt LLMs with a small set of human-generated NLEs to produce further NLEs, yielding more accurate results than both a zero-shot-ICL setting and using only human-generated NLEs. Our results on five popular LLMs (GPT3.5-turbo, Llama2, Vicuna, Zephyr, and Mistral) show that our approach yields over 6% improvement over baseline approaches for eight adversarial datasets: HANS, ISCS, NaN, ST, PICD, PISP, ANLI, and PAWS. Furthermore, previous studies have demonstrated that prompt selection strategies significantly enhance ICL on in-distribution test sets. However, our findings reveal that these strategies do not match the efficacy of our approach for robustness evaluations, resulting in an accuracy drop of 8% compared to the proposed approach. 


## Getting started
**Installing the environment**

You can follow these simple steps to set up your environment with conda.

```bash
conda create --prefix envs python=3.10
conda activate ./envs/
pip install -r requirements.txt
```

## Prediction using open models
You can use the following code to reproduce our results for open models (like zephyrs, mistral, etc.):
```bash
cd code

SEED=1000
TASK=ISCS
PROMPT=icl # icl: standard in-context learning; esnli: using NLEs from esnli; xiclfs: using fs-X-ICL (refer to section 3.2); xiclzs: using zs-X-ICL (refer to section 3.2)
bash run_mis.sh 1000 ISCS icl
```


## Citation

```
@article{he2023using,
  title={Using Natural Language Explanations to Improve Robustness of In-context Learning for Natural Language Inference},
  author={He, Xuanli and Wu, Yuxiang and Camburu, Oana-Maria and Minervini, Pasquale and Stenetorp, Pontus},
  journal={arXiv preprint arXiv:2311.07556},
  year={2023}
}
```
