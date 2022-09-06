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

from Sacchetto import random_num, Sacchetto


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

    def stampa(self):
        print(self.caselle)

    def blocca_posizione(self, i, j):
        """
        blocca la casella di indici i, j se non è occupata,
        altrimenti blocca un altra casella non bloccata della
        colonna j
        """
        if self.caselle[i, j] == 0:
            self.caselle[i, j] = 1
        else:
            i = np.nonzero(self.caselle[:, j] == 0)[0]  # l'indice serve perché np.nonzero restituisce una tupla
            if len(i) == 0:
                print(f'*** errore *** in Cartella.blocca_posizione: non ci sono posizionei libere nella colonna {j}')
                exit(1)
            # blocca la prima casella non bloccata
            self.caselle[i[0], j] = 1


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
          nona colonna;
        - seconda sottofase: partendo da una cartella scelta a caso si bloccano in
          cartelle successive le 3 posizioni della prima colonna; si ripete il
          procedimento per le posizioni rimaste delle colonne successive, partendo
          sempre dalla cartella successiva all'ultima considerata;
        - al termine della seconda sottofase: (i) poiché dopo la prima sottofase
          tutte le cartelle hanno esattamente una casella bloccata in ogni colonna
          il vincolo sulle colonne è soddisfatto, (ii) dopo la prima sottofase c'è
          almeno una cartella che ha boccato la posizione (2,8) che va
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
          attenzione a non spostare la posizione (2,8) in una delle cartelle dove
          essa è bloccata;
        - infine si procede ad assegnare i numeri da 1 a 90 alle posizioni
          bloccate; si procede preliminarmente ad assegnare 90 alla cartella dove
          la posizione (2,8) è bloccata; successivamente, per garantire una
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

        # prima fase, sottofase 2
        c = random_num(6).__next__()  # sceglie una cartella a caso
        # blocca altre 3 posizioni in colonna 0
        for p in range(3):
            cartelle[c].blocca_posizione(0, 0)
            c = (c+1) % 6
        for j in range(1, 8):
            # blocca altre 4 posizioni in colonna j
            for p in range(4):
                cartelle[c].blocca_posizione(0, j)
                c = (c+1) % 6
        # blocca altre 5 posizioni in colonna 8
        for p in range(5):
            cartelle[c].blocca_posizione(0, 8)
            c = (c+1) % 6

        if not self.check_vincoli_gruppo(cartelle):  # vi sono cartelle che non rispettano i vincoli
            # prima fase: sottofase 3
            for c in cartelle:
                while not self.check_vincoli(c):  # la cartella va "aggiustata"
                    # ASSERT: c'è almeno una riga con più di 5 posizioni bloccate e almeno un'altra con meno di 5 posizioni bloccate
                    ind_more = np.nonzero(sum(np.transpose(c.caselle)) > 5)[0][0]  # indice di una riga da cui togliere posizioni bloccate
                    count_more = sum(c.caselle[ind_more]) - 5  # numero di posizioni bloccate da togliere
                    inds_cols = np.nonzero(c.caselle[ind_more] == 1)[0]  # indici di colonna delle posizioni bloccate
                    # toglie tutte le posizioni bloccate in eccesso dalla riga ind_more
                    for j in inds_cols:
                        inds_less = np.nonzero(sum(np.transpose(c.caselle)) < 5)[0]  # indici delle righe a cui aggiungere posizioni bloccate
                        for i in inds_less:
                            if c.caselle[i, j] == 0:  # posizione dela riga i che si può bloccare
                                # sposta la posizione bloccata dalla riga ind_more alla riga i
                                c.caselle[i, j] = 1
                                c.caselle[ind_more, j] = 0
                                count_more -= 1
                                break
                        if count_more == 0:  # non vi sono più posizioni bloccate da rimuovere sulla riga ind_more
                            break

            if not self.check_vincoli_gruppo(cartelle):
                print(f'*** errore *** le cartelle non soddisfano i vincoli')
                exit()

            # seconda fase: assegnare i numeri alle cartelle

            # assegna preliminarmente il numero 90 alla prima cartella che ha la posizione (2,8) bloccata
            for c in cartelle:
                if c.caselle[2, 8] == 1:
                    c.caselle[2, 8] = 90
                    break

            # estrae a sorte i numeri da 1 a 90 e li distribuisce in 9 liste
            sacchetto = Sacchetto()
            bags = [[] for i in range(9)]
            for i in range(90):
                n = sacchetto.estrai()
                if n == 1 or n == 90:  # 1 e 90 sono già piazzati
                    continue
                bags[n // 10].append(n)

            # assegna i numeri una lista alla volta
            for j in range(9):
                # assegna i numeri relativi alla colonna j delle cartelle
                while len(bags[j]) > 0:  # se la lista non è vuota
                    n = bags[j].pop()  # estrai un numero
                    for c in cartelle:
                        inds_rows = np.nonzero(c.caselle[:, j] == 1)[0]  # posizioni bloccate non ancora assegnate nella colonna i
                        if len(inds_rows) > 0:  # vi sono posizioni bloccate non ancora assegnate
                            c.caselle[inds_rows[0], j] = n  # assegna il numero alla posizione bloccata
                            break  # passa ad assegnare un altro numero

        return cartelle

    def check_vincoli(self, cartella):
        """
        Funzione ausiliaria: verifica che le posizioni occupate di
        una cartelle soddisfino i vincoli
        """
        if not sum(sum(cartella.caselle)) == 15:
            return False
        for i in range(3):
            if not sum(cartella.caselle[i]) == 5:
                return False
        for j in range(9):
            if not sum(cartella.caselle[:, j]) > 0:
                return False
        return True

    def check_vincoli_gruppo(self, cartelle):
        """
        Funzione ausiliaria: verifica che le posizioni occupate di
        tutte le cartelle di un gruppo soddisfino i vincoli
        """
        pos90 = False
        for c in cartelle:
            if c.caselle[2, 8] == 1:
                pos90 = True
            if not self.check_vincoli(c):
                return False
        return pos90

