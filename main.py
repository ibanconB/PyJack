import random

playerIn = True
dealerIn = True

# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand = []
dealerHand = []

# deal the cards
def dealCards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# calculate the total of each hand
def total(turn):
    total = 0
    aces = 0
    face = ['J', 'K', 'Q']

    for card in turn:
        if card in range(2, 11):
            total += card
        elif card in face:
            total += 10
        else:  # card is 'A'
            aces += 1

    for _ in range(aces):
        if total + 11 > 21:
            total += 1
        else:
            total += 11

    return total

# check for winner
def revealDealerHand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

# game loop
for _ in range(2):
    dealCards(dealerHand)
    dealCards(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"You have {playerHand} for a total of {total(playerHand)}")

    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")

    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCards(dealerHand)

    if stayOrHit == '1':
        playerIn = False
    else:
        dealCards(playerHand)

    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if total(playerHand) == 21:
    print(f"\nYOU HAVE {playerHand} FOR A TOTAL OF {total(playerHand)} AND DEALER HAS {dealerHand} FOR A TOTAL OF {total(dealerHand)}")
    print("BLACKJACK! YOU WIN")
elif total(dealerHand) == 21:
    print(f"\nYOU HAVE {playerHand} FOR A TOTAL OF {total(playerHand)} AND DEALER HAS {dealerHand} FOR A TOTAL OF {total(dealerHand)}")
    print("BLACKJACK! DEALER WINS")
elif total(playerHand) > 21:
    print(f"\nYOU HAVE {playerHand} FOR A TOTAL OF {total(playerHand)} AND DEALER HAS {dealerHand} FOR A TOTAL OF {total(dealerHand)}")
    print("YOU BUST! DEALER WINS")
elif total(dealerHand) > 21:
    print(f"\nYOU HAVE {playerHand} FOR A TOTAL OF {total(playerHand)} AND DEALER HAS {dealerHand} FOR A TOTAL OF {total(dealerHand)}")
    print("DEALER BUST! YOU WIN")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYOU HAVE {playerHand} FOR A TOTAL OF {total(playerHand)} AND DEALER HAS {dealerHand} FOR A TOTAL OF {total(dealerHand)}")
    print("DEALER WINS")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\nYOU HAVE {playerHand} FOR A TOTAL OF {total(playerHand)} AND DEALER HAS {dealerHand} FOR A TOTAL OF {total(dealerHand)}")
    print("YOU WIN")
