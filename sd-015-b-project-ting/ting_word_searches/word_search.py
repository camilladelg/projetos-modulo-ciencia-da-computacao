def exists_word(word, instance):
    """Aqui irá sua implementação"""
    if len(instance) > 0:
        for inst in instance._data:
            if word not in inst["linhas_do_arquivo"]:
                return []
        # teste1 = []
        #     for i in inst["linhas_do_arquivo"]:
        #         if word.lower() in i.lower():
        #             teste2 = []
        #             teste = {
        #                 "palavra": word,
        #                 "arquivo": inst["nome_do_arquivo"],
        #                 "ocorrencia": teste2.append(
        #                     {"linha": inst["linhas_do_arquivo"].index(i)}
        #                 ),
        #             }
        # teste1.append(teste)
        # return teste1


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
