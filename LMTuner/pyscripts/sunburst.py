#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:30:02 2019

Style reference: 
    CoQA: A Conversational Question Answering Challenge
        Figure 3: Distribution of trigram prefixes of questions in SQuAD and CoQA

@author: zjy
"""

import numpy as np
import argparse
import json
import string
from pyecharts.charts import Sunburst
from pyecharts import options as opts

# In[]: argument
def parse_hparams():
    parser = argparse.ArgumentParser(description='hparams')
    parser.add_argument('-input', default='/Users/sjx/Desktop/lab/MYWORK/KQA Pro/corpus/v1.0/rewrite118k.json')
    parser.add_argument('-ngram', help='ngram', type=int, default=4)
    parser.add_argument('-max_display_num', help='max number of ngrams to display', 
                        type=int, default=15)
    parser.add_argument('-min_count', help='min word occurence', 
                        type=int, default=20)
    args = parser.parse_args()
    return args


# In[]: save ngrams through Trie structure
class Trie:
    def __init__(self, args):
        self.root = ['', 1, 'white', []]
        self.colors = ['#c23531','#2f4554', '#61a0a8', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3']
        self.max_display_num = args.max_display_num
        self.min_word_count = args.min_count
    
    def insert(self, words:list) -> None: # Inserts a word into the trie
        """ Trie insertion """
        curNode = self.root
        for word in words:
            idx, already_contain = isInSubnodes(word, curNode)
            if not already_contain:
                curNode[-1].append([word, 1, [], []])
            else:
                curNode[-1][idx][1] += 1
            curNode = curNode[-1][idx]

    def prune(self, adjust_value=False, adjust_ratio=0.9):
        """ 
        prune based on max_display_num and min_count
        Args:
            adjust_value: if True, adjust node value for better visulization
            adjust_ratio: value within [0,1], the total ratio taken up by child nodes
        
        """
        def recursive(node):
            if len(node[-1]) == 0:
                return
            
            subnodes = node[-1]
            subnodes = sorted(subnodes, key=lambda x: -x[1])[:self.max_display_num]
            subnodes = [n for n in subnodes if n[1] >= self.min_word_count]
            node[-1] = subnodes
            for subnode in node[-1]:
                recursive(subnode)
        
        recursive(self.root)
    
    def assign_node_color(self):
        """ assign node color """
        def recursive(node, father_color):
            if not node:
                return
            
            node[2] = father_color
            for subNode in node[-1]:
                recursive(subNode, father_color)

        numNode_level_1 = len(self.root[-1])

        for idx, subnode_level_1 in enumerate(self.root[-1]):
            # assign father node color
            subnode_level_1[2] = self.colors[idx]
            # assign child node color
            recursive(subnode_level_1, self.colors[idx])

    def postprocess(self):
        # assign root value
        root_value = 0
        for subnode in self.root[-1]:
            root_value += subnode[1]
        self.root[1] = root_value
        
        # prune and colorize
        self.prune()
        # self.assign_node_color()

def isInSubnodes(word, node):
    for i,subnode in enumerate(node[-1]):
        if word == subnode[0]:
            return i, True
    return -1, False


def computeNgramTrie(args, n: int=3, deliminator=" ") -> list:
    all_ngrams = Trie(args)
    preprocess_func = lambda l: l.split(deliminator) if deliminator else l
    texts = json.load(open(args.input))
    for text in texts:
        text = text['rewrite']
        text = [word for word in text.lower().translate(str.maketrans("", "", string.punctuation + string.digits)).split(' ') if len(word)]
        all_ngrams.insert(text[:n])
    all_ngrams.postprocess()
    return all_ngrams


def output(nodes, level=0, max_level=3):
    if level > max_level or not nodes:
        return None

    label, value, color, subnodes = nodes
    if level == 0:
        res = []
        for node in subnodes:
            res.append(output(node, level+1, max_level))
    else:
        children = []
        for node in subnodes:
            child = output(node, level+1, max_level)
            if child:
                children.append(child)
        res = {'name': label, 
            'value': value}
            # "itemStyle": {"color": color}, 
        if children:
            res['children'] = children
    return res


if __name__ == '__main__':
    # args
    args = parse_hparams()

    # generate ngram
    ngramTrie = computeNgramTrie(args, n=args.ngram, deliminator=" ")
    # plot sunburst
    data = output(ngramTrie.root, max_level=args.ngram)

    c = (
        Sunburst(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add(
            "",
            data_pair=data,
            highlight_policy="ancestor",
            radius=[0, "95%"],
            sort_="null",
            levels=[
                {},
                {"r0": "10%","r": "30%"},
                {"r0": "30%", "r": "50%"},
                {"r0": "50%","r": "75%"},
                {"r0": "75%", "r": "100%"},
            ],
        )
        .set_global_opts(title_opts=opts.TitleOpts(
            title="Question Prefixes Distribution",
            ))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
        .render("tmp.html")
    )
