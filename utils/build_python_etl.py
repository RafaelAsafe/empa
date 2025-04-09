import nbformat
from nbconvert import PythonExporter
from rich import print
from copy import deepcopy

python_exporter = PythonExporter()

nb_path = 'E:\GIT\glue-pipe-cookiecutter\develop\main_dev.ipynb'
dest_path = 'teste.p'
nb_version = 5

teste_notebook = nbformat.read('E:\GIT\glue-pipe-cookiecutter\develop\main_dev.ipynb',as_version=4)

filtered_notebook = deepcopy(teste_notebook)

#list(map(lambda cell: cell.get("metadata", {}).get("tags", []), nb.cells)) entender essa implementação
# (cell.get("metadata", {}).get("tags", []) for cell in nb.cells) enteder generators

cells_filteres = [cell for cell in teste_notebook.cells if cell['metadata'].get('tags')]
filtered_notebook.cells= cells_filteres

(body, resources) = python_exporter.from_notebook_node(filtered_notebook)

print(body)

with open(dest_path,"w",encoding="utf-8") as f:
        f.write(body)






