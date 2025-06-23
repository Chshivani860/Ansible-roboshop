import random
print("Russian Rolulette")
print("""Rules:
      1. Enter the number of players
      2. Roll the dice
      3. If you roll 6, its GAME OVER """)
players = int(input("Enter number of players:"))
i=0


while i!=6:
    for j in range(players):
        print("plater ENTER KEY to roll the dice")
        i = random.randint(1,6)

        if i==6:
            print("player ", j+1,"rolled 6, GAME OVER")
            break
        else:
            print("player", j+1,"rolled " ,i, ".GAME CONTINUES")