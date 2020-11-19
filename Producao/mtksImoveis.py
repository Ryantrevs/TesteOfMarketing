from Configuracoes import navegador
from Configuracoes.ChangeMac import mac
import time

def main():
    href = open('./data/BotoesMTKS.txt', 'r', encoding='utf8')
    listaBut = href.readlines()
    links = open('./data/LinksDeAcesso.txt', 'r', encoding='utf8')
    listaLink = links.readlines()
    nav = navegador.confNav()
    mac.iniciar()
    navegador.digitarSite(nav,listaLink[0])
    pesquisa = navegador.elemento(nav,listaBut[0])
    navegador.digitar(pesquisa,"alugar apartamento temporada Urca")
    pesquisar = navegador.elemento(nav,listaBut[1])
    navegador.click(pesquisar)
    site = navegador.google(nav)
    print(site)
    navegador.click(site)
    #teste = navegador.elemento(nav,listaBut[0])
    #navegador.click(teste)
    #print(teste)
    time.sleep(10)
    
