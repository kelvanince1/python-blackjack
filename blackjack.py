from random import shuffle

playing = False

userMoney = 100

restart_game = "To deal the cards, press 'd'. To quit, press 'q'"

suits = ('Hearts', 'Spades', 'Clubs', 'Diamonds')

suit_value = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

ranking = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

restart_game = 'Press d to deal the cards again or q to quit'

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print (self.suit + self.rank)

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = " "

        for card in self.cards:
            card_name = card.__str__()
            hand_comp += " " + card_name

        return 'The hand has %s' %hand_comp

    def card_add(self, card):
        self.cards.append(card)

        if card.rank == 'A':
            self.ace = True
        self.value += ranking[card.rank]

    def calc_val(self):
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value

    def draw(self, hidden):
        if hidden == True and playing == True:
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card, len(self.cards)):
            self.cards[x].draw()

class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranking:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        shuffle(self.deck)

    def deal(self):
        first_card = self.deck.pop()
        return first_card

    def __str__(self):
        deck_comp = ""
        for card in self.cards:
            deck_comp += " " + deck_comp.__str__()

        return "The deck has" + deck_comp

def make_bet():
    #The default starting number of chips is 100
    global bet
    bet = 0

    print('How many chips would you like to bet?')

    def betting(self):
        place_bet = input()
        place_bet = int(place_bet)
        if place_bet < userMoney:
            print('You do not have enough chips to make that bet')
        else:
            userMoney = userMoney - input

def deal_cards():

    global deck, player_hand, dealer_hand, result, playing, bet, userMoney

    deck = Deck()
    deck.shuffle()

    make_bet()

    player_hand = Hand()
    dealer_hand = Hand()


    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())

    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

    result = "Press 'h' to hit and 's' to stand"

    if playing == True:
        print('Folded')
        userMoney -= bet

    playing = True
    game_step()


def hit():
    global deck, player_hand, dealer_hand, result, playing, bet, userMoney

    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.card_add(deck.deal())

        print("The players hand is %s" %player_hand)

        if player_hand.calc_val() > 21:
            result = 'busted ' + restart_game

            userMoney -= bet
            playing = False

    else:
        result = "Can no longer hit " + restart_game

    game_step()

def stand():
    global playing, deck, player_hand, dealer_hand, result, bet, userMoney, bet

    if playing == False:
        if player_hand.calc_val() > 0:
            result = "Sorry but you cannot stand."

    else:
        while dealer_hand.calc_val() < 17:
            dealer_hand.card_add(deck.deal())

        if dealer_hand.calc_val() > 21:
            result = 'Dealer busts. You win!' + restart_game
            userMoney += bet
            playing = False

        elif player_hand.calc_val() > dealer_hand.calc_val():
            result = "You win!" + restart_game
            userMoney += bet
            playing = False

        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = "Tie!" + restart_game
            playing = False

        else:
            result = 'Dealer wins' + restart_game
            userMoney -= bet
            playing = False

    game_step()

def game_step():
    print("")

    print('The players hand is ' ),
    player_hand.draw(hidden = False)

    print('Players hand total is: ' +str(player_hand.calc_val()))

    print('The dealers hand is '),
    dealer_hand.draw(hidden = False)

    if playing == False:
        print(' -- for a total of ', dealer_hand.calc_val() )
        print('Users money left: ' + str(userMoney))
    else:
        print(' there is another card is face down')

    print(result)

    player_input()

def game_exit():
    print('Thank you')
    exit()

def player_input():
    plin = input().lower()

    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        game_exit()
    else:
        print('Invalid input')
        player_input()

deck = Deck()
deck.shuffle()
player_hand = Hand()
dealer_hand = Hand()
deal_cards()


make_bet()
deal_cards()
hit()
stand()
game_step()
game_exit()
player_input()





# class Player(object):
#     def __init__(self, userMoney=100):
#             self.userMoney = userMoney
#
#     def addMoney(self, addUserMoney):
#         self.userMoney += addUserMoney
#
# class Dealer(object):
#     def __init__(self, dealerMoney=2000000):
#         self.dealerMoney = dealerMoney
#
# class Deal():
#     shuffle(deck)
#     print(deck)
#
#     target = 21
#
#     userCard1 = deck[0]
#     userCard2 = deck[2]
#     dealerCard1 = deck[4]
#     dealerCard2 = deck[6]
#
#     userCards = userCard1[0] + userCard2[2]
#
#     if userCards > 21:
#         print('You busted')
#     elif userCards <= 21:
#         print('Do you want to hit or stand?')
#     else:
#         print('Options')
#
#     print('User Cards')
#     print(userCard1)
#     print(userCard2)
#     print('Dealer Cards')
#     print(dealerCard1)
#     print(dealerCard2)
#
# mike = Player(userMoney=100)
# mike.addMoney(20)
# print(mike.userMoney)
