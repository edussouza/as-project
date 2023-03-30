

class flashcard:

    cont = 1

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
        return resposta
    
    def showFlashcard(self):
        print("Pergunta: " + self.pergunta, "\nResposta: " + self.resposta)    
    
def menu():
    str(input("Escolha o que deseja fazer: \n"
                  "1 - Adicionar um flashcard \n"
                  "2 - Deletar um flashcard \n"
                  "3 - Apresentar os flashcards \n"
                  "6 - Sair \n"))
    

def showList(list):
    for flashcard in list:
        print(repr(flashcard))


# opcao = menu()
list = []
menu()

if 1:
    newFlashcard = flashcard(pergunta= input("Escreva a pergunta: \n"), resposta= input("Escreva a resposta: \n"))
    list.append(newFlashcard)
    flashcard.cont = flashcard.cont + 1
    menu()
elif 2:
    list.remove(input)

