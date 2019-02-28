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

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)


class BinTreeNode:

    def __init__(self, data = None, frequency = None, parent = None, leftChild = None, rightChild = None):

        self._data = data
        self._frequency = frequency
        self._parentNode = parent
        self._leftChild = leftChild
        self._rightChild = rightChild

    _data = 0
    _frequency = 0
    _parentNode = 0
    _leftChild = 0
    _rightChild = 0


class TreeCodec:

    def __init__(self, root):
        self._root = root

    _root = BinTreeNode
    _leaves = defaultdict(BinTreeNode)

    def encode(self):
        pass

    def decode(bitsList, hashables):
        pass



def convertSetenceToFrequencyList(sentence):

    tempFrequencyList = defaultdict(int)
    frequencyList = defaultdict(BinTreeNode)

    aSentence = sentence.lower()

    counter = 0

    for w in aSentence:
        tempFrequencyList[w] += 1
        # print("printing", w , tempFrequencyList[w])

    for w in tempFrequencyList:
        frequencyList[counter] = BinTreeNode(w, tempFrequencyList[w], None, None, None)
        #frequencyList[counter].extend([w, tempFrequencyList[w]])
        print("printing this", w, frequencyList[counter]._frequency)
        counter += 1

    return frequencyList


def createFrequencyTree(frequencyList):
    
    lowestFreqency = BinTreeNode
    secondLowestFreqency = BinTreeNode
    
    pq = PriorityQueue()
    lowestFrequency = frequencyList[0]
    
    stack = []
    
    counter = 0
    
    for w in frequencyList:
        
        if frequencyList[w]._frequency < lowestFrequency._frequency:
            secondLowestFrequency = lowestFrequency
            lowestFrequency = frequencyList[counter]
            counter += 1
    

    for w in frequencyList:
        pq.add(frequencyList[w], frequencyList[w]._frequency)
    
    for w in frequencyList:
        stack.append(pq.pop())
        
    
    
    
    return stack.pop()._frequency

##############################################################
#                            Tests                           #
##############################################################


def test_CreateFrequencyTree():
    
    aSentence = "Hello how can I help you"

    frequencyList = convertSetenceToFrequencyList(aSentence)
    
    assert createFrequencyTree(frequencyList) == 1


def test_SentenceConversion():

    aSentence = "Hello how can I help you"

    frequencyList = convertSetenceToFrequencyList(aSentence)

    assert frequencyList[0]._data == 'h'
    assert frequencyList[0]._frequency == 3
    assert frequencyList[1]._data == 'e'
    assert frequencyList[1]._frequency == 2
    #assert frequencyList[1]._frequency == 1


def test_fequencyListCreation():

    frequencyList = defaultdict(list)

    frequencyList[0].extend(['a', 5])

    assert frequencyList[0][0] == 'a'
    assert frequencyList[0][1] == 5

