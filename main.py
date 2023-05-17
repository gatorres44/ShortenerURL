import tkinter as tk
from encurtador_url.encurtador_url import EncurtadorURL
from encurtador_url.api import TinyURL

encurtada_url = None

def encurtar_url():
    url = url_entry.get()

    url_encurtada = EncurtadorURL(url)

    api = TinyURL()
    global encurtada_url
    encurtada_url = api.shorten_url(url_encurtada.url)

    if encurtada_url:
        url_encurtada.encurtada_url = encurtada_url
        encurtada_url_label.config(text=f"URL encurtada: {encurtada_url}")
    else:
        encurtada_url_label.config(text="Não foi possível encurtar a URL.")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(encurtada_url)

#inicio da janela gráfica a partir daqui :D
window = tk.Tk()
window.title("Encurtador de URL")
window.minsize(700, 150)
window.resizable(0, 0)

url_label = tk.Label(window, text="URL:",bg='azure')
url_label.pack()

url_entry = tk.Entry(window, width=100)
url_entry.pack()

space = tk.Label(window, text = ' ',bg='azure')
space.pack()

shorten_button = tk.Button(window, border=2, text="Encurtar", bg='LightBlue1', command=encurtar_url)
shorten_button.pack()

encurtada_url_label = tk.Label(window)
encurtada_url_label.pack()

clp = tk.Button(window, border=2 ,text="Copiar para o Clipboard", bg='LightBlue1',
                command=copy_to_clipboard)
clp.pack()

window['background'] = 'azure'
window.mainloop()
