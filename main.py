import random
import string
import tkinter as tk
from tkinter import messagebox


def gerar_senha(comprimento: int, minusculas: bool, maiusculas: bool, digitos: bool, simbolos: bool) -> str:
    """
    Gera uma senha aleatória com os critérios especificados.

    Args:
        comprimento (int): Tamanho da senha a ser gerada.
        minusculas (bool): Se True, inclui letras minúsculas.
        maiusculas (bool): Se True, inclui letras maiúsculas.
        digitos (bool): Se True, inclui dígitos numéricos.
        simbolos (bool): Se True, inclui caracteres especiais.

    Returns:
        str: Senha gerada ou string vazia se nenhum critério for selecionado.
    """
    validos = ''

    if minusculas:
        validos += string.ascii_lowercase
    if maiusculas:
        validos += string.ascii_uppercase
    if digitos:
        validos += string.digits
    if simbolos:
        validos += string.punctuation

    if not validos:
        messagebox.showerror(
            "Erro", "Não foi selecionado nenhum tipo de caractere")
        return ""

    return ''.join(random.choice(validos) for _ in range(comprimento))


def validar_entrada(event: tk.EventType) -> str:
    """
    Restringe a entrada do usuário para apenas números no campo de comprimento.

    Args:
        event (tk.EventType): Evento de clique da tecla.

    Returns:
        str: Retorna "break" para impedir a entrada de caracteres não numéricos.
    """
    if not event.char.isdigit() and event.keysym != "BackSpace":
        return "break"


def on_click() -> None:
    """
    Captura os inputs do usuário e gera a senha conforme os critérios selecionados.
    """
    try:
        senha = gerar_senha(
            int(entry_comprimento.get()), bool_minusculas.get(), bool_maiusculas.get(), bool_digitos.get(), bool_simbolos.get())
        if senha:
            entry_senha.delete(0, tk.END)
            entry_senha.insert(0, senha)
    except ValueError:
        messagebox.showerror(
            "Erro", "Digite um número válido para o comprimento.")


def main() -> None:
    """
    Configura e exibe a interface gráfica do gerador de senhas.
    """
    global entry_comprimento, entry_senha, bool_minusculas, bool_maiusculas, bool_digitos, bool_simbolos

    gui = tk.Tk()
    gui.title("PasswordGenerator - Gerador de Senhas")
    gui.geometry("400x200")
    gui.resizable(False, False)

    top = tk.Frame(gui)
    top.pack(pady=10)

    label_comprimento = tk.Label(top, text="Comprimento da senha:")
    label_comprimento.pack(side=tk.LEFT, padx=5)

    entry_comprimento = tk.Entry(top, width=5)
    entry_comprimento.pack(side=tk.LEFT)
    entry_comprimento.bind("<KeyPress>", validar_entrada)

    opcoes = tk.Frame(gui)
    opcoes.pack(pady=10)

    bool_minusculas = tk.BooleanVar()
    bool_maiusculas = tk.BooleanVar()
    bool_digitos = tk.BooleanVar()
    bool_simbolos = tk.BooleanVar()

    tk.Checkbutton(
        opcoes, text="Minúsculas", variable=bool_minusculas).grid(row=0, column=0, padx=5, pady=2)
    tk.Checkbutton(
        opcoes, text="Maiúsculas", variable=bool_maiusculas).grid(row=0, column=1, padx=5, pady=2)
    tk.Checkbutton(
        opcoes, text="Dígitos", variable=bool_digitos).grid(row=0, column=2, padx=5, pady=2)
    tk.Checkbutton(
        opcoes, text="Símbolos", variable=bool_simbolos).grid(row=0, column=3, padx=5, pady=2)

    btn = tk.Button(gui, text="Gerar Senha", command=on_click)
    btn.pack(pady=10)

    entry_senha = tk.Entry(gui, width=40, justify='center')
    entry_senha.pack(pady=5)

    gui.mainloop()


if __name__ == "__main__":
    main()
