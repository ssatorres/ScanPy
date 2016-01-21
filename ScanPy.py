#!/usr/bin/python
# -*- coding: utf-8 -*-

## IMPORTANDO MÓDULOS ##
import argparse
from termcolor import colored
import time
import subprocess

## VARIAVEIS ##
data = "%s" % (time.strftime("%d_%m_%Y"))
hora = "%s" % (time.strftime("%H:%M"))
## INICIANDO PROGRAMA ##
def uso():
    print colored("""
     _______.  ______     ___      .__   __. .______   ____    ____
    /       | /      |   /   \     |  \ |  | |   _  \  \   \  /   /
   |   (----`|  ,----'  /  ^  \    |   \|  | |  |_)  |  \   \/   /
    \   \    |  |      /  /_\  \   |  . `  | |   ___/    \_    _/
.----)   |   |  `----./  _____  \  |  |\   | |  |          |  |
|_______/     \______/__/     \__\ |__| \__| | _|          |__|

                  """, 'green', attrs=['bold'])
    print colored("[!] Script By: Expl0itSec GitHub: github.com/DevIgor", 'green', attrs=['bold'])
    print colored("[*] Uso: ./ScanPy.py --ip [IP DO ALVO] -url [URL DO ALVO]", 'green', attrs=['bold'])

def scan(ip, url):
    print
    print colored("=================[*Iniciando Scan*]=================", 'yellow', attrs=['bold'])
    print colored("Iniciando Teste no Ip: " + ip, 'yellow', attrs=['bold'])
    print colored("Iniciando Teste no Site: " + url, 'yellow', attrs=['bold'])
    print

def menu():
    ip = ''
    url = ''
    nmap = 'sudo nmap -sC -sV -Pn '
    wps = 'sudo wpscan --url '
    param = ' --enumerate u '
    log = ' >> Logs/Log_Scan.%s-%s.log' % (data, hora)
    ##  FAZENDO PARSE DOS ARGUMENTOS ##
    parse = argparse.ArgumentParser(description='ScanPy', add_help=False)
    parse.add_argument('-h', '--help', action=uso())
    parse.add_argument('--ip', help='Informe o IP Alvo.')
    parse.add_argument('-url', help='Informe o Site Alvo')
    args = parse.parse_args()
    ip = args.ip
    url = args.url

    scan(ip, url)

    ## INICIANDO SCANNER ##
    scanner = subprocess.call(nmap + ip + log, shell=True,)
    uniscan = subprocess.call(wps + url + param + log, shell=True)
    print colored("====================================================================", 'blue', attrs=['bold'])
    print colored("[+] LOG SALVO EM%s", 'blue', attrs=['bold']) % log
    print colored("====================================================================\n", 'blue', attrs=['bold'])
    print colored("*/*/*/*/*/*/*/FINALIZADO/*/*/*/*/*/*/*/*/*\n", 'red', attrs=['bold'])
menu()