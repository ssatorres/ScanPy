#!/bin/bash

echo "INSTALANDO O PIP"
sudo apt-get install python-pip

echo "INSTALANDO DEPENDÊNCIAS"
sudo pip install argparse termcolor subprocess --upgrade

echo "INSTALANDO PROGRAMAS AUXILIARES"
sudo apt-get install -y wpscan uniscan

sudo chmod +x ScanPy.py

