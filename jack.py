import os
import random
import time

# A new frame
def printNewFrame(hidden, player, dealer):
    #   Clears the terminal(for most of the os)
    os.system('cls' if os.name == 'nt' else 'clear')
    if (hidden==True):
        print(f"Dealer: {dealer[0]}, ## | Value of card:{getValueOfCard(dealer[0])}")
        print(f"Player: ", end =" ") # {player[0]}, {player[1]} | Value of cards:{getAllValue(player)}")
        for i in player:
            print(f" {i} |", end =" ")
        print(f"Value of cards:{getAllValue(player)}")
    else:
        print("Dealer: ", end=" ")
        for i in dealer:
            print(f" {i} |", end=" ")
        print(f"Value of cards:{getAllValue(dealer)}")
        print(f"Player: ", end =" ") # {player[0]}, {player[1]} | Value of cards:{getAllValue(player)}")
        for i in player:
            print(f" {i} |", end =" ")
        print(f"Value of cards:{getAllValue(player)}")

def getValueOfCard(cardGiven):
    if(cardGiven[0] == "J" or cardGiven[0] == "Q" or cardGiven[0] == "K"):
        return 10
    elif(cardGiven[0] == "A"):
        return 11
    elif(cardGiven[0] == "1"):
        return 10
    else: return int(cardGiven[0])

def getAllValue(cards):
    valueOfAllCards = 0
    hasA = False
    numberOfA = 0
    for i in cards:
        if(int(getValueOfCard(i)) == 11):
            hasA = True
            numberOfA += 1
        else:
            valueOfAllCards += getValueOfCard(i)
    try:
        while(numberOfA>0): # For loop didn't work
            if (hasA == True and valueOfAllCards > 11 ):
                valueOfAllCards += 1 # ++ Also works but this makes it more clear. Or apparently not man python is weird 
            elif(hasA == True and valueOfAllCards < 11):
                valueOfAllCards += 11
            numberOfA -= 1
    except:
        pass
    return valueOfAllCards

def jackblack():
    # A deck of palying cards
    playingCardsHeart = ["A♥️","2♥️","3♥️","4♥️","5♥️","6♥️","7♥️","8♥️","9♥️","10♥️","J♥️","Q♥️","K♥️"]
    playingCardsDiamond = ["A♦️","2♦️","3♦️","4♦️","5♦️","6♦️","7♦️","8♦️","9♦️","10♦️","J♦️","Q♦️","K♦️"]
    playingCardsClub = ["A♣️","2♣️","3♣️","4♣️","5♣️","6♣️","7♣️","8♣️","9♣️","10♣️","J♣️","Q♣️","K♣️"]
    playingCardsSpade = ["A♠️" ,"2♠️","3♠️","4♠️","5♠️","6♠️","7♠️","8♠️","9♠️","10♠️","J♠️","Q♠️","K♠️"]
    playingCards = []
    playingCards.extend(playingCardsHeart)
    playingCards.extend(playingCardsDiamond)
    playingCards.extend(playingCardsClub)
    playingCards.extend(playingCardsSpade)
    # Shuffle the cards
    random.shuffle(playingCards)
    # Deals the cards
    dealer = [playingCards.pop(),playingCards.pop()]
    player = [playingCards.pop(),playingCards.pop()]
    print(f"Dealer: {dealer[0]}, ## | Value of card:{getValueOfCard(dealer[0])}")
    print(f"Player: {player[0]}, {player[1]} | Value of cards:{getAllValue(player)}")
    # Checks for a Blakcjack
    if(getAllValue(player) == 21):
        print("🎉 Blackjack! 🎉")

    # Player inputs
    while(True):
        # Player logic

        print("   (Hit - Get another card, Stand - Skip)")
        command = input("> ")
        if (command.lower() == "hit"):
            # New card
            player.append(playingCards.pop())
            printNewFrame(True,player,dealer)
            if(getAllValue(player) == 21): break
            if(getAllValue(player) > 21):
                print("You lose!")
                break
        else: 
            # Dealer logic

            while(getAllValue(dealer) < 17):
                dealer.append(playingCards.pop())
                #   Clears the terminal(for most of the os)
                printNewFrame(False,player,dealer)
                time.sleep(2)

            if(getAllValue(dealer)>21):
                print("🎉 You won! 🎉")
                break
            if(getAllValue(player) > getAllValue(dealer)):
                print("🎉 The player has won! 🎉")
                break
            elif(getAllValue(player) == getAllValue(dealer)):
                print("Tie")
            else:
                print("The Dealer Won")
                break
    


    

    
def main():
    
    # Clears the terminal(for most of the os)
    os.system('cls' if os.name == 'nt' else 'clear')
    jackblack()
    while(True):
        #   Clears the terminal(for most of the os)
        os.system('cls' if os.name == 'nt' else 'clear')
        st = input("> Do you want to keep playing? (y/n) ")
        if (st.lower == 'n'):
            break
        else:
            #   Clears the terminal(for most of the os)
            os.system('cls' if os.name == 'nt' else 'clear')
            jackblack()
main()
