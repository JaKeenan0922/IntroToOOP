#
#
#
# Description-----------------------------------------------------------------------------------------------------------
# Deck.py is a class file containing functions for the manipulations of cards, such as creating decks,
# shuffling, sorting, discarding
# Inherits the cards class
#
#
#
#
#
#
#
#

import random

# ----------------------------------------------------------------------------------------------------------------------
# Import statements
import cards

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# CONSTANTS
NUM_SUITS = 4               # four suits in standard card deck
NUM_PER_SUIT = 13           # 13 cards in a standard suit
CUT_BUFFER = 5              # number of cards from end considered a viable selection for a cut
MIX_BUFFER = 4              # range for cards to be swapped in a mix shuffle
# ----------------------------------------------------------------------------------------------------------------------


class Deck:
    def __init__(self):
        self.deck_list = []
        self.size = 0
        return

    def make_deck(self):
        # the following function makes a deck
        for i in range(NUM_SUITS):
            for j in range(NUM_PER_SUIT):
                new_card = cards.Card(j, i)     # create a temporary card
                self.deck_list.append(new_card)     # add cards to end of array
                # new_card.print_properties()     # print card, mostly for testing.
        self.size = len(self.deck_list)
        return

    def print_deck(self):
        for i in range(self.size):
            self.deck_list[i].print_properties()
        print()
        return

    def shuffle(self):
        # takes in an array of cards, and randomly cuts, and mixes cards
        it = random.randint(30, 100)
        for i in range(it):
            self.mix(random.randint(10, 30))
            self.cut()
            self.mix(random.randint(10, 30))
            self.mix(random.randint(10, 30))
            self.cut()
            self.mix(random.randint(10, 30))
            self.mix(random.randint(10, 30))
            self.mix(random.randint(10, 30))
            self.cut()
        return

    def cut(self):
        # cuts a deck at a given index, and places the lower half atop the cut location.
        random.seed()

        cut_index = random.randint(CUT_BUFFER, self.size-CUT_BUFFER)
        # selection size represents the number of cards at the bottom which must me moved to top
        selection_size = self.size-cut_index

        # if less than half of deck size, should shift top down instead of bottom up.
        if cut_index < (self.size-1)/2:
            for i in range(cut_index):
                temp = self.deck_list[0]
                self.deck_list.append(temp)
                self.deck_list.pop(0)
        else:
            for i in range(selection_size):
                # a cut gets a random value with an offset of at least CUT_BUFFER from the deck ends
                # and selects cards from selected index to the bottom of the deck, and inserts them at the start of
                # the deck and pops off the old values as we go.
                temp = self.deck_list[self.size-1]
                self.deck_list.insert(0, temp)
                self.deck_list.pop()
        return

    def mix(self, iterations):
        # mixes the cards provided by randomly swapping indexes within 4 places of one another
        # parameter iterations defines number of cards swapped. by default, deck size is used.
        if iterations is None:
            iterations = self.size

        for i in range(iterations):
            swap_dex = random.randint(-3, 3)
            index = random.randint(MIX_BUFFER, self.size-MIX_BUFFER)
            temp = self.deck_list[index]
            self.deck_list[index] = self.deck_list[index + swap_dex]
            self.deck_list[index + swap_dex] = temp
        return

    def sort_value(self, group_size, offset):
        # attempting to integrate group_size and offset to allow user to sort a section of say 5 cards by value. Is
        # proving to be difficult- mostly gets sorted but then stops a few iterations short of completion apparently.
        # the idea is to operate this on a deck that was just sorted by suit, and then call this on the number of cards
        # in a suit resulting in a sorted subset
        if group_size is None:
            group_size = self.size
        if offset is None:
            offset = 0
        # this function uses a selection sort algorithm to sort the deck
        # based on the card values, Ace being low in this instance (ignores suit)
        start_dex = offset * group_size
        end_dex = start_dex + group_size - 1
        mindex = 0
        for i in range(start_dex, end_dex):
            mindex = i
            for j in range(i+1, end_dex+1):     # for j=i+1 < self.size j++
                if self.deck_list[j].position < self.deck_list[mindex].position:
                    mindex = j
                self.swap(i, mindex)
        return

    def sort_suit(self):
        # this function uses a selection sort algorithm to sort the deck
        # based on the suit values, alphabetical indexing. (ignores value)
        mindex = 0
        for i in range(self.size-1):
            mindex = i
            for j in range(i+1, self.size):     # for j=i+1 < self.size j++
                if self.deck_list[j].suit[0] < self.deck_list[mindex].suit[0]:
                    mindex = j
                self.swap(i, mindex)
        return

    def simple_sort(self):
        # an inefficient but simple way to return the deck to the original sorted state
        # (alphabetical by suit, low to high material value).
        self.deck_list = []
        self.make_deck()

    def super_sort(self):
        # currently doesn't work... Supposed to sort them by suit, and then by value, but there's some sort of error.
        group_size = int(self.size / NUM_SUITS)
        print("Group size is " + str(group_size))
        self.sort_suit()
        # self.print_deck()
        print()
        for i in range(NUM_SUITS):
            self.sort_value(group_size, i)

    def swap(self, elem1, elem2):
        #
        temp = self.deck_list[elem1]
        self.deck_list[elem1] = self.deck_list[elem2]
        self.deck_list[elem2] = temp
        return
