# Encurtador de URL

Este é um projeto em Python que utiliza a API TinyURL para encurtar URLs.

## Estrutura do projeto

- main.py: Arquivo principal que instancia e utiliza a classe TinyURL para encurtar uma URL e exibir o resultado. Utiliza a biblioteca tkinter para instanciar uma janela gráfica para a aplicação.
- encurtador_url/encurtador_url.py: Contém a classe EncurtadorURL que representa a URL original e a URL encurtada.
- encurtador_url/api.py: Contém a classe TinyURL que lida com a interação com a API TinyURL.

## Execução local

1. Instale a versão de Python para o seu SO e em seguida instale a seguinte dependência:

```bash
pip install requests
```

2. Clone este repositório:

```bash
git clone https://github.com/gatorres44/ShortenerURL.git
```
3. Mova para o diretório do projeto:

```bash
cd ShortenerURL/appEncurtadorURL
```
4. execute o arquivo main.py:

```bash
python3 main.py
```

## Aplicação

![Captura de tela da aplicação](https://raw.githubusercontent.com/gatorres44/ShortenerURL/main/Encurtador_de_URL.PNG)
1. Digite ou copie e URL que deseja encurtar no campo "URL";
2. Clique no botão "Encurtar";
3. A URL encurtada será exibida abaixo;
4. Clique no botão "Copiar para o Clipboard" para copiar a URL gerada.