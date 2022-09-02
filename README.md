# Specifica del progetto "Gioco della tombola"

Il programma deve implementare il gioco della tombola.

In particolare deve:

- poter estrarre a sorte i numeri da 1 a 90;
- poter creare gruppi di 6 cartelle con le caratteristiche specificate di seguito;
- poter registrare N giocatori;
- poter assegnare un numero M di cartelle a ciascun giocatore (ogni giocatore può avere assegnate un numero diverso di cartelle, per seplicità si può supporre che M non possa essere maggiore di un valore predefinito);
- poter verificare se un numero estratto è presente in una cartella e, se è presente, verificare se si è fatto ambo, terna, quaterna, cinquina o tombola e se uno di questi risultati risulta non ancora raggiunto
- iniziare il gioco estraendo un numero alla volta e verificando ogni volta se qualche giocatore ha realizzato un ambo, una terna, una quaterna, una cinquina o una tombola; per semplicità si può supporre che al più un giocatore può realizzare uno di questi risultati dopo ogni estrazione;
- terminare il gioco quando un giocatore ha realizzato una tombola.

Un gruppo di 6 cartelle deve verificare le seguenti condizioni:

- ogni cartella ha 3 righe e 9 colonne
- ogni cartella ha 15 caselle marcate da un numero da 1 a 90 e 12 caselle vuote
- devono esserci esattamente 5 numeri su ogni riga
- devono esserci da 1 a 3 numeri su ogni colonna
- la prima colonna contiene i numeri da 1 a 9, la seconda i numeri da 10 a 19, la terza i numeri da 20 a 29,... la nona colonna contiene i numeri da 80 a 90
- quando presente in una cartella, il numero 90 occupa sempre la casella nell'angolo in basso a destra (riga 3, colonna 9)
- ogni numero da 1 a 90 deve essere presente su una e una sola cartella

# Istruzioni per giocare

Per giocare digitare da linea di comando:

> `python tombola.py -g numero_giocatori -n lista_numero_di_cartelle_per_giocatore`

Ad esempio il comando:

> `python tombola.py -g 3 -n 3 6 4`

Avvia il gioco con 3 giocatori che hanno rispettivamente 3, 6 e 4 cartelle.

Per elencare tutte le opzioni possibili digitare:

> `python tombola.py -h`

Premere `return` per estrarre un numero. Dopo ogni numero viene visualizzato il corrispondente risultato per ciascun giocatore.


