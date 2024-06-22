#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli He
#Version  : 1.0
#Filename : utils.py
from __future__ import print_function

from typing import Tuple, Optional, Any, List
import argparse

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


model_libs = {
    "mistral": "mistralai/Mistral-7B-Instruct-v0.1",
    "zephyr": "HuggingFaceH4/zephyr-7b-alpha",
    "llama3-8B": "meta-llama/Meta-Llama-3-8B",
 }

def create_model(model_name: str, peft_model_name: Optional[str], device: str,
                  do_compile: bool = True, dtype: torch.dtype = torch.bfloat16) -> Tuple[Any, Any]:

    model_kwargs = {}
    peft_kwargs = {}

    if device == "cuda":
        model_kwargs['torch_dtype'] = peft_kwargs['torch_dtype'] = dtype
        model_kwargs['device_map'] = peft_kwargs['device_map'] = 'balanced_low_0'  # 'auto'
    else:
        model_kwargs['low_cpu_mem_usage'] = True

    tokenizer = AutoTokenizer.from_pretrained(model_name, resume_download=True, padding_side="left")
    tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(model_name, resume_download=True, trust_remote_code=True, **model_kwargs)

    if do_compile is True:
        model = torch.compile(model)

    model.eval()

    return tokenizer, model

def args():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--model_name",
        type=str,
        choices=list(model_libs.keys())
    )

    parser.add_argument(
        "--train_file",
        type=str,
        help="In-context demonstration examples",
        required=True,
    )

    parser.add_argument(
        "--test_file",
        type=str,
        help="test file for the evaluation",
        required=True,
    )

    parser.add_argument(
        "--task",
        type=str,
        choices=["HANS", "NAN", "ISCS", "ESNLI", "ANLI"],
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=1000,
        help="random seed",
    )

    return parser
