#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli He
#Version  : 1.0
#Filename : data_utils.py
from __future__ import print_function

import random
import json
import string

meta_dict = {
     "SST-2": {0: "negative", 1: "positive"},
     "QQP": {0: "no", 1: "yes"},
     "MNLI": {0: "entailment", 1: "not entailment"},
     "QNLI": {0: "yes", 1: "no"},
     "RTE": {0: "yes", 1: "no"},
     "MRPC": {"0": "No", "1": "Yes"},
     "HANS": {0: "entailment", 1: "not entailment"},
     "NAN": {"entailment": "entailment", "contradiction": "not entailment", "neutral": "not entailment"},
     "ISCS": {0: "entailment", 1: "not entailment", 2: "not entailment"},
     "ESNLI": {0: "entailment", 1: "not entailment", 2: "not entailment"},
     "ANLI": {"e": "entailment", "c": "not entailment", "n": "not entailment"},
  }

meta_dict = {
     "SST-2": {0: "negative", 1: "positive"},
     "QQP": {0: "no", 1: "yes"},
     "MNLI": {0: "entailment", 1: "not entailment"},
     "QNLI": {0: "yes", 1: "no"},
     "RTE": {0: "yes", 1: "no"},
     "MRPC": {"0": "No", "1": "Yes"},
     "HANS": {0: "entailment", 1: "not entailment"},
     "NAN": {"entailment": "entailment", "contradiction": "contradiction", "neutral": "neutral"},
     "ISCS": {0: "entailment", 1: "neutral", 2: "contradiction"},
     "ESNLI": {0: "entailment", 1: "neutral", 2: "contradiction"},
     "ANLI": {"e": "entailment", "c": "contradiction", "n": "neutral"},
  }


def NAN(inst):

    prompt = "Premise: {}\nHypothesis: {}".format(
           inst["premise"].strip(),
           inst["hypothesis"].strip()
           + ("" if inst["hypothesis"].strip()[-1] in string.punctuation else ".")
       )
    return prompt, meta_dict["NAN"][inst["label"]]


def HANS(inst):

    prompt = "Premise: {}\nHypothesis: {}".format(
           inst["premise"].strip(),
           inst["hypothesis"].strip()
           + ("" if inst["hypothesis"].strip()[-1] in string.punctuation else ".")
       )
    return prompt, meta_dict["HANS"][inst["label"]]


def ESNLI(inst):

    prompt = "Premise: {}\nHypothesis: {}".format(
           inst["premise"].strip(),
           inst["hypothesis"].strip()
           + ("" if inst["hypothesis"].strip()[-1] in string.punctuation else ".")
       )
    return prompt, meta_dict["ESNLI"][inst["label"]]


def ISCS(inst):

    prompt = "Premise: {}\nHypothesis: {}".format(
           inst["prem"].strip(),
           inst["hypo"].strip()
           + ("" if inst["hypo"].strip()[-1] in string.punctuation else ".")
       )
    return prompt, meta_dict["ISCS"][inst["label"]]

def ANLI(inst):

    prompt = "Premise: {}\nHypothesis: {}".format(
           inst["context"].strip(),
           inst["hypothesis"].strip()
           + ("" if inst["hypothesis"].strip()[-1] in string.punctuation else ".")
       )
    return prompt, meta_dict["ANLI"][inst["label"]]


def load_prompt(input_file):
    with open(input_file) as reader:
        prompt = reader.read().strip()

    return prompt + "\n###"


def read_data(prompt, test_file, data_loader, test_examples=None, binary=False):
    test_data = []
    with open(test_file) as f:
        for line in f:
            inst = json.loads(line.strip())
            test_data.append(inst)

    prompts, answers = [], []
    test_examples = test_examples if test_examples else 100
    if test_examples > len(test_data):
        test_examples = len(test_data)

    processed = 0

    for test in random.sample(test_data, test_examples)[processed:]:
        test_doc, answer = data_loader(test)
        prompts.append(prompt + "\n" + test_doc)
        answers.append(answer)

    return prompts, answers
