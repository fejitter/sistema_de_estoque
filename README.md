# **README.md — Sistema de Gerenciamento de Estoque**

# Sistema de Gerenciamento de Estoque  
Um sistema simples, robusto e totalmente funcional para controle de estoque utilizando **Python + CSV**, com suporte a múltiplos usuários, login, menus dinâmicos e persistência completa de dados.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Ativo-success?style=for-the-badge)
![License](https://img.shields.io/badge/Licença-Livre-green?style=for-the-badge)
![CSV](https://img.shields.io/badge/Persistência-CSV-orange?style=for-the-badge)

</div>

---

## **Integrantes do Projeto**

Preencha com os nomes e contatos:

| Nome | E-mail | GitHub |
|------|---------|---------|
| Carlos Decker | carlosdecker022@gmail.com | https://github.com/CarlosDecker |
| Felipe Pais | felipegvpais1@gmail.com | https://github.com/fejitter |
| Matheus Souza | matheusc2.as@gmail.com | https://github.com/QuaintMatheus |

---

## **Descrição do Projeto**

Este projeto implementa um **sistema completo de gerenciamento de estoque**, com:

- Cadastro, listagem e edição de produtos  
- Controle de entrada e saída no estoque  
- Sistema de pedidos para clientes  
- Persistência em três arquivos CSV:
  - `usuarios.csv`
  - `produtos.csv`
  - `estoque.csv`
- Login com credencial  
- Menus exclusivos para ADM e Cliente  
- CRUD completo de usuários (ADM)  
- Histórico de pedidos (Clientes)  

O foco é demonstrar **POO**, **organização**, **modularização** e **persistência de dados**.

---

## **Tecnologias Utilizadas**

- 🐍 Python 3.10+
- 📁 Manipulação de arquivos (CSV)
- 🧱 Programação Orientada a Objetos
- 🖥️ Execução via terminal

---

## **Estrutura do Projeto**

```

/AtPrat/
│
├── classes.py          # Todas as classes do sistema
├── persistencia.py     # Funções de leitura e escrita dos CSVs
├── main.py             # Menu principal e fluxo do programa
|
├── produtos.csv        # Armazena dados dos produtos
├── estoque.csv         # Armazena quantidades
└── usuarios.csv        # Armazena usuários e credenciais

````

---

## **Como Executar o Sistema**

### Pré-requisitos

- Python instalado  
  https://www.python.org/downloads/

---

### Baixar o projeto

```bash
git clone https://github.com/fejitter/sistema_de_estoque.git
cd sistema_de_estoque
````

---

### Executar

```bash
python main.py
```

ou

```bash
python3 main.py
```

---

## **Login e Usuários**

Ao iniciar, o sistema solicita a credencial.

Se não existir nenhum usuário, um **ADM padrão** será criado:

```
Credencial: ADM001
Nome: Administrador
Telefone: 0000-0000
```

---

## **Funcionalidades**

### Administrador

* Cadastrar produtos
* Listar produtos
* Adicionar estoque
* Remover estoque
* Listar estoque
* Cadastrar usuário
* Listar usuários
* Editar informações de qualquer usuário
* Excluir usuários
* Logout sem encerrar o programa

---

### Cliente

* Listar produtos
* Criar pedidos
* Finalizar pedidos
* Histórico de compras
* Editar informações pessoais
* Logout

---

## **Possíveis Melhorias Futuras**

* Sistema de autenticação com senha e hash (bcrypt)
* Banco de dados (SQLite)
* Interface gráfica (Tkinter / PyQt)
* API com Flask ou FastAPI
* Logs de operações
* Arquivamento de usuários ao invés de exclusão direta

---

## **Contato**

Dúvidas? Sugestões? Entre em contato com qualquer membro do grupo!
