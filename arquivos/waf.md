# 🔐 O que é ModSecurity?

**ModSecurity** é um **Web Application Firewall (WAF)** de código aberto usado para proteger aplicações web contra ataques comuns, como:

- SQL Injection
- Cross-Site Scripting (XSS)
- Remote File Inclusion
- Directory Traversal
- Ataques de força bruta e varredura automatizada

Ele funciona como um **módulo adicional** para servidores web como:

- Apache HTTP Server
- NGINX (com suporte adicional via ModSecurity-nginx connector)
- IIS (Internet Information Services da Microsoft)

---

## 🧰 Funcionalidades Principais

- **Análise e filtragem de requisições HTTP** (GET, POST, etc.)
- **Bloqueio de requisições maliciosas** com base em regras personalizadas
- **Registro detalhado** de acessos e tentativas de ataque
- Suporte ao **OWASP Core Rule Set (CRS)** — um conjunto de regras padrão de segurança

---

## 🔍 Como Funciona?

1. Intercepta todas as requisições que chegam ao servidor web.
2. Analisa cabeçalhos, corpo da requisição, parâmetros e cookies.
3. Verifica se há comportamentos maliciosos com base em regras.
4. Executa uma ação:
   - Permitir
   - Bloquear
   - Registrar
   - Redirecionar

---

## 🛠️ Modo de Operação

- `DetectionOnly`: Apenas monitora e registra eventos suspeitos, sem bloquear.
- `On`: Ativa a proteção e bloqueia requisições maliciosas.

---

## 📦 Exemplos de Uso

- Proteger sites WordPress, Joomla, Magento expostos à internet.
- Blindar APIs REST contra ataques de injeção ou fuzzing.
- Aplicações em conformidade com **PCI-DSS**, **LGPD**, etc.

---

## 📚 Leitura Recomendada

- [ModSecurity GitHub](https://github.com/SpiderLabs/ModSecurity)
- [OWASP CRS](https://coreruleset.org/)
- [Documentação Oficial](https://www.modsecurity.org/)

---

## ✅ Deseja saber mais?

Posso te ajudar a:
- Instalar e configurar o ModSecurity no Apache ou NGINX
- Integrar com o OWASP CRS
- Ativar modos de teste e produção

Basta pedir! 😉
