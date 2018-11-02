'''from random import *

deck = [{'value' :i,'suit' :c} for c in ['spades','clubs','hearts','diamonds'] for i in range(2,15)]

print(deck[0]['value'],'of',deck[0]['suit'])

shuffle(deck)

print(deck[0]['value'],'of',deck[0]['suit'])

shuffle(deck)

print(deck[0]['value'],'of',deck[0]['suit'])

'''
from random import *

deck = [{'value' :i,'suit' :c} for c in ['spades','clubs','hearts','diamonds'] for i in range(2,15)]

shuffle(deck)

print(deck[0]['value'],'of',deck[0]['suit'])

print(deck[1]['value'],'of',deck[1]['suit'])

print(deck[2]['value'],'of',deck[2]['suit'])


