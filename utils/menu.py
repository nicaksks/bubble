from utils.images.main import images
from utils.gifs.main import gifs
from utils.videos.main import videos
from utils.audios.main import audios
from utils.update.main import update

import os
from time import sleep

def start():
    os.system("cls")
    print("Bem-vindo(a) ao CLI das Bolhas.")
    print("Escolhe uma opção para continuar.")
    print("1 - Imagens \n2 - Gifs \n3 - vídeos \n4 - Áudios \n\nCaso queira fazer atualizações nos arquivo digite: 5")

    selected = int(input("-> "))
    mode(selected)


def mode(selected):

    valid_options = [1, 2, 3, 4, 5]

    if selected not in valid_options:
        print("Digite uma opção válida.")
        sleep(1)
        start()

    options = [images, gifs, videos, audios, update]
    options[selected - 1]()
