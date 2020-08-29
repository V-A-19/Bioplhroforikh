# -*- coding: utf-8 -*-

#nucleo_1="ACC"
#nucleo_2="ACAAG"
with open('first.txt', 'r') as file:
        nucleo_1= file.read()
with open('second.txt', 'r') as file:
        nucleo_2 = file.read().replace('\n', '')


print("lenght1" , len(nucleo_1))
print("lenght2" , len(nucleo_2))

def remove_from_bigger(nucleo_1, nucleo_2):
    if len(nucleo_1)>len(nucleo_2):
        nucleo_1=nucleo_1[:-2]
        nucleo_2=nucleo_2[:-1]
    else:
        nucleo_2=nucleo_2[:-2]
        nucleo_1=nucleo_1[:-1]

    return nucleo_1,nucleo_2


def remove_from_smaller(nucleo_1, nucleo_2):
    if len(nucleo_1)>len(nucleo_2):
        nucleo_1=nucleo_1[:-1]
        nucleo_2=nucleo_2[:-2]
    else:
        nucleo_2=nucleo_2[:-1]
        nucleo_1=nucleo_1[:-2]

    return nucleo_1,nucleo_2
    #print(nucleo_1)
    #print(nucleo_2)

round=1
#print("Starting nucleotides are: {} and {}".format(nucleo_1, nucleo_2))

print("The algorithm used now will be: 1st player removes 2 from the biggest\
sequence and 1 from the smallest and the 2nd player the opposite.")
def first_most(nucleo_1, nucleo_2, round):
    while True:
    #    print("\nRound {}".format(round))
     #   print("player 1")
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 2 wins")
            break
        nucleo_1, nucleo_2=remove_from_bigger(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 1 wins")
            break
      #  print("player 2")
        nucleo_1, nucleo_2=remove_from_smaller(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        round+=1


first_most(nucleo_1, nucleo_2, round)

print("The algorithm used now will be: 1st player removes 2 from the biggest\
sequence and 1 from the smallest and the 2nd player the same.")
def both_most(nucleo_1, nucleo_2, round):
    while True:
       # print("\nRound {}".format(round))
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 2 wins")
            break
        #print("player 1")
        nucleo_1, nucleo_2=remove_from_bigger(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 1 wins")
            break
        #print("player 2")
        nucleo_1, nucleo_2=remove_from_bigger(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        round+=1
        
both_most(nucleo_1, nucleo_2, round)



print("The algorithm used now will be: 1st player removes 1 from the biggest\
sequence and 2 from the smallest and the 2nd player the opposite.")
def first_less(nucleo_1, nucleo_2, round):
    while True:
        #print("\nRound {}".format(round))
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 2 wins")
            break
        #print("player 1")
        nucleo_1, nucleo_2=remove_from_smaller(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 1 wins")
            break
        #print("player 2")
        nucleo_1, nucleo_2=remove_from_bigger(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        round+=1

first_less(nucleo_1, nucleo_2, round)

print("The algorithm used now will be: 1st player removes 1 from the biggest\
sequence and 2 from the smallest and the 2nd player the same.")
def both_less(nucleo_1, nucleo_2, round):
    while True:
       # print("\nRound {}".format(round))
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 2 wins")
            break
        #print("player 1")
        nucleo_1, nucleo_2=remove_from_smaller(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        if len(nucleo_1)==0 or len(nucleo_2)==0:
            print("player 1 wins")
            break
        #print("player 2")
        nucleo_1, nucleo_2=remove_from_smaller(nucleo_1, nucleo_2)
        #print(nucleo_1)
        #print(nucleo_2)
        round+=1

both_less(nucleo_1, nucleo_2, round)



explanation="""
Explanation:
Οπότε σύμφωνα με τα παραπάνω πειράματα,
υπάρχουν οι εξής εκδοχές(ζεύγη):
(θα αναφερθώ στα μήκη του εκάστοτε νουκλεοτιδίου ώς m και n),

1: m=ζυγός και n=ζυγός
2: m=μονός και n=μονός
3: m=ζυγός και n=μονός
4: m=μονός και n=ζυγός

Επίσης υπάρχουν οι συνδυσμοί των τεχνικών που μπορούν να χρησιμοποιήσουν οι
παίκτες, οι οποίοι είναι:

(Αναφέρομαι στη μέθοδο "αφαιρεί περισσότερα" ως την μέθοδο όπου ο παίκτης
επιλέγει να αφαιρεί 2 νουκλεοτίδια απο την αλληλουχία που έχει τα περισσότερα
και 1 απο την αλληλουχια που έχει τα λιγότρα. Αντίστοιχα "αφαιρεί λίγοτερο"
αναφέρεται στην μέθοδο που ο παίκτης επιλέγει να αφαιρεσει 1 νουκλεοτίδιο απο
την αλλήλουχία με τα περισσότερα και 2 απο την αλληλουχια με τα περισσότερα)

5: παικτης1=αφαιρεί περισσότερα και παίκτης2=αφαιρεί λιγότερα
6: παικτης1=αφαιρεί περισσότερα και παίκτης2=αφαιρεί περισσότερα
7: παικτης1=αφαιρεί λιγότερα και παίκτης2=αφαιρεί περισσοτερα
8: παικτης1=αφαιρεί λιγότερα και παίκτης2=αφαιρεί λιγότερα


Σύμφωνα με τα παραπάνω δημιουργείται ο παρακάτω πίνακας:
|Συνδυασμός περίπτωσης με μέθοδο | Νικητής  |
| 1 με 5                        | παίκτης1 |
| 1 με 6                        | παίκτης1 |
| 1 με 7                        | παίκτης1 |
| 1 με 8                        | παίκτης2 |

| 2 με 5                        | παίκτης2 |
| 2 με 6                        | παίκτης2 |
| 2 με 7                        | παίκτης1 |
| 2 με 8                        | παίκτης1 |

| 3 με 5                        | παίκτης2 |
| 3 με 6                        | παίκτης2 |
| 3 με 7                        | παίκτης1|
| 3 με 8                        | παίκτης1 |

| 4 με 5                        | παίκτης1 |
| 4 με 6                        | παίκτης2 |
| 4 με 7                        | παίκτης1 |
| 4 με 8                        | παίκτης2 |

Οπότε σε κάθε γύρο θα πρέπει να υπολογίζεται εκ νέου το ποιος παικτης παίζει
και σε ποιον συνδυασμο ανηκουν οι αλληλουχίες εκεινης της στιγμής για να βγει
ο νικητής(σύμφωνα πάντα με τον παραπάνω πίνακα).


"""
print(explanation)

