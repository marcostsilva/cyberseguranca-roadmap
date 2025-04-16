#!/usr/bin/env python3
import subprocess
import argparse
from colorama import Fore, Style, init

# Inicializa colorama para cores no terminal
init()

def print_banner():
    """Exibe um banner colorido para o script"""
    banner = f"""
{Fore.GREEN}
  ____        _       ____             _            
 |  _ \      | |     |  _ \           | |           
 | |_) |_   _| |__   | |_) |_ __ _   _| |_ ___ _ __ 
 |  _ <| | | | '_ \  |  _ <| '__| | | | __/ _ \ '__|
 | |_) | |_| | |_) | | |_) | |  | |_| | ||  __/ |   
 |____/ \__,_|_.__/  |____/|_|   \__,_|\__\___|_|   
{Style.RESET_ALL}
"""
    print(banner)

def run_gobuster(domain, wordlist, output_file):
    """Executa o Gobuster para enumeração de subdomínios"""
    print(f"{Fore.BLUE}[*] Executando Gobuster no domínio: {domain}{Style.RESET_ALL}")
    try:
        cmd = f"gobuster dns -d {domain} -w {wordlist} -o {output_file}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"{Fore.GREEN}[+] Gobuster concluído! Resultados salvos em {output_file}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[-] Erro ao executar Gobuster: {e}{Style.RESET_ALL}")

def run_dirb(domain, output_file):
    """Executa o Dirb para enumeração de diretórios"""
    print(f"{Fore.BLUE}[*] Executando Dirb no domínio: {domain}{Style.RESET_ALL}")
    try:
        cmd = f"dirb http://{domain} -o {output_file}"
        subprocess.run(cmd, shell=True, check=True)
        print(f"{Fore.GREEN}[+] Dirb concluído! Resultados salvos em {output_file}{Style.RESET_ALL}")
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[-] Erro ao executar Dirb: {e}{Style.RESET_ALL}")

def main():
    print_banner()
    
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(
        description="Script para automatizar busca de subdomínios com Gobuster ou Dirb",
        epilog="Exemplo de uso: python3 subenum.py -d exemplo.com -t gobuster -w wordlist.txt -o resultados.txt"
    )
    
    parser.add_argument("-d", "--domain", help="Domínio alvo para enumeração")
    parser.add_argument("-t", "--tool", choices=["gobuster", "dirb"], help="Ferramenta a ser utilizada (gobuster/dirb)")
    parser.add_argument("-w", "--wordlist", help="Caminho para o arquivo de wordlist (necessário para Gobuster)")
    parser.add_argument("-o", "--output", default="resultados.txt", help="Arquivo de saída para os resultados")
    
    args = parser.parse_args()
    
    # Verifica os argumentos e executa a ferramenta apropriada
    if args.tool == "gobuster":
        if not args.wordlist:
            print(f"{Fore.RED}[-] Wordlist é necessária para o Gobuster!{Style.RESET_ALL}")
            parser.print_help()
            return
        run_gobuster(args.domain, args.wordlist, args.output)
    elif args.tool == "dirb":
        run_dirb(args.domain, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
