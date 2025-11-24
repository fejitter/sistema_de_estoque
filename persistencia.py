import csv
from classes import Produto, Adm, Cliente


class PersistenciaCSV:

    # produtos

    @staticmethod
    def salvar_produtos(catalogo, caminho="produtos.csv"):
        with open(caminho, "w", newline="", encoding="utf-8") as arq:
            writer = csv.writer(arq)
            writer.writerow(["codigo", "nome", "categoria", "preco"])
            for p in catalogo.values():
                writer.writerow([p.codigo, p.nome, p.categoria, p.preco])

    @staticmethod
    def carregar_produtos(caminho="produtos.csv"):
        catalogo = {}
        try:
            with open(caminho, "r", encoding="utf-8") as arq:
                reader = csv.DictReader(arq)
                for linha in reader:
                    p = Produto(
                        int(linha["codigo"]),
                        linha["nome"],
                        linha["categoria"],
                        float(linha["preco"])
                    )
                    catalogo[p.codigo] = p
        except FileNotFoundError:
            pass
        return catalogo

    # estoque

    @staticmethod
    def salvar_estoque(estoque, caminho="estoque.csv"):
        with open(caminho, "w", newline="", encoding="utf-8") as arq:
            writer = csv.writer(arq)
            writer.writerow(["codigo_produto", "quantidade"])
            for codigo, qtd in estoque.produtos.items():
                writer.writerow([codigo, qtd])

    @staticmethod
    def carregar_estoque(estoque, caminho="estoque.csv"):
        try:
            with open(caminho, "r", encoding="utf-8") as arq:
                reader = csv.DictReader(arq)
                for linha in reader:
                    estoque.produtos[int(linha["codigo_produto"])] = int(linha["quantidade"])
        except FileNotFoundError:
            pass

    # users

    @staticmethod
    def salvar_usuarios(usuarios, caminho="usuarios.csv"):
        with open(caminho, "w", newline="", encoding="utf-8") as arq:
            writer = csv.writer(arq)
            writer.writerow(["credencial", "tipo", "nome", "telefone"])
            for u in usuarios.values():
                tipo = "adm" if isinstance(u, Adm) else "cliente"
                writer.writerow([u.credencial, tipo, u.nome, u.telefone])

    @staticmethod
    def carregar_usuarios(caminho="usuarios.csv"):
        usuarios = {}
        try:
            with open(caminho, "r", encoding="utf-8") as arq:
                reader = csv.DictReader(arq)
                for linha in reader:
                    cred = linha["credencial"]
                    nome = linha["nome"]
                    telefone = linha["telefone"]
                    tipo = linha["tipo"]

                    if tipo == "adm":
                        usuarios[cred] = Adm(nome, telefone, cred)
                    else:
                        usuarios[cred] = Cliente(nome, telefone, cred)

        except FileNotFoundError:
            pass
        return usuarios
