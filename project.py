#Defining a function named typing.
import time,sys
def typing(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)


import random

typing("Welcome to The Quest!!\n")
typing("Story...\n")
typing("Intro\n")

room=("monster", "shop", "treasure box", "monster", "shop", "monster")

gold=1000 #used in store to buy items
hp=100 #user's hp
opp_hp=100 #monster's hp
extra_hp=0 #extra opponent hp for boss round
stamina=100 #stamina determines the power of user's attack
sword1=False #increases attack by 20
sword2=False #increases attack by 30
sword3=False #increases attack by 40
armor1=False #decreases opp_att by 10
armor2=False #decreases opp_att by 20
armor3=False #decereases opp_att by 30
potion=5 #increases hp by 30
ultra_potion=5 #increases hp by 50
which_potion=0 #variable that lets you select the potion that you want to take.


def fight():
  global opp_hp
  opp_hp=int(100+extra_hp)
  typing("The match starts. You get the first chance\n")
  global hp
  while not hp<=0 or not opp_hp<=0:
    if hp<=0 or opp_hp<=0:
      break
    else:
      typing("Would you like to attack or use potion??\n")
      d=int(float(input("1=Attack, 2=Use potions\n")))
      while d!=2 and d!=1:
        typing("Invalid input. Try again.\n")
        d=int(input("1=Attack, 2=Use potion\n"))
        if d==2 or d==1:
          break
        else:
          pass
          
      #If user decides to attack    
      if d==1:
        userattack=random.randint(40,70)
        typing("You will do the attack now\n")
        opp_hp=opp_hp-userattack*(stamina/100)
        if sword1==True:
          opp_hp=opp_hp-20
        elif sword2==True:
          opp_hp=opp_hp-30
        elif sword3==True:
          opp_hp=opp_hp-40
        if opp_hp>0:
          typing(f"Monster's HP={opp_hp}\n")
        elif opp_hp<=0:
          opp_hp=0
          typing(f"Monster's HP={opp_hp}\n")
      
      #If user decided to use potion
      elif d==2:
        typing("Which potion would you like to drink?\n")
        which_potion=int(input("1=Potion, 2=Ultra Potion\n"))
        if hp==100:
          hp=hp+0
        elif which_potion==1:
          if potion>0:
            hp=hp+30
            potion=potion-1
          elif potion==0:
            typing("You don't have a potion with you.\n")
        elif which_potion==2:
          if ultra_potion>0:
            hp=hp+50
          elif ultra_potion==0:
            typing("You don't have a ultra potion.\n")
        else:
          typing("Invalid input. You lose your chance.\n")
        typing(f"Your HP:-{hp}\n")

      #Monster's turn to attack
      if opp_hp<=0:
        hp=hp+0
      elif opp_hp!=0:
        typing("Now monster will take it's turn.\n")
        opp_attack=random.randint(((m-1)*10), (m*10))
        hp=hp-opp_attack
        if hp<0:
          hp=0
        if armor1==True:
          hp=hp+10
        elif armor2==True:
          hp=hp+20
        elif armor3==True:
          hp=hp+30
        print(f"Your HP={hp}\n")

def potion_time():
  global hp
  global potion
  global ultra_potion
  typing("You have some time to rest.\n")
  typing("Would you like to use a potion?\n")
  a=int(float(input("1=Yes, 2=No\n")))

  #If invalid input for whether user wants a potion or not
  while a!=2 and a!=1:
    typing("Invalid input. Try again.\n")
    a=int(input("1=Attack, 2=Use potion\n"))
    if a==2 or a==1:
      break
    else:
      pass  
  if a==1:
    typing("Which potion would you like to take?\n")
    potion_chosen=int(input("1=Potion, 2=Ultra Potion\n"))

    #If invalid input for potion chosen
    while potion_chosen!=2 and potion_chosen!=1:
      typing("Invalid input. Try again.\n")
      potion_chosen=int(input("1=Potion, 2=Ultra Potion\n"))
      if potion_chosen==2 or potion_chosen==1:
        break
      else:
        pass

    #If user decides to take potion
    if potion_chosen==1:
      #If user's HP is already 100
      if hp==100:
        typing("Your HP is already 100\n")
      elif potion>0:
        hp=hp+30
        #If user HP goes above 100
        if hp>100:
          hp=100
        potion=potion-1
        typing(f"Your HP={hp}\n")
        typing(f"You now have {potion} Potions left\n")
    #If user decides to take ultra potion
    elif potion_chosen==2:
      #If user's HP is already 100
      if hp==100:
        typing("Your HP is already 100\n")
      elif ultra_potion>0:
        hp=hp+50
        #If user HP goes above 100
        if hp>100:
          hp=100
        ultra_potion=ultra_potion-1
        typing(f"Your HP={hp}\n")
        typing(f"You now have {ultra_potion} Ultra Potions left\n")
    potion_time()
  elif a==2:
    pass

