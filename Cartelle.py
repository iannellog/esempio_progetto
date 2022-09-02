#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale
"""

class Cartella:

    def __init__(self):
        pass


class Gruppo_cartelle:

    def __init__(self):
        pass

    def genera_gruppo(self):
        """
        genera un gruppo di 6 cartelle che rispettano i voncoli

        Risultati restituiti:
            lista di cartelle generate
        """
        return [Cartella() for i in range(6)]

