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


Have a node class that asks the parent if the chidl node is the right child or the left child
hashtable with the character, pointing to the leaf, and then have that leaf return the traverse up the tree
to get the path for that node.

"""

# class Stack:
#      def __init__(self):
#          self.items = []
#
#      def isEmpty(self):
#          return self.items == []
#
#      def push(self, item):
#          self.items.append(item)
#
#      def pop(self):
#          return self.items.pop()
#
#      def peek(self):
#          return self.items[len(self.items)-1]
#
#      def size(self):
#          return len(self.items)


class BinTreeNode:

    def __init__(self, data = None, frequency = None, parent = None, leftChild = None, rightChild = None):

        self._data = data
        self._frequency = frequency
        self._parentNode = parent
        self._leftChild = leftChild
        self._rightChild = rightChild

    def leafNodes(self):

        if self._leftChild is None and self._rightChild is None:
            yield self
        else:
            yield from self._leftChild.leafNodes()
            yield from self._rightChild.leafNodes()

    def isChild(self, inquire):

        if inquire == self._leftChild:
            return 0
        if inquire == self._rightChild:
            return 1

        return None



class TreeCodec:

    def __init__(self, root):
        self._root = root
        self._leaves = dict(BinTreeNode)

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
    
    pq = PriorityQueue(priority_key=lambda p: p)
    lowestFrequency = frequencyList[0]


    # counter = 0

    # for w in frequencyList:
    #     print("This is w:", w)
    #     if frequencyList[w]._frequency < lowestFrequency._frequency:
    #         secondLowestFrequency = lowestFrequency
    #         lowestFrequency = frequencyList[counter]
    #         counter += 1




    # CHange w for node and use frequencyList.values()

    for w in frequencyList:
        pq.add(frequencyList[w], frequencyList[w]._frequency)
        #pq.add(frequencyList[w])

    # print("Now gunna pop")
    # print(pq.pop()._data)
    # print(pq.pop()._data)
    # print(pq.pop()._data)
    # print(pq.pop()._data)



    counter = 0



    while len(pq) > 1:
    # while counter < 2*len(frequencyList)-1:
    # while counter < 2:



        i = pq.pop()
        j = pq.pop()



        tempParentNode = BinTreeNode(frequency=i._frequency + j._frequency, leftChild=i, rightChild=j)

        i._parentNode = tempParentNode
        j._parentNode = tempParentNode


        pq.add(tempParentNode, tempParentNode._frequency)



    counter += 1

    i = pq.pop()

    return i

def printOutContents(itemsToPrint):

    counter = 0

    while counter < len(itemsToPrint):
        print("Items to print", itemsToPrint)
        counter += 1

def theStackMaker(priorityQueue):

    stack = []
    counter = 0

    while counter < len(priorityQueue):
        stack.append(priorityQueue.pop())

    return stack

def traverseTree(tree):

    for w in len(tree):
        print("This is the tree:", w, tree[w]._data)
        print("This is the node frequency:", w, tree[w].frequency)



##############################################################
#                            Tests                           #
##############################################################



def test_CreateFrequencyTree():

    # aSentence = "Hello how can I help you"
    # aSentence = "Hello"
    aSentence = "haaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"

    frequencyList = convertSetenceToFrequencyList(aSentence)

    TreeCodec = createFrequencyTree(frequencyList)

    # traverseTree(TreeCodec)

    assert TreeCodec._frequency == 111
    assert TreeCodec._leftChild._frequency == 11
    assert TreeCodec._leftChild._leftChild._frequency == 1
    assert TreeCodec._leftChild._rightChild._frequency == 10
    assert TreeCodec._rightChild._frequency == 100







def test_SentenceConversion():

    aSentence = "Hello"

    frequencyList = convertSetenceToFrequencyList(aSentence)

    assert frequencyList[0]._data == 'h'
    assert frequencyList[0]._frequency == 1
    assert frequencyList[1]._data == 'e'
    assert frequencyList[1]._frequency == 1
    assert frequencyList[1]._frequency == 1


def test_fequencyListCreation():

    frequencyList = defaultdict(list)

    frequencyList[0].extend(['a', 5])

    assert frequencyList[0][0] == 'a'
    assert frequencyList[0][1] == 5

