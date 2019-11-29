import cards
import os

deck = cards.Deck()
print("Here is an initialized card deck (it initializes to empty):")
print(deck)
print("\n")

deck.set_standard()
print("Here is a card deck filled with a standard set of cards:")
print(deck)
print("\n")

deck.shuffle()
print("Here is that deck shuffled:")
print(deck)
print("\n")

deck.shuffle()
print("Here is that deck shuffled one more time:")
print(deck)
print("\n")

ans = input("\n*** Press any key to continue to a demonstration of a dealer dealing cards to a player ***")
os.system('clear')

print(
    "now, if you're dealing a deck of cards, you can collect the",
    "cards in a hand that the player has. This hand is a deck of cards",
    "that start out empty, and we add cards to it as the dealer deals them.")

player = cards.Deck()

while True:
    print("\nCards in the deck --> {}".format(deck))
    print("\nCards in the players hand --> {}\n".format(player))
    while True:
        ans = input("Would you like me to deal you a card? (Y/n)")
        if ans in "yYnN\n":
            break
        else:
            print("Invalid input. Please try again.")

    if ans in "yY\n":
        player.add_card(deck.deal_card())

    else:
        break

ans = input("\n*** Press any key to continue to a demonstration of a dealer dealing 5 cards to three players ***")
os.system('clear')

print("Now let's have the dealer deal 5 cards to each of three players")

# each player starts with an empty hand
player1 = cards.Deck()
player2 = cards.Deck()
player3 = cards.Deck()

# Create the dealers deck by initializing a new deck and calling the set_standard method
# ...note how you can do this all in one line
dealer = cards.Deck()

# let's set the dealers deck to have all the standard cards, then shuffle the deck
dealer.set_standard()
dealer.shuffle()

# let's deal each player 5 cards
for x in range(5):
    player1.add_card(dealer.deal_card())
    player2.add_card(dealer.deal_card())
    player3.add_card(dealer.deal_card())

print("\nPlayer 1's cards are:")
print("{}, the total value of which is {}".format(player1, player1.points()))

print("\nPlayer 2's cards are:")
print("{}, the total value of which is {}".format(player2, player2.points()))

print("\nPlayer 3's cards are:")
print("{}, the total value of which is {}".format(player3, player3.points()))

print("\nDealers remaining cards are:")
print("{}, the total value of which is {}".format(dealer, dealer.points()))

ans = input(
    "\n*** Press any key to continue to a demonstration of a players throwing their cards away (on a pile) ***"
)
os.system('clear')

print("Now let's have the dealer deal 5 cards to each of three players")

print(
    "\n\nLet's say that player 1 decides to throw their first card on the pile, and player 2, their third card, and player 3 their second card"
)
pile = cards.Deck()  # create and empty deck called pile to store the discarded cards
pile.add_card(player1.remove_card(0))
pile.add_card(player2.remove_card(2))
pile.add_card(player3.remove_card(1))

print("\nPlayer 1's cards are now:")
print("{}, the total value of which is {}".format(player1, player1.points()))

print("\nPlayer 2's cards are now:")
print("{}, the total value of which is {}".format(player2, player2.points()))

print("\nPlayer 3's cards are now:")
print("{}, the total value of which is {}".format(player3, player3.points()))

print("\nDealers remaining cards are:")
print("{}, the total value of which is {}".format(dealer, dealer.points()))

print("\nThe cards in the pile (that have been thrown away) are:")
print("{}, the total value of which is {}".format(pile, pile.points()))
