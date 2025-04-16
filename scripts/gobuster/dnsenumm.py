import dns.resolver

def carregar_wordlist(caminho):
    with open(caminho, r) as arquivo:
        return [linha.strip() for linha in arquivo if linha.strip()]


def verificar_subdominio(subdominio):
    try:
        resultado = dns.resolver.resolve(subdominio, "A")
        return [ip.to_text() for ip in resultado]
    except:
        return None


def main():
    dominio = input("digite o dominio principal: ").strip()
    wordlist = input("Caminhos da wordlist (ex: subdomains.txt): ").strip()

    subdominios = carregar_wordlist(wordlist)

    print(f"\n[+] Iniciando enumeração de subdomínios para {domínio}")
    print("=" * 50)

    with open("subdominios_encontrados.txt", "w") as saida:
        for sub in subdominios:
            alvo = f"{sub}.{dominio}"
            resultado = verificar_subdominio(alvo)

            if resultado:
                ips = ', '.join(resultado)
                print(f"[+] Encontrado: {alvo} -> {ips}")
                saida.write(f"{alvo} -> {ips}\n")

    print("\n[✔] Enumeração finalizada. Resultados salvos em 'subdominios_encontrados.txt'.")


if __name__ == "__main__":
    main()