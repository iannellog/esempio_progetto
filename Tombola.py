#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:29:04 2022

@author: iannello

Sep 2, 2022:
- Acquisizione da riga di comando del numero di giocatori e
del numero di cartelle per giocatore
- Verifica che i dati da linea di comando siano coerenti e
segnalazione nel caso non lo siano
- Creazione sacchetto, tabellone e cartelle
- Creazione giocatori

Sep 3, 2022
- Assegnazione cartelle ai giocatori
- Estrazione del numero e verifica da parte dei giocatori
"""

from argparse import ArgumentParser
from math import ceil

from Sacchetto import Sacchetto
from Tabellone import Tabellone
from Cartelle import Gruppo_cartelle
from Giocatore import Giocatore

parser = ArgumentParser()
parser.add_argument('-g', '--n_giocatori',
                    help='Numero dei giocatori',
                    type=int, default=2)
parser.add_argument('-n', '--n_cartelle',
                    help='Numero di carelle per giocatore (lista, default [1, 1])',
                    nargs='*', type=int, default=[1, 1])


ranking = ['nullo', 'ambo', 'terna', 'quaterna', 'cinquina', 'tombola']


def is_migliore(nuovo_risultato, risultato_precedente):
    """
    Parametri
        un nuovo risultato da confrontare con il precedente migliore
        risultato (nuovo_risultato)
        precedente miglore risultato (risultato_precedente)

    Risultati restituiti
        True se il nuovo risultato è migliore, False altrimenti
    """
    if ranking.index(nuovo_risultato) > ranking.index(risultato_precedente):
        return True
    else:
        return False


if __name__ == '__main__':
    # Acquisisci quanti giocatori e quante cartelle per giocatore
    args = parser.parse_args()
    n_giocatori = args.n_giocatori
    n_cartelle = args.n_cartelle
    if len(n_cartelle) == n_giocatori:
        print(f'Vi sono {n_giocatori} giocatori che chiedono rispettivamente {n_cartelle} cartelle')
    else:
        print(f'Il numero di giocatori non corrisponde alla lunghezza della lista di cartelle da assegnare')
        exit(1)

    # Crea sacchetto da cui estrarre i numeri
    sacchetto = Sacchetto()

    # Crea tabellone
    tabellone = Tabellone()

    # Genera un numero sufficiente di cartelle a gruppi di 6
    tot_cartelle = sum(n_cartelle)
    n_gruppi = ceil(tot_cartelle/6)
    cartelle = []
    for i in range(n_gruppi):
        cartelle += Gruppo_cartelle().genera_gruppo()
    print(f'Create {len(cartelle)} cartelle')

    # Distribuisci le cartelle ai giocatori
    giocatori = []
    assegnate = 0
    for i in range(n_giocatori):
        giocatore = Giocatore()
        giocatore.riceve_cartelle(cartelle[assegnate:assegnate+n_cartelle[i]])
        assegnate += n_cartelle[i]
        giocatori.append(giocatore)

    risultato_migliore = 'nullo'
    print('Il gioco può iniziare, premi INVIO per estrarre un numero')
    while True:
        input('')
        numero = sacchetto.estrai()
        print(f'Il numero estratto è {numero}')

        # aggiorna tabellone
        segnala = False
        risultato = tabellone.segna_numero(numero)
        flag = is_migliore(risultato, risultato_migliore)
        if flag:
            risultato_migliore = risultato
            segnala = True

        # aggiorna le cartelle dei giocatori
        for giocatore in giocatori:
            risultato = giocatore.segna_numero(numero)
            flag = is_migliore(risultato, risultato_migliore)
            if flag:
                risultato_migliore = risultato
                segnala = True

        # rileva vincite
        if segnala:
            print(f'---> {risultato_migliore}')

        # se qualcuno ha fatto tombola termina il gioco
        if risultato_migliore == 'tombola':
            print('Il gioco è terminato')
            break
