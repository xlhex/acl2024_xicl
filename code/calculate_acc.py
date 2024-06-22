#!/usr/bin/python
#-*-coding:utf-8 -*-
#Author   : Xuanli He
#Version  : 1.0
from __future__ import print_function

import sys
import re
import json

def main(input_file):

    total = 0
    correct = 0
    with open(input_file) as reader:
        for i, line in enumerate(reader):
            if not line.startswith('{"original_prompt"'): continue
            items = json.loads(line)
            response = items["output"].strip().split("###")[0].strip()
            total += 1
            for line in response.split("\n"):
                line = line.strip()
                if line.startswith("Label:"):
                    print(line.replace("Label: ", ""), items["answer"])
                    if line.replace("Label: ", "") == items["answer"]:
                        correct += 1
                    if items["answer"] == "not entailment":
                        if line.replace("Label: ", "") in ["contradiction", "neutral"]:
                            correct += 1
                    break

    print(correct, total, round(correct/total*100, 2))

if __name__ == "__main__":
    main(sys.argv[1])

