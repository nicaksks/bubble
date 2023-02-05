import os
from time import sleep

from utils.exit import exit
from playsound import playsound
import utils.menu

# Audios
def audios():
    os.system("cls")
    print("Você está na aba áudios.")
    print("Caso queira voltar para o início digite: 0\n")

    list_users()
    selected = input("\n-> ")
    list_audios(selected)

# Lista de Usuários
def list_users():
    try:
        folders = os.listdir('assets/audios')
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

# Lista de Áudios
def list_audios(selected):

    exit(selected)

    try:
        folders = os.listdir(f'assets/audios/{selected}')
        if len(folders) == 0:
            print(f"{selected} não possui nenhum áudio disponível.")
            sleep(1)
            return audios()
    except:
        print("Esse usuário não existe.")
        sleep(1)
        return audios()

    #Exibir o conteudo dentro das pastas
    for a in folders:
        print(a)

    try:
        audioID = int(input("\n -> "))
        play_audio(selected, audioID)
    except ValueError:
        print("Digite um número válido.")
        sleep(1)
        return audios()

# Play Audio
def play_audio(selected, audioID):

    try:
        print(f"Está tocando o áudio de {selected.title()}")
        playsound(f"assets/audios/{selected.lower()}/{audioID}.wav")
        audios()
    except:
        print("Esse áudio não existe.")
        sleep(1)
    return audios()
