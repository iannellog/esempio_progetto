#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale
"""

import numpy as np


class Tabellone:

    def __init__(self):
        """
        Il tabellone è rappresentato da due matrici 18x5
        la prima matrice memorizza nella riga 'i' (i da 0 a 17) in numeri da
        (i * 5 + 1) a ((i+1) * 5);
        gli elementi della seconda matrice contengono 1 se il numero nella
        casella casella omologa della prima matrice è stato estratto,
        0 altrimenti,
        """
        self.righe_vals = np.zeros((18, 5), dtype=int)
        for i in range(18):
            self.righe_vals[i] = [j for j in range(5*i + 1, 5*(i+1) + 1)]
        self.righe_masks = np.zeros((18, 5), dtype=int)
        # print(self. righe_vals)

    def segna_numero(self, val):
        """
        controlla il numero estratto su tutto il tabellone

        Parametri di ingresso:
            val: numero estratto

        Risultati restituiti:
            quale evento si è verificato: nullo, ambo, terna, quaterna, cinquina, tombola
        """
        i = (val - 1) // 5
        j = (val - 1) % 5
        self.righe_masks[i, j] = 1
        # print(self. righe_masks)
        if sum(self.righe_masks[i]) == 5:  # il test non è corretto: TODO
            risultato = 'tombola'
        else:
            risultato = 'nullo'
        return risultato