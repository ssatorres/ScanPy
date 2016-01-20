#!/bin/bash

echo "INSTALANDO O PIP"
sudo apt-get install python-pip

echo "INSTALANDO DEPENDÊNCIAS"
sudo pip install argparse termcolor subprocess --upgrade

sudo chmod +x ScanPy.py

