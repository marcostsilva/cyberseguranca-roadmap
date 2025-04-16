# Mudando para uma biblioteca mais robusta com suporte a Unicode: ReportLab

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

output_path = "/mnt/data/Relatorio_Tecnico_Pentest_DVWA.pdf"
c = canvas.Canvas(output_path, pagesize=A4)
width, height = A4

def draw_title(text, y_offset):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2 * cm, y_offset, text)
    return y_offset - 1 * cm

def draw_paragraph(text, y_offset, font_size=11):
    c.setFont("Helvetica", font_size)
    for line in text.split("\n"):
        c.drawString(2 * cm, y_offset, line.strip())
        y_offset -= 0.6 * cm
    return y_offset - 0.4 * cm

y = height - 2 * cm

# Cabeçalho
c.setFont("Helvetica-Bold", 16)
c.drawCentredString(width / 2, y, "Relatório Técnico - Pentest Simulado em DVWA")
y -= 2 * cm

# Seções
y = draw_title("Informações do Projeto", y)
info = """Autor: Marcos Teodoro da Silva
Data: 16/04/2025
Ambiente: Lab Virtual
Alvo: DVWA
Objetivo: Simular exploração de vulnerabilidades web"""
y = draw_paragraph(info, y)

sections = {
    "1. Reconhecimento": """
IP do alvo: 192.168.0.100
Scanner de portas: nmap -sV -p- 192.168.0.100
Serviços encontrados:
- HTTP 80 (Apache)
- MySQL 3306
""",
    "2. Enumeração": """
- Fuzzing de diretórios com dirb
- Login padrão testado com sucesso: admin:password
- Vulnerabilidade detectada: SQL Injection
""",
    "3. Exploração": """
Ferramenta: sqlmap
Comando:
sqlmap -u "http://192.168.0.100/login.php" --data="user=admin&pass=123" --dump
Dump de tabela 'users' com 5 registros
""",
    "4. Pós-Exploração": """
- Acesso à conta administrativa
- Coleta de informações sensíveis (simulado)
- Verificação de logs de auditoria
""",
    "5. Recomendações": """
- Implementar validação de entrada (Prepared Statements)
- Atualizar DVWA para versão mais recente
- Restringir acesso ao banco de dados
""",
    "6. Sumário Executivo": """
Um teste de invasão controlado foi conduzido no ambiente DVWA com o objetivo de identificar vulnerabilidades comuns em aplicações web. Durante o teste, foi identificada uma falha de SQL Injection que permitiu acesso não autorizado a dados sensíveis. Medidas corretivas foram sugeridas para mitigar os riscos.
"""
}

for title, body in sections.items():
    y = draw_title(title, y)
    y = draw_paragraph(body.strip(), y)
    if y < 4 * cm:
        c.showPage()
        y = height - 2 * cm

c.save()
output_path