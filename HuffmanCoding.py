# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 10:36:29 2019

@author: spencer.stewart
"""

from boltons.queueutils import PriorityQueue
from boltons.queueutils import SortedPriorityQueue
from collections import defaultdict
from enum import Enum


"""

You always connect the two smallest frequency nodes together.
And then create a new node that connects bother of them.
then look at the next lowest two and connect them.



"""


class BinTreeNode:

    def __init__(self, data = None, parent = None, leftChild = None, rightChild = None):

        self._data = data
        self._parentNode = parent
        self._leftChild = leftChild
        self._rightChild = rightChild

    _data = 0
    _parentNode = 0
    _leftChild = 0
    _rightChild = 0


class TreeCodec:

    def __init__(self):
        pass

    root = BinTreeNode


def convertSetenceToFrequencyList(sentence):

    tempFrequencyList = defaultdict(int)
    frequencyList = defaultdict(list)

    aSentence = sentence.lower()

    counter = 0

    for w in aSentence:
        tempFrequencyList[w] += 1
        # print("printing", w , tempFrequencyList[w])

    for w in tempFrequencyList:
        frequencyList[counter].extend([w, tempFrequencyList[w]])
        # print("printing this", w, frequencyList[counter])
        counter += 1

    return frequencyList



##############################################################
#                            Tests                           #
##############################################################



def test_SentenceConversion():

    aSentence = "Hello how can I help you"

    frequencyList = convertSetenceToFrequencyList(aSentence)

    assert frequencyList[0][0] == 'h'
    assert frequencyList[0][1] == 3
    assert frequencyList[1][0] == 'e'
    assert frequencyList[1][1] == 2


def test_fequencyListCreation():

    frequencyList = defaultdict(list)

    frequencyList[0].extend(['a', 5])

    assert frequencyList[0][0] == 'a'
    assert frequencyList[0][1] == 5
