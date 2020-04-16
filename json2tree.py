#!/usr/bin/python3
""" A python code to generate a tree for the JSON API links """
import sys, os
import json
import requests

class Node:
    def __init__(self, value=None, children=None):
        if children is None:
            children = []
        self.value, self.children = value, children

def pprint_tree(node, file=None, _prefix="", _last=True):
    print(_prefix, "└─ " if _last else "├─ ", node.value, sep="", file=file)
    _prefix += "   " if _last else "│  "
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        _last = i == (child_count - 1)
        pprint_tree(child, file, _prefix, _last)

def printTree(field, _prefix=''):
    global isFirstKey
    if isinstance(field, dict):
        print(_prefix + '|- (object)')
        print('  ', end='')
        for key in field.keys():
            print(_prefix + key + ' ', end='')
            printTree(field[key])
    if isinstance(field, list):
        print('(array)')
        print('  ', end='')
        printTree(field[0], _prefix='  ')
    if isinstance(field, str):
        print('(string)')
        print('  ', end='')
    if isinstance(field, int):
        print('(integer)')
        print('  ', end='')


if __name__ == '__main__':
    # f = open('data.json', 'r')
    # jsonTest = json.load(f)
    link = 'https://api.covid19india.org/state_district_wise.json'
    jsonTest = requests.get(link).json()
    printTree(jsonTest)

