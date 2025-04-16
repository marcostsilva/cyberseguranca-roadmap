import dns.resolver  # Importa a biblioteca para realizar consultas DNS

# Lista de tipos de registros DNS para consultar
tipos = ["A", "MX", "NS", "TXT"]

def consultar_dns(dominio):
    # Abre ou cria o arquivo "resultado_dns.txt" em modo de escrita
    with open("resultado_dns.txt", "w") as arquivo:
        # Escreve um título no arquivo
        arquivo.write(f"Consultas DNS para o domínio: {dominio}\n")
        arquivo.write("=" * 50 + "\n")

        for tipo in tipos:
            # Para cada tipo de registro, exibe uma mensagem informando qual tipo está sendo consultado
            arquivo.write(f"\n[+] Consultando registro {tipo} para: {dominio}\n")
            print(f"\n[+] Consultando registro {tipo} para: {dominio}")  # Exibe no terminal

            try:
                # Tenta realizar a consulta DNS para o domínio e o tipo de registro
                respostas = dns.resolver.resolve(dominio, tipo)

                # Percorre todas as respostas recebidas e escreve no arquivo
                for r in respostas:
                    resultado = r.to_text()  # Converte o registro para texto (IP, servidor, etc.)
                    arquivo.write(f"  - {resultado}\n")
                    print(f"  - {resultado}")  # Exibe no terminal

            except dns.resolver.NoAnswer:
                # Se não houver resposta para esse tipo de registro, registra no arquivo
                arquivo.write("  [!] Nenhuma resposta para esse tipo de registro.\n")
                print("  [!] Nenhuma resposta para esse tipo de registro.")  # Exibe no terminal

            except dns.resolver.NXDOMAIN:
                # Se o domínio não existir, escreve isso no arquivo e para as consultas
                arquivo.write("  [!] Domínio não existe.\n")
                print("  [!] Domínio não existe.")  # Exibe no terminal
                break

            except dns.exception.Timeout:
                # Se a consulta DNS expirar, registra a falha no arquivo
                arquivo.write("  [!] Tempo esgotado na consulta.\n")
                print("  [!] Tempo esgotado na consulta.")  # Exibe no terminal

            except Exception as e:
                # Captura qualquer outro erro e escreve no arquivo
                arquivo.write(f"  [!] Erro: {e}\n")
                print(f"  [!] Erro: {e}")  # Exibe no terminal

        # Após as consultas, escreve um rodapé no arquivo
        arquivo.write("=" * 50 + "\n")
        arquivo.write(f"Consulta realizada em: {dominio}\n")
        arquivo.write("=" * 50 + "\n")

if __name__ == "__main__":
    # Pede para o usuário digitar o domínio
    dominio = input("Digite o domínio (ex: google.com): ").strip()
    # Chama a função de consulta DNS
    consultar_dns(dominio)
