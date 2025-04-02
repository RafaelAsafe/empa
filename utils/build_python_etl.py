import nbformat
from rich import print

nb_path = 'E:\GIT\glue-pipe-cookiecutter\develop\main_dev.ipynb'
nb_version = 5

teste_noteboook = nbformat.read('E:\GIT\glue-pipe-cookiecutter\develop\main_dev.ipynb',as_version=nbformat.NO_CONVERT)


print(teste_noteboook.cells)








