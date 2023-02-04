import urllib.request
import os
from pyunpack import Archive
import shutil
import utils.menu
from time import sleep

def update():

  os.system("cls")
  print("Os arquivos estão sendo baixados. Aguarde alguns minutos.")
  url = "http://localhost:80/assets.rar"
  name = "/assets.rar"
  path = "assets/download"

  createFolder(path)

  urllib.request.urlretrieve(url, path + name)
  print("\nArquivos baixados com sucesso.")

  print("Os arquivos estão sendo extraidos. Aguarde alguns segundos.")
  Archive(path + name).extractall("assets")
  print("Arquivos extraidos com sucesso!")
  deleteFolder(path)
  
  sleep(1)
  utils.menu.start()

def createFolder(path):
  if not os.path.exists(path):
    os.makedirs(path, exist_ok=True)

def deleteFolder(path):
  if os.path.exists(path):
    shutil.rmtree(path)