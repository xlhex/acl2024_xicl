#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli He
#Version  : 1.0
from __future__ import print_function

import random
import sys
import json

import torch

from data_utils import *
from utils import *

def main(model_name, train_file, test_file, task, seed):
    model_path = model_libs[model_name]
    tokenizer, model = create_model(model_path, None, 'cuda')

    random.seed(seed)
    torch.random.manual_seed(seed)

    data_loaders = {
         "HANS": HANS,
         "NAN": NAN,
         "ISCS": ISCS,
         "ESNLI": ESNLI,
         "ANLI": ANLI
      }
    
    prompt = load_prompt(train_file)

    total = 0
    correct = 0

    if train_file.endswith("esnli_no.txt") or train_file.endswith("anli_v1.txt"):
        new_token = 10 
    elif train_file.endswith("esnli.txt") or train_file.endswith("anli_v1_reason.txt"):
        new_token = 80
    elif train_file.endswith("chatgpt_from_esnli.txt") or train_file.endswith("anli_v1_chat_anli.txt"):
        new_token = 90
    else:
        new_token = 100

    prompts, answers = read_data(prompt, test_file, data_loaders[task], test_examples=1000 if "anli_v1" not in train_file else 500, binary=False)

    for i, (prompt, answer) in enumerate(zip(prompts, answers)):
        if i < st: continue
        inputs = tokenizer(prompt, return_tensors="pt")
        for key in inputs:
            inputs[key] = inputs[key].cuda()
        max_len = inputs.input_ids.shape[-1] + new_token
        with torch.inference_mode():
            generate_ids = model.generate(**inputs, max_length=max_len, do_sample=False)
        response = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
        prompt_len = len(tokenizer.batch_decode(inputs.input_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0])
        print(json.dumps({"original_prompt": prompt, "answer": answer, "prompt": response[:prompt_len], "output": response[prompt_len:]}))
    

if __name__ == "__main__":

    parser = args()
    # Parse arguments
    args = parser.parse_args()
    
    main(args.model_name, args.train_file, args.test_file, args.task, args.seed)
