"""When the game starts all of the cards are all face down in rows and columns. You click on a card to select it and it turns over to show the suit and rank (value). 
Then you click another card to select it and it also turns face up.
If the two cards match (have the same rank and value) then the cards stay facing up. 
Otherwise they both turn down and you take another turn. 
You win when you have found all of the matches. 
The game keeps track of the total time it took you to find all of the matches."""

class Card():

    suit_names = ["Clubs", "Spades", "Diamond", "Hearts"]
    rank_names = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit = "0", rank = "0"):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        representation = "{} of {}".format(self.rank_names[self.rank], self.suit_names[self.suit])
        return representation

class Deck():

    def __init__(self):
        self.card_list = []   # It stotes the objects of class "Card"

        for i in range(len(Card.suit_names)):
            for j in range(len(Card.rank_names)):
                self.card_list.append(Card(i, j))  #This is called composition

    def __str__(self):
        lst = []
        for card in self.card_list:
            lst.append(card.__str__())
            string = ",".join(lst)
        return string
    

def main():
    my_deck = Deck()
    return my_deck

if __name__ == "__main__":
    print(main())
    
