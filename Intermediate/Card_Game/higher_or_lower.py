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


for suit in suits_tuple:
    for value,rank in enumerate(ranks_tuple):
        card_dic = {"suit":suit, "rank":rank, "value":value + 1}
        cardlist.append(card_dic)

while True:
    shuffle_list = shuffle(cardlist)
    currentcarddict = getcard(shuffle_list)
    print(currentcarddict)
    currentcardrank = currentcarddict["rank"]
    currentcardsuit = currentcarddict["suit"]
    currentcardvalue = currentcarddict["value"]
    print('Starting card is:', currentcardrank + ' of ' + currentcardsuit)


    for cardnumber in range(0,NCARDS):
        num = input("Will the next card will have higher or lower value = ")
        answer = num.lower()

        nextcarddict = getcard(shuffle_list)
        print(nextcarddict)
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

    goagain = input("Do you Want to play Again? = ")
    if goagain == "q":
        break

            











