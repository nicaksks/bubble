import os
from time import sleep

from utils.exit import exit
import utils.menu

# Gifs
def gifs():
    os.system("cls")
    print("Você está na aba de gifs.")
    print("Caso queira voltar para o início digite: 0\n")

    list_users()
    selected = input("\n-> ")
    list_gifs(selected)

# Lista de Usuários
def list_users():
    try:
        folders = os.listdir('assets/gifs')
    except:
        print("É necessário atualizar.")
        sleep(1)
        utils.menu.start()

    if len(folders) == 0:
        print("Não tem nenhum usuário cadastrado.")
        sleep(1)

        selected = "0"
        return exit(selected)

    for users in folders:
        print(". " + users.title())

# Lista de Gifs
def list_gifs(selected):

    exit(selected)

    try:
        folders = os.listdir(f'assets/gifs/{selected}')
        if len(folders) == 0:
            print(f"{selected} não possui nenhum gif disponível.")
            sleep(1)
            return gifs()
    except:
        print("Esse usuário não existe.")
        sleep(1)
        return gifs()

    #Exibir o conteudo dentro das pastas
    for a in folders:
        print(a)

    try:
        gifID = int(input("\n -> "))
        play_gif(selected, gifID)
    except ValueError:
        print("Digite um número válido.")
        sleep(1)
        return gifs()

# Play Gif
def play_gif(selected, gifID):

    try:
        print(f"Gif {selected.title()} está sendo exibido.")
        os.system(f"start assets/gifs/{selected.lower()}/{gifID}.gif")
        gifs()
    except:
        print("Esse gif não existe.")
        sleep(1)
    return gifs()
