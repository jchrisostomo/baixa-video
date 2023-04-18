import tkinter
import customtkinter
from pytube import YouTube

def baixarVideo():
    try:
        ytEndereco = campoEndereco.get()
        ytObjeto = YouTube(ytEndereco, on_progress_callback=emProgresso)
        video = ytObjeto.streams.get_highest_resolution()

        titulo.configure(text=ytObjeto.title, text_color="white")
        downloadConcluido.configure(text="")
        video.download()
        downloadConcluido.configure(text="Download concluído!")
    except:
        downloadConcluido.configure(text="Endereço inválido.", text_color="DarkRed")

def emProgresso(stream, chunk, bytes_remaining):
    tamanho_total = stream.filesize
    bytes_baixados = tamanho_total - bytes_remaining
    percentual_progresso = bytes_baixados / tamanho_total * 100
    print(percentual_progresso)
    percent = str(int(percentual_progresso))
    progresso.configure(text=percent + "%")
    progresso.update()

    barraProgresso.set(float(percentual_progresso) / 100)

# Configuração
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# Aplicativo
aplicativo = customtkinter.CTk()
aplicativo.geometry("720x200")
aplicativo.title("Baixa Vídeo")

# Elementos da interface
titulo = customtkinter.CTkLabel(aplicativo, text="Cole o endereço do vídeo (CTRL+V) e depois clique em baixar:")
titulo.pack(padx=10, pady=10)

# Entrada do endereco do video
link = tkinter.StringVar()
campoEndereco = customtkinter.CTkEntry(aplicativo, width=600, height=30, textvariable=link)
campoEndereco.pack()

# Progresso do download
barraProgresso = customtkinter.CTkProgressBar(aplicativo, width=400)
barraProgresso.set(0.0)
barraProgresso.pack(padx=10, pady=10)

progresso  = customtkinter.CTkLabel(aplicativo, text="0%")
progresso.pack()



# Botao de baixar
baixar = customtkinter.CTkButton(aplicativo, text="Baixar", command=baixarVideo)
baixar.pack(padx=10, pady=10)

# Download concluído
downloadConcluido = customtkinter.CTkLabel(aplicativo, text="")
downloadConcluido.pack(padx=5, pady=5)

# Executar aplicativo
aplicativo.mainloop()