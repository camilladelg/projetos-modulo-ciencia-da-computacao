from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(dados):
        cnt = Counter()
        datasFabricacao = []
        datasValidade = []
        nomesEmpresa = []
        for dado in dados:
            datasFabricacao.append(dado["data_de_fabricacao"])
            datasValidade.append(dado["data_de_validade"])
            nomesEmpresa.append(dado["nome_da_empresa"])
        for nome in nomesEmpresa:
            cnt[nome] += 1

        menor = sorted(datasFabricacao)
        maior = sorted(datasValidade)
        empresa = sorted(cnt.items(), key=lambda x: x[1], reverse=True)[0][0]

        return (
            f"Data de fabricação mais antiga: {menor[0]}\n"
            f"Data de validade mais próxima: {maior[0]}\n"
            f"Empresa com mais produtos: {empresa}"
        )
