import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    if len(instance) > 0:
        for i in instance._data:
            if i["nome_do_arquivo"] == path_file:
                return None

    file = txt_importer(path_file)
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(file_info)
    print(instance._data[-1], file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    if len(instance) <= 0:
        print("Não há elementos", file=sys.stdout)
        return None
    file = instance.dequeue()
    print(
        f"Arquivo {file['nome_do_arquivo']} removido com sucesso",
        file=sys.stdout,
    )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position < 0 or position >= instance.__len__():
        print('Posição inválida', file=sys.stderr)
        return None
    print(instance.search(position), file=sys.stdout)
