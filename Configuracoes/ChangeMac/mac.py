import sys
import subprocess
import argparse
import random
import time
import re

interface = "enp1s0"

def alterarMac(interface, novoMac):

    subprocess.call(["sudo","ifconfig",interface,"down"])

    subprocess.call(["sudo","ifconfig",interface,"hw",
    "ether", novoMac])

    subprocess.call(["sudo","ifconfig",interface,"up"])


def getMacAleatorio():
    chars = "123456789abcdef"
    mac = "00"
    for i in range(5):
        mac += ":" + random.choice(chars) + random.choice(chars) 
    return mac

def getMacAtual(intface):
    output = subprocess.check_output(["ifconfig",intface])
    return re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output)).group(0)

def iniciar():
    tempoEspera = 60
    macAtual = getMacAtual(interface)
    print(macAtual)
    macAleatorio = getMacAleatorio()
    alterarMac(interface,macAleatorio)
    novoMac = subprocess.check_output(["ifconfig", interface])
    if (macAleatorio) in str(novoMac):
        print(f"O novo mac é: {macAleatorio}")
    return



