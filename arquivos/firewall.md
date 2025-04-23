# Firewall, IPS, IDS e WAF - Conteúdo para Certificação Security+

## Introdução
Firewalls, IPS (Intrusion Prevention Systems), IDS (Intrusion Detection Systems) e WAFs (Web Application Firewalls) são tecnologias essenciais para a segurança de redes e aplicações, cobradas na certificação **CompTIA Security+**.

---

## 1. Firewall

### Definição
Dispositivo (ou software) que filtra o tráfego de rede com base em regras de segurança predefinidas.

### Tipos
- **Stateless (Packet Filtering)**: Filtra pacotes individualmente (IP, porta, protocolo).
- **Stateful**: Mantém registro do estado das conexões (ex: TCP handshake).
- **Proxy Firewall**: Age como intermediário para requisições (camada de aplicação).
- **Next-Generation Firewall (NGFW)**: Inclui DPI (Deep Packet Inspection), inspeção SSL, e integração com IPS/IDS.

### Funções Principais
✅ Filtragem de tráfego (permitir/negar)  
✅ NAT (Network Address Translation)  
✅ VPN (Virtual Private Network)  
✅ Prevenção básica contra DoS  

---

## 2. IDS (Intrusion Detection System)
### Definição
Sistema **passivo** que monitora e alerta sobre atividades maliciosas.

### Tipos
- **NIDS (Network-based)**: Monitora toda a rede.
- **HIDS (Host-based)**: Monitora um host específico.
- **Signature-based**: Compara tráfego com banco de dados de ameaças conhecidas.
- **Anomaly-based**: Detecta desvios do comportamento normal.

### Características
🔹 Gera alertas, mas **não bloqueia** tráfego.  
🔹 Pode ser **inline** (no caminho do tráfego) ou **passivo** (cópia do tráfego).  

---

## 3. IPS (Intrusion Prevention System)
### Definição
Sistema **ativo** que detecta **e bloqueia** ameaças em tempo real.

### Tipos
- **NIPS (Network-based)**: Protege toda a rede.
- **HIPS (Host-based)**: Protege um dispositivo específico.
- **Inline**: Posicionado diretamente no fluxo de tráfego.

### Diferença para IDS
🚦 **IPS bloqueia automaticamente**, enquanto IDS apenas alerta.  

---

## 4. WAF (Web Application Firewall)
### Definição
Protege aplicações web filtrando tráfego HTTP/HTTPS.

### Ataques que previne
- SQL Injection  
- XSS (Cross-Site Scripting)  
- CSRF (Cross-Site Request Forgery)  

### Modos de Operação
- **Detecção**: Apenas registra ameaças.
- **Proteção**: Bloqueia ativamente.

---

## Comparativo
| Tecnologia | Camada OSI | Ação | Exemplo de Uso |
|------------|------------|------|----------------|
| **Firewall** | 3-4 (Rede/Transporte) | Filtra tráfego | Bloquear acesso não autorizado |
| **IDS** | 3-7 (Rede/Aplicação) | Detecta e alerta | Monitorar tentativas de intrusão |
| **IPS** | 3-7 (Rede/Aplicação) | Detecta e bloqueia | Impedir exploração de vulnerabilidades |
| **WAF** | 7 (Aplicaçao) | Filtra HTTP/HTTPS | Proteger contra SQL Injection |

---

## Perguntas de Exemplo (Estilo Security+)
1. **Qual sistema é mais adequado para bloquear um ataque de força bruta em um servidor web?**  
   a) Firewall Stateless  
   b) HIDS  
   c) NIPS  
   d) WAF  
   **Resposta:** c) NIPS  

2. **Um WAF é mais eficaz contra qual tipo de ataque?**  
   a) DDoS  
   b) SQL Injection  
   c) Spoofing de IP  
   d) Varredura de portas  
   **Resposta:** b) SQL Injection  

---

## Melhores Práticas
- 🔄 **Atualize assinaturas** regularmente (especialmente em IPS/IDS).  
- 📊 **Monitore logs** para identificar falsos positivos/negativos.  
- 🛡️ **Use em camadas** (ex: Firewall + IPS + WAF).  

---

## Conclusão
Essas tecnologias são fundamentais para a **segurança defensiva** e são amplamente cobradas na Security+. Recomendo praticar em laboratórios (ex: pfSense para firewalls, Snort para IDS/IPS).  

📌 **Dica para a prova:** Entenda **quando usar cada tecnologia** e seus limites (ex: um firewall não previne XSS, mas um WAF sim).  