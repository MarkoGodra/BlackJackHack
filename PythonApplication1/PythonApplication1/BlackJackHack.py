import sys
import numpy as np
import random

def cmp(a, b) :
    if(a > b) :
        return 1
    elif(b > a) :
        return -1
    else :
        return 0

# n - number of cards in deck
# i - number of cards already played (goes from 0 - n)
# p - number of cards player taken
# d - number of cards dealer taken


def BJ(i) :
 
    options = [0]

    if (n - 1) < 4 :
        print("Not enough cards")
        return 0 # No more cards

    for p in range(2, n - i -2) : # Number of cards taken

        print("#######Player will have total of", p, "##########")
        #player hand
        player = c[i] + c[i + 2] + sum(c[i + 4 : i + p + 2])
        print("Player draws ", c[i + 4 : i + p + 2])
        print("player = ", player)

        #if player's hand is more than 21 player is busted
        if(player  > 21) :
            print("Player busted")
            print("Player = ", player)
            options.append(-1 + BJ(i + p + 2))
            #print("options", options)
            break # Breaks out of for loop and goes to return

        for d in range(2, n - i - p) :
            
            print("########Dealer will have total of ", d, " cards, and player has ", p, " cards#######")
            dealer = c[i + 1] + c[i + 3] + sum(c[i + p + 2 : i + p + d])
            print("Dealer draws ", c[i + p + 2 : i + p + d])
            print("Dealer = ", dealer)

            if (dealer >= 17) :
                print("Dealer stops drawing")
                break
    
        if (dealer > 21) :
            print("Dealer busted")
            dealer = 0
            
        print("End of hand")
        print("Player = ", player, " : Dealer = ", dealer)
        print()

        options.append(cmp(player, dealer) + BJ(i + p + d))

    #print("Options : ", options)
    return max(options)
             


#c = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]

c = [10, 7, 4, 2, 1, 2, 3, 1, 6]
#c = [10,9,3,1,5,5,6,7,3,8,10,9,1,2,2,3,4,5,6,7,9,1]

np.random.shuffle(c)
n = len(c)

print("Cards : ", c)
print("Max money that can be won ", BJ(0), "$")