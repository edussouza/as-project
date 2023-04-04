class flashcard:

    cont = 0

    def __init__(self, pergunta, resposta):
        self.cont = self.cont
        self.pergunta = pergunta
        self.resposta = resposta

    def __repr__(self):
        return f'({self.pergunta}, {self.resposta})'        

    def getPergunta(self):
        return self.pergunta 
    
    def getResposta(self):
        return self.resposta

    def setPergunta(self, pergunta):
        self.pergunta = pergunta

    def setResposta(self, resposta):
        self.resposta = resposta
    
    def showFlashcard(self):
        print("Pergunta: " + self.pergunta, "\nResposta: " + self.resposta)    