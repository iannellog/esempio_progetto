#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:29:04 2022

@author: iannello

Sep 2, 2022
- definizione interfaccia e implementazione minimale

Sep 4, 2022
- definizione rappresentazione della classe Cartella
- implementazione del metodo segna_numero
"""

class Giocatore:

    def __init__(self):
        """
        Il giocatore è rappresentato mediante la lista di cartelle a lui
        assegnate (inizialmente vuota)
        """
        self.cartelle = []

    def riceve_cartelle(self, cartelle):
        """
        Parametri di ingresso:
            lista di cartelle assegnate al giocatore
        """
        self.cartelle = cartelle
        # print(f'Il giocatore ha ricevuto {len(cartelle)} cartelle')

    def segna_numero(self, numero):
        """
        controlla il numero estratto su tutte le cartelle assegnate

        Parametri di ingresso:
            numero estratto

        Risultati restituiti:
            quale evento si è verificato: nullo, ambo, terna, quaterna, cinquina, tombola
        """
        for cartella in self.cartelle:
            risultato = cartella.segna_numero(numero)
        return risultato

    def stampa_cartelle(self):
        for c in self.cartelle:
            c.stampa()
            print()
