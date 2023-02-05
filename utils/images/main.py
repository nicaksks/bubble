import os
from time import sleep

from utils.exit import exit
import utils.menu

# images
def images():
    os.system("cls")
    print("Você está na aba de images.")
    print("Caso queira voltar para o início digite: 0\n")

    list_users()
    selected = input("\n-> ")
    list_images(selected)

# Lista de Usuários
def list_users():

    try:
        folders = os.listdir('assets/images')
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

# Lista de Images
def list_images(selected):

    exit(selected)

    try:
        folders = os.listdir(f'assets/images/{selected}')
        if len(folders) == 0:
            print(f"{selected} não possui nenhum imagem disponível.")
            sleep(1)
            return images()
    except:
        print("Esse usuário não existe.")
        sleep(1)
        return images()

    #Exibir o conteudo dentro das pastas
    for a in folders:
        print(a)

    try:
        imageID = int(input("\n -> "))
        play_images(selected, imageID)
    except ValueError:
        print("Digite um número válido.")
        sleep(1)
        return images()

# Display Image
def play_images(selected, imageID):

    if os.path.exists(f"assets/images/{selected.lower()}/{imageID}.png"):
        print(f"{selected.title()} está sendo exibido.")
        os.system(f"start assets/images/{selected.lower()}/{imageID}.png")
        return images()
    else:
        print('Esse Imagem não existe.')
        sleep(1)
        return images()