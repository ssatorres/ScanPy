#!/usr/bin/python
# -*- coding: utf-8 -*-

## IMPORTANDO MÓDULOS ##
import argparse
from termcolor import colored
import os
import time
import subprocess

## VARIAVEIS ##
data = "%s" % (time.strftime("%Y_%m_%d"))
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
    print colored("[*] Uso: ./ScanPy.py --ip [ENDEREÇO ALVO (SITE ou MÁQUINA)]", 'green', attrs=['bold'])

def scan(ip):
    print
    print colored("=================[*Iniciando Scan*]=================", 'yellow', attrs=['bold'])
    print colored("Iniciando Teste no Ip: " + ip, 'yellow', attrs=['bold'])
    print

def menu():
    ip = ''
    nmap = 'sudo nmap -sC -sV -Pn '
    log = ' >> Log_Scan.%s.log' % (data)
    ##  FAZENDO PARSE DOS ARGUMENTOS ##
    parse = argparse.ArgumentParser(description='ScanPy', add_help=False)
    parse.add_argument('-h', '--help', action=uso())
    parse.add_argument('--ip', help='Informe o IP Alvo.')
    args = parse.parse_args()
    ip = args.ip

    scan(ip)

    ## INICIANDO SCANNER ##
    scanner = subprocess.call(nmap + ip + log, shell=True,)

    print colored("*/*/*/*/*/*/*/FINALIZADO/*/*/*/*/*/*/*/*/*", 'red', attrs=['bold'])
menu()