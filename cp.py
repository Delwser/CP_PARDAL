import requests
print('Bem vindo ao enumerador de subdominios e arquivos!\n')
print("1TDCPG - Guilherme Vasconcelos")
alvo = input("Coloque o alvo: \n")
lista_enumerados = []
def carregar_lista_arquivos():
    """Carrega a lista de arquivos a serem verificados."""
    return ["main.css", "index.html", "about.html", "contact.html", "styles.css",
            "app.js", "logo.png", "main.js", "index.php", "login.php", "dashboard.php"]

def buscando_urls(alvo):
    with open("subdomains-top1million-5000.txt", "r") as arquivo: #Abrindo o arquivo, e lendo ele.
        urls = arquivo.readlines() #Definindo quais tipos de 
        print("--------------------------")
        print("Subdominios encontrados:")
        for i in range(0, len(urls)):  # Puxando as primeiras 20 linhas
            url = "https://" + urls[i].strip() + "." + alvo  # Adicionando https para fazer requisição
            try:               
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"O subdomínio: {url} status: {response.status_code}")
                    lista_enumerados.append(url)
            except:
                pass
            
        buscando_dir(alvo)

def buscando_dir(alvo):
    print("------Buscando diretórios------")
    with open("dirb.txt", "r") as arquivos:
        urls = arquivos.readlines()
        lista_arquivos = carregar_lista_arquivos()
        for arquivo in lista_arquivos:
            alvo = "https://" + alvo
            for linha in range(0, len(urls)):
                url = alvo + urls[linha].strip()
                response = requests.get(url)
                if response.status_code == 200:
                    print(f"O site {url} retornou status: {response.status_code}")
                    print("--Testando se é Diretório, e se tem arquivo--")
                    base_url = alvo + urls[linha].strip()
                    dir_url = f"{base_url}/{arquivo}"
                    respo = requests.get(dir_url)
                    if respo.status_code == 200:
                        print(f"Arquivo Encontrado: {dir_url} ")
                else:
                    pass


def verificar_arquivos(base_url):
    """Verifica a existência de arquivos no diretório do subdomínio."""
    lista_arquivos = carregar_lista_arquivos()
    for arquivo in lista_arquivos:
        dir_url = f"{base_url}/{arquivo}"
        try:
            respo = requests.get(dir_url)  # Desabilita a verificação do certificado SSL
            if respo.status_code == 200:
                print(f"Arquivo Encontrado: {dir_url}")
        except:
            pass

buscando_urls(alvo)
buscando_dir(alvo)
