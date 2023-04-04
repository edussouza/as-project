from flashcard import flashcard

class box:

    def __init__(self, level):
        self.level = level
        self.flashcards = []

    def includeFlashcard(self, flashcard):
        self.flashcards.append(flashcard)

    def removeFlashcard(self, flashcard):
        self.flashcards.pop(flashcard)    
    