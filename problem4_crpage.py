# STAT/CS 287
# HW 01
#
# Name: Cecily Page
# Date: September 11 2018

from problem2_crpage import coin_flip
from collections import Counter


def dependent_coin_lip(p, q1, q2):

    flip1 = coin_flip(p)
    if flip1 is 'H':
        flip2 = coin_flip(q1)
    else:
        flip2 = coin_flip(q2)

    return flip1, flip2


def joint_prob(p, q1, q2):

    prob = {('H', 'H'): q1*p, ('H', 'T'): (1-q1)*p, ('T', 'H'): (1-p)*q2, ('T', 'T'): (1-p)*(1-q2)}

    return prob


def print_dictionary_table(d):

    for key, value in d.items():
        print(key, '       ', value)

    return None


flip_546 = []
flip_215 = []
for i in range(1000):
    flip_546.append(dependent_coin_lip(.5, .4, .6))
    flip_215.append(dependent_coin_lip(.2, .1, .5))

count1 = Counter(flip_546)
count2 = Counter(flip_215)

prob1 = joint_prob(.5, .4, .6)
prob2 = joint_prob(.2, .1, .5)

print('Count of Unique Events p=.5, q1=.4, q2=.6')
print_dictionary_table(count1)
print('Count of Unique Events p=.2, q1=.1, q2=.5')
print_dictionary_table(count2)

print('Probabilities for p=.5, q1=.4, q2=.6')
print_dictionary_table(prob1)
print('Probabilities for p=.2, q1=.1, q2=.5')
print_dictionary_table(prob2)
