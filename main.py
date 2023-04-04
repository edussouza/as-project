from flashcard import flashcard
from deck import deck

def menu1() -> int:
    opcao = int(input("\nDeseja: \n"
                      "1 - Gerenciar flashcards \n"
                      "2 - Começar estudo \n"
                      "3 - Sair \n"))
    return opcao

def menu2() -> int:
    opcao = int(input("\nEscolha o que deseja fazer: \n"
                  "1 - Adicionar um flashcard \n"
                  "2 - Deletar um flashcard \n"
                  "3 - Apresentar os flashcards \n"
                  "6 - Voltar \n"))
    return opcao    

def showList(list):
    i = 1
    for flashcard in list:
        print(i, repr(flashcard))
        i +=1



myDeck = deck()

while True:    

    opcao = menu1()
    
    if opcao == 1:

        while True:
            
            op = menu2()

            if op == 1:
                newFlashcard = flashcard(pergunta = input("\nDigite a pergunta\n"), resposta = input("Digite a resposta\n"))
                myDeck.includeFlashcard(newFlashcard)
                flashcard.cont += 1

            elif op == 2:
                showList(myDeck.list)
                index = int(input("\nQual flashcard deseja remover: \n"))
                if index <= len(myDeck.list):
                    myDeck.removeFlashcard(index)

            elif op == 3:
                showList(myDeck.list)

            elif op == 6:
                break 

            else: 
                print("Opção invalida")

    elif opcao == 2:
        pass

    elif opcao == 3:
        break

    else:
        print("Por favor, escolha uma opção válida")