#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale

Sep 4, 2022
- aggiunta del metodo segna_numero alla classe Cartella
"""

class Cartella:

    def __init__(self):
        pass

    def segna_numero(self, numero):
        """
        controlla il numero estratto sulla cartella

        Parametri di ingresso:
            numero estratto

        Risultati restituiti:
            quale evento si è verificato: nullo, ambo, terna, quaterna, cinquina, tombola
        """
        return "nullo"


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

