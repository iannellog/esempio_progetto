#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale
"""

class Tabellone:

    def __init__(self):
        pass

    def segna_numero(self, val):
        """
        controlla il numero estratto su tutto il tabellone

        Parametri di ingresso:
            val: numero estratto

        Risultati restituiti:
            quale evento si è verificato: nullo, ambo, terna, quaterna, cinquina, tombola
        """
        risultato = 'tombola'
        return risultato