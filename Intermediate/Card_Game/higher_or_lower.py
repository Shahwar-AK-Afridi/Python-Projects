import random

ranks_tuple = ("Ace","1","2","3","4","5","6","7","8","9","10","Jack","King","Queen")
suits_tuple = ("Spades","Heart","Club","Diamonds")

card_dic = {}
cardlist = []
score = 50
NCARDS = 8

def getcard(decklistin:list)->dict:
    """Sending the top-most card in the deck"""
    this_card = decklistin.pop()
    return this_card

def shuffle(decklistin:list)->list:
    """shuffling the deck of cards"""
    decklistout = decklistin.copy()
    random.shuffle(decklistout)
    return decklistout

print('Welcome to Higher or Lower.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')

for suit in suits_tuple:
    for value,rank in enumerate(ranks_tuple):
        card_dic = {"suit":suit, "rank":rank, "value":value + 1}
        cardlist.append(card_dic)

while True:  #To play multiple games
    shuffle_list = shuffle(cardlist)
    currentcarddict = getcard(shuffle_list)
    currentcardrank = currentcarddict["rank"]
    currentcardsuit = currentcarddict["suit"]
    currentcardvalue = currentcarddict["value"]
    print('Starting card is:', currentcardrank + ' of ' + currentcardsuit)


    for cardnumber in range(0,NCARDS):
        num = input("Will the next card be higher or lower than the " + currentcardrank + " of " + currentcardsuit + "? (enter h or l):")
        answer = num.lower()

        nextcarddict = getcard(shuffle_list)
        nextcardrank = nextcarddict["rank"]
        nextcardsuit = nextcarddict["suit"]
        nextcardvalue = nextcarddict["value"]

        if answer == "h":
            if nextcardvalue > currentcardvalue:
                print('You got it right, it was higher')
                score += 20
            else:
                print('Sorry, it was not higher')
                score -= 15
        elif answer == "l":
            if nextcardvalue < currentcardvalue:
                print('You got it right, it was lower')
                score += 20
            else:
                print('Sorry, it was not lower')
                score -= 15

        print("Your Score is = ", score)

    goagain = input("Do you Want to play Again?, press c to continue, or q to quit ")
    if goagain == "c":
        continue
    elif goagain == "q":
        break

            











