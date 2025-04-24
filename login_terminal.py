import os

ARQUIVO_USUARIOS = 'usuarios.txt'


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def carregar_usuarios():
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'r') as f:
            for linha in f:
                usuario, senha = linha.strip().split(',')
                usuarios[usuario] = senha
    return usuarios


def salvar_usuario(usuario, senha):
    with open(ARQUIVO_USUARIOS, 'a') as f:
        f.write(f"{usuario},{senha}\n")


def login():
    limpar_tela()
    print("=== LOGIN ===")
    usuarios = carregar_usuarios()
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"✅ Login bem-sucedido. Bem-vindo, {usuario}!")
    else:
        print("❌ Usuário ou senha incorretos.")
    input("\nPressione Enter para continuar...")


def cadastro():
    limpar_tela()
    print("=== CADASTRO ===")
    usuarios = carregar_usuarios()
    usuario = input("Novo usuário: ")

    if usuario in usuarios:
        print("❌ Usuário já existe!")
    else:
        senha = input("Nova senha: ")
        salvar_usuario(usuario, senha)
        print("✅ Cadastro realizado com sucesso!")
    input("\nPressione Enter para continuar...")


def menu():
    while True:
        limpar_tela()
        print("=== SISTEMA DE LOGIN ===")
        print("[1] Login")
        print("[2] Cadastro")
        print("[3] Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            login()
        elif opcao == '2':
            cadastro()
        elif opcao == '3':
            print("👋 Saindo...")
            break
        else:
            print("Opção inválida!")
            input("Pressione Enter para tentar novamente...")


if __name__ == "__main__":
    menu()
