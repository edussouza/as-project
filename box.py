from flashcard import flashcard

class box:

    def __init__(self, level):
        self.level = level
        self.list = []

    def addFlashcard(self, flashcard):
        self.list.append(flashcard)

    def removeFlashcard(self, flashcard):
        self.list.pop(flashcard)    

    # def moveFlashcard(self, flashcard, correct):
