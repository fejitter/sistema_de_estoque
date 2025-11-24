class Produto:
    def __init__(self, codigo, nome, categoria, preco):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco

    def __str__(self):
        return f"{self.codigo} | {self.nome} ({self.categoria}) R${self.preco:.2f}"

class Estoque:
    def __init__(self, codigo_interno):
        self.codigo_interno = codigo_interno
        self.produtos = {}

    def adicionar_produto(self, codigo_produto, quantidade):
        self.produtos[codigo_produto] = self.produtos.get(codigo_produto, 0) + quantidade

    def remover_produto(self, codigo_produto, quantidade):
        if codigo_produto not in self.produtos:
            raise Exception("Produto não existe no estoque")

        if self.produtos[codigo_produto] < quantidade:
            raise Exception("Quantidade insuficiente no estoque")

        self.produtos[codigo_produto] -= quantidade

        if self.produtos[codigo_produto] == 0:
            del self.produtos[codigo_produto]

class Pedido:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, quantidade):
        self.produtos[codigo] = self.produtos.get(codigo, 0) + quantidade

    def calcular_total(self, catalogo):
        total = 0
        for codigo, quantidade in self.produtos.items():
            produto = catalogo[codigo]
            total += produto.preco * quantidade
        return total

class Usuario:
    def __init__(self, nome, telefone, credencial):
        self.nome = nome
        self.telefone = telefone
        self.credencial = credencial

class Cliente(Usuario):
    def __init__(self, nome, telefone, credencial):
        super().__init__(nome, telefone, credencial)
        self.historico = []

    def exibir_historico(self):
        if not self.historico:
            return "Nenhum pedido realizado."
        texto = "Histórico:\n"
        for i, total in enumerate(self.historico, start=1):
            texto += f"Pedido {i}: R${total:.2f}\n"
        return texto

class Adm(Usuario):
    pass

class Caixa:
    def __init__(self, id_caixa):
        self.id_caixa = id_caixa

    def fechar_pedido(self, pedido, estoque, catalogo):
        for codigo, quantidade in pedido.produtos.items():
            estoque.remover_produto(codigo, quantidade)

        total = pedido.calcular_total(catalogo)
        print(f"Pedido fechado no Caixa {self.id_caixa}. Total: R${total:.2f}")
        return total
