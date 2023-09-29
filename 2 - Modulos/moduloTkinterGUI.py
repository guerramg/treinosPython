import tkinter as tk

# CRIANDO A JANELA
janela =  tk.Tk()
janela.geometry('640x480')
janela.title('Gerenciador de Frases')

# CRIANDO FRAME
frame = tk.Frame(janela)
frame.pack(padx=100, pady=10, fill='x', expand=True)

# CRIANDO O LABEL
label = tk.Label(frame, text='Olá Mundo')
label.pack(fill='x', expand=True)

# TEXTO ALTERADO
frase = tk.Label(frame, text='')
frase.pack(fill='x', expand=True)
fraseInput = tk.Entry(frame)
fraseInput.pack(fill='x', expand=True)

# FUNÇÃO PARA TROCA DE FRASE NO LABEL
def trocar():
    frase.config(text=fraseInput.get())

# CRIANDO BOTAO
botao = tk.Button(frame,  text='Alterar', command=trocar)
botao.pack(fill='x', pady=25, expand=True)



# INICIANDO O SISTEMA

janela.mainloop()