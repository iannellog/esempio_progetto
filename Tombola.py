#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 10:29:04 2022

@author: iannello

Sep 2,2022:
- Acquisizione da riga di comando del numero di giocatori e
del numero di cartelle per giocatore
"""

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-g', '--n_giocatori',
                    help='Numero dei giocatori',
                    type=int, default=2)
parser.add_argument('-n', '--n_cartelle',
                    help='Numero di carelle per giocatore (lista, default [1, 1])',
                    nargs='*', type=int, default=[1, 1])


if __name__ == '__main__':
    # Acquisisci quanti giocatori e quante cartelle per giocatore
    args = parser.parse_args()
    n_giocatori = args.n_giocatori
    n_cartelle = args.n_cartelle
    print(f'Vi sono {n_giocatori} giocatori che chiedono rispettivamente {n_cartelle} cartelle')

    # Crea tabellone
    # Genera un numero sufficiente di cartelle a gruppi di 6
    # Distribuisci le cartelle ai giocatori
    # Ripeti
    #   estrai un numero
    #   aggiorna tabellone e tabelle
    #   rileva vincite
    #   se qualcuno ha fatto tombola termina il gioco