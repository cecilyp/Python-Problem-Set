# STAT/CS 287
# HW 01
#
# Name: <Cecily Page>
# Date: <Thursday, September 6th 2018>

import random


def coin_flip(p):
    """
    :param p:
    :return:
    """
    prob = random.random()
    if prob <= p:
        return 'H'
    else:
        return 'T'


def count_runs(coin_flips: list):

    runs = []
    count = 0
    for flip in coin_flips:

        if flip is 'H':
            count = count + 1
            continue
        elif count == 0:
            continue
        else:
            runs.append(count)
            count = 0

    return runs


def run_stats(run: list):
    stats = {}
    final_stats = {}
    for item in run:
        if item in stats:
            stats[item].append(item)
        else:
            stats[item] = [item]

    for key, value in stats.items():
        final_stats[key] = len(value)
    return final_stats


probabilities = [0.2, 0.4, 0.6, 0.8]
all_flips = []

for prob in probabilities:
    prob_flip = []

    for j in range(1000):
        prob_flip.append(coin_flip(prob))

    all_flips.append(prob_flip)

for i, flips in enumerate(all_flips):
    print('This is the number of runs for probability of heads being ', probabilities[i])
    runs = count_runs(flips)
    print(run_stats(runs))

# print(all_flips)
# YOUR CODE HERE #
