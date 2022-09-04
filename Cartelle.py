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
- implementato il metodo segna_numero (da verificare corretezza)
- implementata la generazione di un gruppo di cartelle (in parte)
"""

import numpy as np


class Cartella:

    def __init__(self):
        """
        La cartella è rappresentato da una matrice 3x9.
        Nella fase di creazione gli elementi della matrice assumono il
        valore 1 se la casella è bloccata, 0 se non è bloccata,

        Nella fase di gioco, ciascun elemento della matrice memorizza 0
        per indicare che la casella è vuota, memorizza un numero da 1 a
        90 per indicare che il numero è presente nella cartella, ma non
        è stato estratto, memorizza -1 per indicare che il numero
        inizialmente presente nella cartella è stato estratto;
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

    def blocca_posizione(self, i, j):
        """
        blocca la casella di indici i, j
        """
        self.caselle[i, j] = 1


class Gruppo_cartelle:

    def __init__(self):
        pass

    def genera_gruppo(self):
        """
        genera un gruppo di 6 cartelle che rispettano i vincoli

        Strategia:
        - si individuano prima le caselle delle cartelle su cui posizionare i numeri
          in modo da rispettare i vincoli successivamente si assegnano i numeri alle
          caselle precedentemente individuate; la prima fase si scompone in tre
          sottofasi;
        - prima sottofase: nella prima cartella si blocca la posizione (0,0), poi le
          posizioni (1,1), (2,2), (0,3), (1,4), ..., (2,8); si sipete la
          cosa nella cartella successiva iniziando da (1,0); si ripete poi nella
          terza partendo da (2,0) e così fino alla sesta cartella; a questo punto
          sono state bloccate 54 posizioni e ne restano da posizionare 36 di cui
          3 nella prima colonna, 4 nelle colonne dalla seconda all'ottava, 5 nella
          non colonna;
        - seconda sottofase: partendo da una cartella scelta a caso si bloccano in
          cartelle successive le 3 posizioni della prima colonna; si ripete il
          procedimento per le posizioni rimaste delle colonne successive, partendo
          sempre dalla cartella successiva all'ultima considerata;
        - al termine della seconda sottofase: (i) poiché dopo la prima sottofase
          tutte le cartelle hanno esattamente una casella bloccata in ogni colonna
          il vincolo sulle colonne è soddisfatto, (ii) dopo la prima sottofase c'è
          almeno una cartella che ha boccato la posizione (8,8) che va
          obbligatoriamente riservata al numero 90 (iii) poiché dopo la prima
          sottofase tutte le cartelle hanno bloccato 9 posizioni, e poiché nella
          seconda sottofase le caselle sono state bloccate considerando una
          cartella alla volta, dopo la seconda sottofase tutte le cartelle hanno
          bloccato 15 posizioni; pertanto anche tale vincolo è soddisfatto; non
          è invece in generale soddisfatto il vincolo sulle righe;
        - teza sottofase: nel caso in una cartella il vincolo sulle righe non
          sia soddisfatto, si procede a spostare le posizioni bloccate dalle
          righe che hanno più di 5 posizioni bloccate a quelle che ne hanno meno
          fino a soddisfare il vincolo; in questa sottofase occorre fare
          attenzione a non spostare la posizione (8,8) in una delle cartelle dove
          essa è bloccata;
        - infine si procede ad assegnare i numeri da 1 a 90 alle posizioni
          bloccate; si procede preliminarmente ad assegnare 90 alla cartella dove
          la posizione (8,8) è bloccata; successivamente, per garantire una
          distribuzione casuale, si parte dai numeri da 1 a 9 in ordine casuale;
          si passa poi ai numeri da 10 a 19, sempre in ordine casuale e così via
          fino ai numeri da 80 a 89.

        Risultati restituiti:
            lista di cartelle generate
        """
        cartelle = [Cartella() for i in range(6)]

        # prima fase, sottofase 1
        i = 0
        for c in cartelle:
            # blocca nove posizioni nella cartella in nove colonne diverse
            for j in range(9):
                #print(f'({i}, {j})')
                c.blocca_posizione(i, j)
                i = (i + 1) % 3
            i = (i + 1) % 3  # passa alla riga successiva per differenziare le cartelle

        return cartelle

