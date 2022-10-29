import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
        return None
    try:
        with open(path_file, encoding="utf-8") as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    else:
        return data.split('\n')
