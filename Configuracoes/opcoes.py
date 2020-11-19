from selenium import webdriver
from random import *

proxies = ["169.57.157.148:25", "169.57.157.146:8123",
"169.57.157.148:25","169.57.157.148:80"]

def configurar():
    #proxy = proxies[randint(0,(len(proxies)-1))]
    proxy = '169.57.157.146:8123'
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("start-maximized")
    opcoes.add_argument("--disable-blink-features")
    opcoes.add_argument("--disable-blink-features=AutomationControlled")
    opcoes.add_experimental_option("excludeSwitches", ["enable-automation"])
    opcoes.add_experimental_option('useAutomationExtension', False)
    #opcoes.add_argument('--proxy-server={}'.format(proxy))
    return opcoes