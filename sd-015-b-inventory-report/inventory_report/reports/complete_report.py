from inventory_report.reports.simple_report import SimpleReport
from collections import Counter

# from simple_report import SimpleReport


# teste = [
#     {
#         "id": 1,
#         "nome_do_produto": "MESA",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-05-04",
#         "data_de_validade": "2023-02-09",
#         "numero_de_serie": "FR48",
#         "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#     },
#     {
#         "id": 1,
#         "nome_do_produto": "MESA ESCRITÓRIO",
#         "nome_da_empresa": "Forces of Nature",
#         "data_de_fabricacao": "2022-05-01",
#         "data_de_validade": "2023-02-10",
#         "numero_de_serie": "FR49",
#         "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#     },
#     {
#         "id": 2,
#         "nome_do_produto": "CADEIRA",
#         "nome_da_empresa": "Physicians Total Care, Inc.",
#         "data_de_fabricacao": "2022-05-03",
#         "data_de_validade": "2023-02-08",
#         "numero_de_serie": "FR47",
#         "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#     },
#     {
#         "id": 3,
#         "nome_do_produto": "LUPA",
#         "nome_da_empresa": "Newton Laboratories, Inc.",
#         "data_de_fabricacao": "2022-05-02",
#         "data_de_validade": "2023-02-07",
#         "numero_de_serie": "FR46",
#         "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
#     },
# ]


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(listaDict):
        empresas = []
        itens = "Produtos estocados por empresa:\n"

        for empresa in listaDict:
            empresas.append(empresa["nome_da_empresa"])

        qntProducts = Counter(empresas).most_common()

        for element in qntProducts:
            itens += f"- {element[0]}: {element[1]}\n"

        return f"{SimpleReport.generate(listaDict)}\n{itens}"


# CompleteReport.generate(teste)
