import random

# ------------------- CLASSES --------------------
class Card:
    def __init__(self, suit, rank, value):
    self.suit = suit
    self.rank = rank
    self.value = value

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

class Dealer:
    def __init__(self):
        self.points = 0

# ------------------- FUNCTIONS ------------------
def createPlayer():
    print('Enter your name: ')
    name = input()
    print()
    print("Hello, " + name + '.')
    player = Player(name)
    return player

def newCard():
    # randomly generate the suit (doesn't matter for Blackjack)
    suit = random.randint(1,4)
    if (suit == 1):
        suit = "______"
    elif (suit == 2):
        suit = "______"
    elif (suit == 3):
        suit = "_______"
    elif (suit == 4):
        suit = "_______"

    # randomly generate the rank to determine point value
    number = random.randint(1,13)
    if (number == 11):
        rank = "J"
        value = 10
    elif (number == 12):
        // Todo 
    elif (number == 13):
        // Todo
    elif (number == 1):
        // Todo
    else:
        rank = number
        value = number
    
    # pass the suit and value to the card
    return Card(suit, rank, value)

def dealCards(player, dealer):
    print("Dealing cards...")
    print()

    # player's cards
    cardP1 = // Todo 
    cardP2 = // Todo
    player.points = // Todo 

    # dealer's cards
    // Todo: similar to the player’s card, draw 2 new cards for the dealer, and calculate the dealer's points

    # say what cards the dealer has
    print("The dealer has the " + str(cardD1.rank) + " of " + cardD1.suit + " and their other card is face down.")
    print()

    # say what cards we have
    print("You have the " + str(______) + " of " + _______ + " and the " + str(cardP2.rank) + " of " + cardP2.suit + '.')
    print("You have " + str(__________) + " points.")
    print()

    return cardD2

def playerHit(player):
    // Todo: give the player a new card & update their points

    //Todo: print to the console the new card value and your new points!

def playerStand(player, dealer, cardD2):
    # first, reveal the dealer's face down card
    print("The dealer flips their other card over. It is the " + str(______) + " of " + _________ + '.')
    print(___________________________)
    print()

    # dealer takes new cards until they are over 17 points
    while (dealer.points < 17):
        dealerHit(dealer)

    # dealer has stopped, now see who wins
    // Todo: Determine who wins by exploring the different combinations. 
    if (__________):
        print("Dealer has more than 21 points! You win!")
        print()
    elif (______________):
        print(_______________)
        print()
    elif (______________):
        print("Dealer has " + str(_________) + " points and you have " + str(________) + " points. You lose.")
        print()
    elif (_______________):
        print("Dealer has " + str(dealer.points) + " points and you have " + str(player.points) + " points. You win!")
        print()
    elif (_______________):
        print("You both have " + str(__________) + " points! No one wins.")
        print()
    else:
        # should never get to this (logically impossible)
        print("ERROR")
        print()

def dealerHit(dealer):
    cardDN = newCard()
    __________________
    print("The dealer takes the " + str(cardDN.rank) + " of " + cardDN.suit + '.')
    print("The dealer now has " + str(________) + " points.")
    print()

def playBlackjack(player, dealer):

    # reset everyone's points
    player.points = 0
    dealer.points = 0

    # deal cards, keeping the dealer's hidden card
    cardD2 = dealCards(player, dealer)

    while(True):
    # first check if you are over 21 points
    if (_________):
        print("You have more than 21 points! You lose.")
        print()
        break

    # if you have Blackjack
    if (___________):
        # must also check if dealer has Blackjack as well
        if (___________):
            print("Both of you have Blackjack! No one wins.")
            print()
            break
        else:
            print("You have Blackjack! You win!")
            print()
            break

    # otherwise (you are less than 21 points)
    else:
        # ask if the player wants another card
        print("Would you like another card? (Y/N)")
        answer = input()
        print()

        if (answer == "____"):
            # "hit" the player with a new card
            __________(_______)
        else:
            # the player stops, now it is the dealer's turn
            playerStand(player, dealer, cardD2)
            # exit the while loop to end the game
            break

def startGame():
    # create the player
    player = createPlayer()

    # create the dealer
    dealer = Dealer()

    # keep playing as long as the player wants
    while(True):
        print("Would you like to play Blackjack? (Y/N)")
        answer = input()
        print()

    if (_____ == “___”):
        ______(_______,_______)
    else:
        break

# play the game!
startGame()
