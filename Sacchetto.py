#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale

Sep 3, 2022
- impementazione mediante generator
Sep 4, 2022
- aggiunto un generatore di numeri casuali da 0 a n-1
"""

import random
import time


def random_num(n: int, seed: int = None):
    """
    Generator
    the generator drow an infinite list of numbers by lot
    Numbers are between 0 and n-1
    The random generator is initialized by a different seed
    each time the generator is created, unless an explicit seed
    is passed upn creation
    """
    if seed is None:
        random.seed(time.perf_counter_ns())
    else:
        random.seed(seed)
    while True:
        yield random.randrange(n)


def extractor(n, seed=None):
    """
    Generator
    the generator drow n numbers by lot
    Numbers are between 1 and N and are all different
    After n extractions the iterator terminates
    The random generator is initialized by a different seed
    each time the generator is created, unless an explicit seed
    is passed upn creation
    """
    if seed is None:
        random.seed(time.perf_counter_ns())
    else:
        random.seed(seed)
    tobe_extracted = [i+1 for i in range(n)]
    while len(tobe_extracted) > 0:
        ind = random.randrange(len(tobe_extracted))
        x = tobe_extracted.pop(ind)
        yield x


class Sacchetto:

    def __init__(self, seed=None):
        self.pool_di_numeri = extractor(90, seed)

    def estrai(self):
        """
        estrae un numero dal sacchetto

        Risultati restituiti:
            numero estratto
        """
        try:
            return self.pool_di_numeri.__next__()
        except StopIteration:
            return 0
