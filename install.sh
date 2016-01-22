#!/bin/bash

echo "ADICIONANDO REPO DO KALI"
apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6
echo '# Kali linux repositories | Adicionado Por ScanPy\ndeb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list

echo "INSTALANDO O PIP"
sudo apt-get install python-pip

echo "INSTALANDO DEPENDÊNCIAS"
sudo pip install argparse termcolor subprocess --upgrade

echo "INSTALANDO PROGRAMAS AUXILIARES"
sudo apt-get install -y wpscan uniscan

sudo chmod +x ScanPy.py

