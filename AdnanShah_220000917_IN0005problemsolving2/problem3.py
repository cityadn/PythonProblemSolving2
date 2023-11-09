import sys
import random

def setup(top_cities):
    random.shuffle(top_cities)

player1 = input("Enter your name Player 1:\n")
player2 = input("Enter your name Player 2:\n")

top_cities = ['Cape Town', 'Cape Town', 'Stone Town',
              'Stone Town', 'Lamu', 'Lamu', 'Essaouira',
              'Essaouira', 'Djenné', 'Djenné', 'Bahir Dar',
              'Bahir Dar', 'Luxor', 'Luxor', 'Windhoek',
              'Windhoek', 'Nairobi', 'Nairobi', 'Agadir',
              'Agadir']

enter = input("Press enter to start the game\n")

score1 = 0
score2 = 0

quit_game = 0

while (len(top_cities) != 0) or (quit_game != 1):
    setup(top_cities)
    quit_game = int(input("Do you want to quit (yes=1, no=0)?\n"))

    if quit_game == 1:
        sys.exit()
    
    print(top_cities)
    ready = input("Press any key if you've read and memorised as much of the list as possible {}".format(player1))

    for i in range(0, 50):
            print("         ")
        
    index1 = int(input("Enter the index of a city {}:\n".format(player1)))
    print(top_cities[index1])

    same_city1 = int(input("""Guess where the repeat of that city is: 
                          (give the index number):\n"""))
    print(top_cities[same_city1])

        
    if (top_cities[same_city1] == top_cities[index1]):
        score1 = score1 + 1
        top_cities.pop(index1)
        top_cities.pop(same_city1-1)
        
    elif (top_cities[same_city1] == top_cities[index1]):
        score1 = score1 + 1
        top_cities.pop(index1-1)
        top_cities.pop(same_city1)
    else:
        score1=score1+0

    print(score1)



    print(top_cities)
    
    ready = input("Press any key if you've read and memorised as much of the list as possible {}".format(player2))

    for i in range(0, 50):
            print("         ")
        
    index2 = int(input("Enter the index of a city {}:\n".format(player2)))
    print(top_cities[index2])

    same_city2 = int(input("""Guess where the repeat of that city is: 
                          (give the index number, {}):\n""".format(player2)))
    print(top_cities[same_city2])

    
    if top_cities[same_city2] == top_cities[index2]:
        score2 = score2 + 1
        top_cities.pop(index2)
        top_cities.pop(same_city2-1)
        
    elif (top_cities[same_city2] == top_cities[index2]):
        score2 = score2 + 1
        top_cities.pop(index2-1)
        top_cities.pop(same_city2)

    else:
        score2=score2+0

    print(score2)

if score1 > score2:
    print("{} wins! {}Score={}, {}Score={}".format(player1, player1, score1, player2, score2))
elif score1 < score2:
    print("{} wins! [}Score={}, {}Score={}".format(player2, player2, score2, player1, score1))
elif score1 == score2:
    print("Tie! {}Score={}, {}Score={}".format(player1, score1, player2, score2))
        

