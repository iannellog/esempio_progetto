#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale

Sep 4, 2022
- aggiunta del metodo segna_numero alla classe Cartella
- definita la rappresentazione della cartella
- implementato il metoro segna_numero (da verificare corretezza)
"""

import numpy as np


class Cartella:

    def __init__(self):
        """
        La cartella è rappresentato da una matrice 3x9;
        ciascun elemento della matrice memorizza 0 per indicare che la casella
        è vuota, memorizza un numero da 1 a 90 per indicare che il numero è
        presente nella cartella, ma non è stato estratto, memorizza -1 per
        indicare che il numero inizialmente presente nella cartella è stato
        estratto;
        i numeri da 1 a 90 sono in colonne della matrice che rispettano
        la specifica.
        """
        self.caselle = np.zeros((3, 9), dtype=int)

    def segna_numero(self, numero):
        """
        controlla il numero estratto sulla cartella

        Parametri di ingresso:
            numero estratto

        Risultati restituiti:
            quale evento si è verificato: nullo, ambo, terna, quaterna, cinquina, tombola
        """
        if numero not in self.caselle:
            return "nullo"
        else:
            i, j = np.nonzero(self.caselle == numero)  # posizione del numero
            self.caselle[i, j] = -1  # segna che il numero è stato estratto
            risultato_riga = -sum(self.caselle[i][np.nonzero(self.caselle[i] < 0)])  # conta i numeri estratti sulla riga su cui si trova il numero estratto
            risultato_cartella = -sum(self.caselle[np.nonzero(self.caselle < 0)])  # conta i numeri estratti su tutta la cartella
            if risultato_cartella == 15:
                risultato = 'tombola'
            elif risultato_riga == 5:
                risultato = 'cinquina'
            elif risultato_riga == 4:
                risultato = 'quaterna'
            elif risultato_riga == 3:
                risultato = 'terna'
            elif risultato_riga == 2:
                risultato = 'ambo'
            else:
                risultato = 'nullo'
            return risultato


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

