# @author Marco Panajia
# Calcolatrice in Python

print("Inserire primo numero: ")
n1=int(input())
print("Inserire secondo numero: ")
n2=int(input())
print("Che operazione vuoi fare ?\n1) Somma \n2) Sottrazione \n3) Moltiplicazione \n4) Divisione\n--> ")
scelta= int(input())
while scelta!=1 and scelta!=2 and scelta!=3 and scelta!=4:
  print("La scelta non è corretta !\nChe operazione vuoi fare ?\n1) Somma \n2) Sottrazione \n3) Moltiplicazione \n4) Divisione\n--> ")
  scelta= int(input())
if scelta == 1:
  somma = n1 + n2
  print("La somma è uguale a: ")
  print(somma)
if scelta == 2:
  sottrazione = n1 - n2
  print("La sottrazione è uguale a: ")
  print(sottrazione)
if scelta == 3:
  moltiplicazione = n1 * n2
  print("La moltiplicazione è uguale a: ")
  print(moltiplicazione)
if scelta == 4:
  divisione = n1 / n2
  print("La divisione è uguale a: ")
  print(divisione)
print("Vuoi ancora usare la calcolatrice ? [s/n]: ")
continuazione = input('')
while continuazione!='s' and continuazione!='n':
    print("Errore !\nVuoi ancora usare la calcolatrice ? [s/n]: ")
    continuazione = input('')
while continuazione == 's':
  print("Inserire primo numero: ")
  n1=int(input())
  print("Inserire secondo numero: ")
  n2=int(input())
  print("Che operazione vuoi fare ?\n1) Somma \n2) Sottrazione \n3) Moltiplicazione \n4) Divisione\n--> ")
  scelta= int(input())
  while scelta!=1 and scelta!=2 and scelta!=3 and scelta!=4:
    print("La scelta non è corretta !\nChe operazione vuoi fare ?\n1) Somma \n2) Sottrazione \n3) Moltiplicazione \n4) Divisione\n--> ")
    scelta= int(input())
  if scelta == 1:
    somma = n1 + n2
    print("La somma è uguale a: ")
    print(somma)
  if scelta == 2:
    sottrazione = n1 - n2
    print("La sottrazione è uguale a: ")
    print(sottrazione)
  if scelta == 3:
    moltiplicazione = n1 * n2
    print("La moltiplicazione è uguale a: ")
    print(moltiplicazione)
  if scelta == 4:
    divisione = n1 / n2
    print("La divisione è uguale a: ")
    print(divisione)
  print("Vuoi ancora usare la calcolatrice ? [s/n]: ")
  continuazione = input('')
  while continuazione!='s' and continuazione!='n':
    print("Errore !\nVuoi ancora usare la calcolatrice ? [s/n]: ")
    continuazione = input('')
  

