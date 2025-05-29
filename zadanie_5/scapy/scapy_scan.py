from scapy.all import sr1, IP, TCP

target = 'portal.wsb.pl'
ports = range(22, 444)


# Bardzo podstawowe rozpoznawanie systemu operacyjnego na podstawie TTL i rozmiaru okna TCP
def simple_os_guess(ip):
    pkt = IP(dst=ip)/TCP(dport=80, flags='S')
    resp = sr1(pkt, timeout=1, verbose=0)
    if resp is not None and resp.haslayer(TCP):
        ttl = resp.ttl
        window = resp[TCP].window
        # Prosta heurystyka do zgadywania systemu operacyjnego
        if ttl <= 64:
            os = "Linux/Unix-like (TTL~64)"
        elif ttl <= 128:
            os = "Windows (TTL~128)"
        elif ttl <= 255:
            os = "Cisco/Network device (TTL~255)"
        else:
            os = "Nieznany"
        print(f"Zgadywany system operacyjny: {os}, Rozmiar okna TCP: {window}")
    else:
        print("Nie udało się określić systemu operacyjnego (brak odpowiedzi na SYN)")

print(f"Skanowanie portów {target} w zakresie 22-443...\n")
for port in ports:
    # Wysyła pakiet SYN na każdy port
    pkt = IP(dst=target)/TCP(dport=port, flags='S')
    resp = sr1(pkt, timeout=0.5, verbose=0)
    if resp is not None and resp.haslayer(TCP):
        if resp[TCP].flags == 0x12:  # SYN-ACK oznacza, że port jest otwarty
            print(f"Port {port} jest OTWARTY")
        elif resp[TCP].flags == 0x14:  # RST-ACK oznacza, że port jest zamknięty
            pass  # Port jest zamknięty

# Próba rozpoznania systemu operacyjnego po zakończeniu skanowania portów
print("\nPróba rozpoznania systemu operacyjnego na podstawie TTL i rozmiaru okna TCP:")
simple_os_guess(target)

print("Skanowanie zakończone.")