n=0
while n!=14:
  inside_room=random.choice(room)

  # if user has to face a monster
  if hp==0:
    break
  elif inside_room=="monster":
    typing("You have to face a monster...\n")
    monsters=("m1", "m2", "m3", "m4", "m5", "m6")
    monster=random.choice(monsters)

    if monster=="m1":
      m=1
      #monster 1
      #Attack in range of 0-10
      typing("You have to face monster 1\n")
      opp_att=random.randint(0,10)
      fight()
      potion_time()

    if monster=="m2":
      m=2
      #monster 2
      #Attack in range of 10-20
      typing("You have to face monster 2\n")
      opp_att=random.randint(10,20)
      fight()
      potion_time()

    if monster=="m3":
      m=3
      #monster 3
      #Attack in range of 20-30
      typing("You have to face monster 3\n")
      opp_att=random.randint(20,30)
      fight()
      potion_time()

    if monster=="m4":
      m=4
      #monster 4
      #Attack in range of 30-40
      typing("You have to face monster 4\n")
      opp_att=random.randint(30,40)
      fight()
      potion_time()

    if monster=="m5":
      m=5
      #monster 5
      #Attack in range of 40-50
      typing("You have to face monster 5\n")
      opp_att=random.randint(40,50)
      fight()
      potion_time()

    if monster=="m6":
      m=6
      #monster 6
      #Attack in range of 50-60
      typing("You have to face monster 6\n")
      opp_att=random.randint(50,60)
      fight()
      potion_time()

    n=n+1

  # if user gets a treasure box
  if hp==0:
    break
  elif inside_room=="treasure box":
    typing("You got a treasure box\n")

    prize=random.randint(2,7)
    gold=gold+(prize*100)

    typing(f"You now have {gold} gold\n")
    n=n+1

  #if user encounters a shop
  if hp==0:
    break
  elif inside_room=="shop":
    typing("You reached a shop..\n")
    typing(f"You have {gold} gold with you. Would you like to the enter the shop?\n")
    
    s=''

    #for incorrect inputs
    while s!="YES" or s!="NO" or s!="yes" or s!="no" or s!="Yes" or s!="No":
      s=input("Yes or No?")
      if s=="YES" or s=="Yes" or s=="yes" or s=="NO" or s=="no" or s=="No":
        break
      else:
        pass
      typing("Incorrect input.Try again\n")

    #whether player wants to enter the shop or not...
    if s=="YES" or s=="Yes" or s=="yes":
      typing("Entering the shop..\n")
    elif s=="NO" or s=="no" or s=="No":
      typing("Leaving the store..\n")
    n=n+1

#If lose anytime in between the game.
if hp==0:
  typing("You lose. Better luck next time....\n")

#Boss round
elif hp!=0:
  typing("You have entered room 15\n")
  typing("You have to face the boss now..\n")
  extra_hp=100
  fight()
  #If user loses the boss round
  if hp==0:
    result="lose"
    typing(f"You have {result} the game...\n")
  #If user wins the boss round
  elif hp!=0:
    result="won"
    typing(f"You have {result} the game..\n")
  #Displaying the result
  if result=="won":
    typing("All the treasure is yours..\n")
  elif result=="lose":
    typing("Unfortunately you couldn't make it to the treasure...\n")
