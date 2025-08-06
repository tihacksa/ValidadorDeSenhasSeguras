import re


def validar_senha(senha):
    if len(senha) < 16:
        return "Senha muito curta (mínimo 16 caracteres)"
    if not re.search(r"[A-Z]", senha):
        return " A senha precisa de pelos menos uma letra MAIÚSCULA"
    if not re.search(r"\d", senha):
        return " A senha precisa de pelo menos um número"
    if not re.search(r"[!@#$%^&*()_+=\-]", senha):
        return "A senha precisa de pelo menos um símbolo (!@#$...)"
    return "Senha segura"


if __name__ == "__main__":
    while True:
        senha = input("Digite a senha pra validar acesso (ou 'sair'):").strip()
        if senha.lower() == "sair":
            print("Encerrando o validador. Até logo!")
            break

        if senha == "":
            print("Entrada vazia. Por favor, digite uma senha.")
            continue
        resultado = validar_senha(senha)
        print(resultado)
