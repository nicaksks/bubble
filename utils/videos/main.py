import os
from time import sleep

from utils.exit import exit
import utils.menu

# Videos
def videos():
    os.system("cls")
    print("Você está na aba de vídeos.")
    print("Caso queira voltar para o início digite: 0\n")

    list_users()
    selected = input("\n-> ")
    list_videos(selected)

# Lista de Usuários
def list_users():

    try:
        folders = os.listdir('assets/videos')
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

# Lista de Vídeos
def list_videos(selected):

    exit(selected)

    try:
        folders = os.listdir(f'assets/videos/{selected}')
        if len(folders) == 0:
            print(f"{selected} não possui nenhum vídeo disponível.")
            sleep(1)
            return videos()
    except:
        print("Esse usuário não existe.")
        sleep(1)
        return videos()

    #Exibir o conteudo dentro das pastas
    for a in folders:
        print(a)

    try:
        videoID = int(input("\n -> "))
        play_video(selected, videoID)
    except ValueError:
        print("Digite um número válido.")
        sleep(1)
        return videos()

# Play Video
def play_video(selected, videoID):

    try:
        print(f"O vídeo {selected.title()} está sendo exibido.")
        os.system(f"start assets/videos/{selected.lower()}/{videoID}.mp4")
        videos()
    except:
        print("Esse vídeo não existe.")
        sleep(1)
    return videos()
