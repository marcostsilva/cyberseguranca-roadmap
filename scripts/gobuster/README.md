### Como rodar este script

1. Criar ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Dê permissão de execução: chmod +x subenum.py
Instale as dependências: pip install colorama

Exemplos de Uso:
Com Gobuster:
# python3 subenum.py -d exemplo.com -t gobuster -w wordlist.txt -o resultados.txt

Com Dirb:
# python3 subenum.py -d exemplo.com -t dirb -o resultados.txt

Ajuda:
# python3 subenum.py --help


