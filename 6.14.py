f = open("first.txt", "r")
first=f.read()
f.close()
ff = open("second.text","r")
second=ff.read()
ff.close()
player=1
cont=True
print("Welcome players")
while cont==True :
    if len(first)==1 and len(second)==1 :
      print("There are not more moves left." + "Player "+str(player)+" you win!!")
      cont=False
    elif len(first)==0 :
      print("There are not more moves left." + "Player "+str(player)+" you win!!")
      cont=False
    elif len(second)==0 :
      print("There are not more moves left." + "Player "+str(player)+" you win!!")
      cont=False
    else :
      print("Your DNAS are :"+" "+first + " "+ second)
      print("Player "+ str(player) +" your turn")
      chosen1=input("From which DNA you will remove nucleotides first : ")
      if chosen1=="first":
       move1=input("Enter the nucleotides you want to remove: ")
       while len(move1)>2 :
        move1=input("The nuclotides you can remove are one or two not more.Please retype the nuclotides: ")
       first=first.replace(move1, '',1)
       if len(move1)==1:
        move2=input("Enter the nucleotides you want to remove from the second DNA: ")
        while len(move2)>2 :
         move2=input("The nuclotides you can remove are two not more.Please retype the nuclotides: ")
       elif len(move1)==2:
        move2=input("Enter the nucleotide you want to remove from the second DNA: ")
        while len(move2)>2 :
         move2=input("You can remove only one nucleotide.Please retype the nuclotide: ")
       second=second.replace(move2,'',1)
      elif chosen1=="second" :   
       move1=input("Enter the nucleotides you want to remove: ")
       while len(move1)>2 :
        move1=input("The nuclotides you can remove are one or two not more.Please retype the nuclotides: ")
       second=second.replace(move1, '',1)
       if len(move1)==1:
        move2=input("Enter the nucleotides you want to remove from the first DNA: ")
        while len(move2)>2 :
         move2=input("The nuclotides you can remove are two not more.Please retype the nuclotides: ")
       elif len(move1)==2:
        move2=input("Enter the nucleotide you want to remove from the first DNA: ")
        while len(move2)>2 :
         move2=input("You can remove only one nucleotide.Please retype the nuclotide: ")
        first=first.replace(move2,'',1)
      if player==1 : 
       player=2
      elif player==2 : 
       player=1 
     
     
