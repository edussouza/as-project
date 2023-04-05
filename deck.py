from flashcard import flashcard 

class deck:

    list = []
    
    def __init__(self):
        pass

    def addFlashcard(self, flashcard):
        deck.list.append(flashcard)

    def removeFlashcard(self, index):
        deck.list.pop(index-1)

    def showDeck(self):
        print(deck.list)