# imports
import os
import random
import time

# Creates and shows a new frame
def printNewFrame(hidden, player, dealer, split):
    #   Clears the terminal(for most of the os)
    os.system('cls' if os.name == 'nt' else 'clear')
    # Hides the dealer's card.
    if(split):
        if (hidden):
            print(f"Dealer: {dealer[0]}, ## | Value of card:{getValueOfCard(dealer[0])}")
            print(f"Player: ", end =" ")
            for i in player:
                for j in i:
                    print(f" {j} |", end =" ")
                print(f"🃏 Hand: ", end=" ")
                print(f"Value of cards:{getAllValue(i)}")
        else:
            # Shows the dealer's card.
            print("Dealer: ", end=" ")
            for i in dealer:
                print(f" {i} |", end=" ")
            print(f"Value of cards:{getAllValue(dealer)}")
            print(f"Player: ", end =" ")
            for i in player:
                print(f" {i} |", end =" ")
            print(f"Value of cards:{getAllValue(player)}")
    else:
        if (hidden):
            print(f"Dealer: {dealer[0]}, ## | Value of card:{getValueOfCard(dealer[0])}")
            print(f"Player: ", end =" ")
            for i in player:
                print(f" {i} |", end =" ")
            print(f"Value of cards:{getAllValue(player)}")
        else:
            # Shows the dealer's card.
            print("Dealer: ", end=" ")
            for i in dealer:
                print(f" {i} |", end=" ")
            print(f"Value of cards:{getAllValue(dealer)}")
            print(f"Player: ", end =" ")
            for i in player:
                print(f" {i} |", end =" ")
            print(f"Value of cards:{getAllValue(player)}")


# Gives the int value of a single card.
def getValueOfCard(cardGiven):
    if(cardGiven[0] == "J" or cardGiven[0] == "Q" or cardGiven[0] == "K"):
        return 10
    elif(cardGiven[0] == "A"):
        return 11
    elif(cardGiven[0] == "1"):
        return 10
    else: return int(cardGiven[0])


# Gets the value of all cards in the hand.
def getAllValue(cards):
    valueOfAllCards = 0
    hasA = False
    numberOfA = 0
    for i in cards:
        if(int(getValueOfCard(i)) >= 11):
            hasA = True
            numberOfA += 1
        else:
            valueOfAllCards += getValueOfCard(i)
    try:
        while(numberOfA>0): # For loop didn't work
            if (hasA == True and valueOfAllCards >= 11 ):
                valueOfAllCards += 1 
            elif(hasA == True and valueOfAllCards < 11):
                valueOfAllCards += 11
            numberOfA -= 1
    except:
        pass
    return valueOfAllCards

def jackblack():
    didYouWin = "False"
    # A deck of palying cards.
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
    split = False
    startingCards = True
    # Player inputs
    while(True):
        if(getAllValue(player) == 21):
                printNewFrame(False,player,dealer,split)
                didYouWin = "Blackjack"
                print("🎉 Blackjack! 🎉")
                break
        # Player logic
        if(player[0][0] == player[1][0] and startingCards):
            print("   (Hit - Get another card, Stand - Skip, Split - split your hand)")
        else:
            print("   (Hit - Get another card, Stand - Skip)")
        command = input("> ")
        if (command.lower() == "hit"):
            # New card.
            player.append(playingCards.pop())
            startingCards = False
            printNewFrame(True,player,dealer,split)
            if(getAllValue(player) == 21):
                printNewFrame(False,player,dealer,split)
                didYouWin = "True"
            elif(getAllValue(player) > 21):
                printNewFrame(False,player,dealer,split)
                print("You lose!")
                break
        elif(command.lower() == "split"):
            split = True
            player2 = [player.pop(),playingCards.pop()]
            player.append(playingCards.pop())
            splitCards = [player, player2]
            printNewFrame(True,splitCards,dealer,split)
        else: 
            # Dealer logic.

            while(getAllValue(dealer) < 17):
                printNewFrame(False,player,dealer,split)
                dealer.append(playingCards.pop())
                time.sleep(2)
                printNewFrame(False,player,dealer,split)

            if(getAllValue(dealer)>21):
                time.sleep(2)
                printNewFrame(False,player,dealer,split)
                print("🎉 You won! 🎉")
                didYouWin = "True"
                break
            if(getAllValue(player) > getAllValue(dealer)):
                time.sleep(2)
                printNewFrame(False,player,dealer,split)
                print("🎉 You won! 🎉")
                didYouWin = "True"
                break
            elif(getAllValue(player) == getAllValue(dealer)):
                time.sleep(2)
                printNewFrame(False,player,dealer,split)
                didYouWin = "Tie"
                print("Tie")
                break
            else:
                time.sleep(2)
                printNewFrame(False,player,dealer,split)
                print("The Dealer Won")
                break
    return didYouWin
    
# Get number input (used for the betting system).
def get_number_input(prompt):
    while True:
        value = input(prompt)
        if value.isnumeric():
            return int(value)
        else:
            print("Please enter a valid number.")


def main():
    # The money of the player.
    playerMoney = 2500
    while(True):
        # Clears the terminal(for most of the os)
        os.system('cls' if os.name == 'nt' else 'clear')
        if(playerMoney == 0):
            print("Man... You should stop")
            break
        print(f"Your money: {playerMoney}")
        bet = get_number_input("> What amount would you like to bet? ")
        while(bet > playerMoney or bet < 1):
            print("> You don't have sufficient funds")
            print(f"Your money: {playerMoney}")
            bet = get_number_input("> What amount would you like to bet? ")
        didYouwin = jackblack()
        if(didYouwin == "True"):
            playerMoney += int(bet)
        elif(didYouwin == "False"):
            playerMoney -= int(bet)
        elif(didYouwin == "Blackjack"):
            playerMoney += int(bet) * 1.5
        
        keepPlaying = input("> Would you like to keep playing? (yes/no)")
        if(keepPlaying.lower == "no"):
            break







    
main()