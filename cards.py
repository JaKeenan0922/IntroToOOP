#
# This file is a class which defines the properties of standard playing cards i.e. suit, value, face or not.
#
#
#
#
#
#
#

# CONSTANTS ------------------------------------------------------------------------------------------------------------
# CARD_NAME is an array of string names corresponding to cards in a typical 52 card deck.
CARD_NAME = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
CARD_SUIT = ['Clubs', 'Diamonds', 'Hearts', 'Spades']   # sorted alphabetically for easy sorting of deck
# Constant representing value of face cards in blackjack
FACE_VALUE = 10
# ----------------------------------------------------------------------------------------------------------------------


class Card:

    def __init__(self, position, suit):
        self.position = position  # integer representing position of card in array with Ace being 0, King being 12
        self.suit = str(CARD_SUIT[suit])         # string representing suit of the card.
        self.isFace = bool(self.position == 10 or self.position == 11 or self.position == 12)   # is it a face card?
        if self.isFace:
            self.value = FACE_VALUE     # integer represents material value of card in blackjack. Faces are worth 10
        else:
            self.value = self.position+1  # sets correct values for all cards except for the Ace special case

    def print_properties(self):
        print(CARD_NAME[self.position] + " of " + self.suit + " worth " + str(self.value) + " points.")

