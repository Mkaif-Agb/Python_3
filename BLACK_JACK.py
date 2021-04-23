import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + " of " + self.rank


class Deck():
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))


    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The Deck has" +  deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck)

class Card():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.ace -= 1

class Chips():
    def __init__(self,total = 100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet


    def lose_bet(self):
        self.total -= self.bet


def take_chip(chips):
    while True:

        try:
            chips.bet = int(input("Enter The Amount of Chips You Want To Bet"))

        except:
            print("Sorry Please Provide an Integer")

        else:
            if chip.bet > chips.total:
                print(f"You Don't Have Enough Chips, The Amount of Chips you have are {chips.total}".format())
            else:
                break


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand():
    global playing
    while True:
        x = input("Hit or Stand? Enter h or s")
        if x[0].lower() == h:
            hit(deck,hand)
        elif x[0].lower() == s:
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Enter h or s Only ")
            continue
        break


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


#----------------------------- CODE IMPLEMENTATION --------------------------------------#
#----------------------------- GAME CODE ------------------------------------------------#

while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()
    take_bet(player_chips)

    show_some(player_hand,dealer_hand)

    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            show_all(player_hand,dealer_hand)

            if dealer_hand.value >21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif player_hand.value > dealer_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)

        print(f"\n Player Total Chips are {player_chips.total}".format())

        new_game = input("Would u like to Play Another hand? Yes or No")

        if new_game[0].lower() == "y":
            playing = True
            continue
        else:
            print("Thank You For Playing")