import random
import string

def gerar_senha(comprimento, caracteres):
    caracteres_validos = ''
    if '1' in caracteres:
        caracteres_validos += string.ascii_lowercase
    if '2' in caracteres:
        caracteres_validos += string.ascii_uppercase
    if '3' in caracteres:
        caracteres_validos += string.digits
    if '4' in caracteres:
        caracteres_validos += string.punctuation

    senha = ''.join(random.choice(caracteres_validos) for _ in range(comprimento))
    return senha

try:
    comprimento = int(input("Digite o comprimento da senha desejado: "))
    tipos = input("Digite os tipos de caracteres desejados (1 - minúsculas, 2 - maiúsculas, 3 - dígitos, 4 - símbolos): ")

    senha_gerada = gerar_senha(comprimento, tipos)

    print(f"Senha gerada: {senha_gerada}")

except ValueError:
    print("Entrada inválida! Digite apenas os números mencionados.")