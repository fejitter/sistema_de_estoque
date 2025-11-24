from classes import *
from persistencia import PersistenciaCSV

# menu

def menu_adm(catalogo, estoque, usuarios, usuario_logado):
    while True:
        print("\n=== MENU ADM ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Adicionar ao estoque")
        print("4 - Remover do estoque")
        print("5 - Mostrar estoque")
        print("6 - Cadastrar usuário")
        print("7 - Listar usuários")
        print("8 - Editar usuário")
        print("9 - Excluir usuário")
        print("0 - Sair")
        op = input("Escolha: ")

        # 1 - Cadastrar produto
        if op == "1":
            codigo = int(input("Código: "))
            if codigo in catalogo:
                print("Código já existe!")
                continue

            nome = input("Nome: ")
            categoria = input("Categoria: ")
            preco = float(input("Preço: "))

            catalogo[codigo] = Produto(codigo, nome, categoria, preco)
            PersistenciaCSV.salvar_produtos(catalogo)
            print("Produto cadastrado!")

        # 2 - Listar produtos
        elif op == "2":
            print("\n=== PRODUTOS ===")
            for p in catalogo.values():
                print(f"{p.codigo} - {p.nome} | R${p.preco}")

        # 3 - Adicionar estoque
        elif op == "3":
            codigo = int(input("Código: "))
            if codigo not in catalogo:
                print("Produto não existe!")
                continue
            qtd = int(input("Quantidade: "))
            estoque.adicionar_produto(codigo, qtd)
            PersistenciaCSV.salvar_estoque(estoque)

        # 4 - Remover estoque
        elif op == "4":
            codigo = int(input("Código: "))
            qtd = int(input("Quantidade: "))
            try:
                estoque.remover_produto(codigo, qtd)
                PersistenciaCSV.salvar_estoque(estoque)
            except Exception as e:
                print("Erro:", e)

        # 5 - Mostrar estoque
        elif op == "5":
            print("\n=== ESTOQUE ===")
            for cod, qtd in estoque.produtos.items():
                print(f"{catalogo[cod].nome}: {qtd}")

        # 6 - Cadastrar usuário
        elif op == "6":
            print("\n=== CADASTRAR USUÁRIO ===")
            cred = input("Credencial: ")

            if cred in usuarios:
                print("Credencial já existe!")
                continue

            nome = input("Nome: ")
            telefone = input("Telefone: ")
            tipo = input("Tipo (adm/cliente): ").lower()

            if tipo == "adm":
                usuarios[cred] = Adm(nome, telefone, cred)
            else:
                usuarios[cred] = Cliente(nome, telefone, cred)

            PersistenciaCSV.salvar_usuarios(usuarios)
            print("Usuário cadastrado!")

        # 7 - Listar usuários
        elif op == "7":
            print("\n=== USUÁRIOS ===")
            for u in usuarios.values():
                tipo = "Administrador" if isinstance(u, Adm) else "Cliente"
                print(f"{u.credencial} | {tipo} | {u.nome} | {u.telefone}")

        # 8 - Editar usuário
        elif op == "8":
            print("\n=== EDITAR USUÁRIO ===")
            cred = input("Credencial do usuário: ")

            if cred not in usuarios:
                print("Usuário não encontrado!")
                continue

            user = usuarios[cred]
            print(f"Editando {user.nome} ({user.credencial})")

            novo_nome = input(f"Novo nome (ENTER para manter): ")
            novo_tel = input(f"Novo telefone (ENTER para manter): ")

            if novo_nome.strip():
                user.nome = novo_nome
            if novo_tel.strip():
                user.telefone = novo_tel

            PersistenciaCSV.salvar_usuarios(usuarios)
            print("Usuário atualizado!")

        # 9 - Excluir usuário
        elif op == "9":
            print("\n=== EXCLUIR USUÁRIO ===")
            cred = input("Credencial do usuário: ")

            if cred not in usuarios:
                print("Usuário não encontrado!")
                continue

            if cred == usuario_logado.credencial:
                print("Você não pode excluir sua própria conta!")
                continue

            confirm = input("Digite 'sim' para confirmar: ").lower()
            if confirm == "sim":
                del usuarios[cred]
                PersistenciaCSV.salvar_usuarios(usuarios)
                print("Usuário excluído!")
            else:
                print("Cancelado.")

        elif op == "0":
            break

        else:
            print("Inválido")


def menu_cliente(cliente, catalogo, estoque, usuarios):
    pedido = Pedido()

    while True:
        print("\n=== MENU CLIENTE ===")
        print("1 - Ver produtos")
        print("2 - Adicionar ao pedido")
        print("3 - Finalizar pedido")
        print("4 - Ver histórico")
        print("5 - Editar meus dados")
        print("0 - Sair")
        op = input("Escolha: ")

        # 1 - Listar produtos
        if op == "1":
            for p in catalogo.values():
                print(f"{p.codigo} - {p.nome} | R${p.preco}")

        # 2 - Adicionar ao pedido
        elif op == "2":
            codigo = int(input("Código: "))
            if codigo not in catalogo:
                print("Não existe!")
                continue
            qtd = int(input("Quantidade: "))
            pedido.adicionar_produto(codigo, qtd)

        # 3 - Fechar pedido
        elif op == "3":
            if not pedido.produtos:
                print("Pedido vazio!")
                continue
            caixa = Caixa(1)
            try:
                total = caixa.fechar_pedido(pedido, estoque, catalogo)
                cliente.historico.append(total)
                PersistenciaCSV.salvar_estoque(estoque)
                pedido = Pedido()
            except Exception as e:
                print("Erro:", e)

        # 4 - Histórico
        elif op == "4":
            print(cliente.exibir_historico())

        # 5 - Editar informações
        elif op == "5":
            novo_nome = input("Novo nome (ENTER pra manter): ")
            novo_tel = input("Novo telefone (ENTER pra manter): ")

            if novo_nome.strip():
                cliente.nome = novo_nome
            if novo_tel.strip():
                cliente.telefone = novo_tel

            PersistenciaCSV.salvar_usuarios(usuarios)
            print("Dados atualizados!")

        elif op == "0":
            break

        else:
            print("Inválido")


# main

if __name__ == "__main__":
    catalogo = PersistenciaCSV.carregar_produtos()
    estoque = Estoque(1)
    PersistenciaCSV.carregar_estoque(estoque)
    usuarios = PersistenciaCSV.carregar_usuarios()

    if not usuarios:
        usuarios["ADM001"] = Adm("Administrador", "0000-0000", "ADM001")
        PersistenciaCSV.salvar_usuarios(usuarios)

    while True:
        print("\n=== SISTEMA DE ESTOQUE ===")
        cred = input("Digite sua credencial (ou 'sair' para encerrar): ")

        if cred.lower() == "sair":
            break

        if cred not in usuarios:
            print("Credencial inválida.")
            continue

        usuario_logado = usuarios[cred]

        # Menu ADM
        if isinstance(usuario_logado, Adm):
            menu_adm(catalogo, estoque, usuarios, usuario_logado)

        # Menu Cliente
        else:
            menu_cliente(usuario_logado, catalogo, estoque, usuarios)

        # Salvar tudo a cada logout
        PersistenciaCSV.salvar_produtos(catalogo)
        PersistenciaCSV.salvar_estoque(estoque)
        PersistenciaCSV.salvar_usuarios(usuarios)

    print("Sistema encerrado.")
