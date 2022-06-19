# -*- coding: UTF-8 -*-
'''
@Project ：fluent_python_codes 
@File    ：Card.py
@IDE     ：PyCharm 
@Author  ：闻小文
@Date    ：2022/6/19 18:00 
@win_name   ：wzw
'''


import collections
from random import choice


#命名元组赋予每个位置一个含义，提供可读性和自文档性。它们可以用于任何普通元组，
# 并添加了通过名字获取值的能力，通过索引值也是可以的。
Card = collections.namedtuple("Card",["rank","suit"])

class FrenchDeck():
    ranks = [str(n) for n in range(2,11)]+list('JQKA')
    suits = 'spades dimonds clubs hearts'.split()  #->['spades','dimonds',clubs','hearts']

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


deck = FrenchDeck()
print(len(deck))

print(choice(deck))
print('-'*20)

print(deck[:3])
print('-'*20)

print(deck[12::13])
print('-'*20)

#正向迭代
for card in deck:
    print(card)
print('-'*20)

#反向迭代
for card in reversed(deck):
    print(card)
print('-'*20)

#扑克牌排序
suit_values = dict(spades=3,hearts=2,dimonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values)+suit_values[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)
