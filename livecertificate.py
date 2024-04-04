import pyshark

def detect_tls_handshakes(pcap_file):
    tls_handshakes = []
    certificate_exchanges = []
    cap = pyshark.FileCapture(pcap_file, display_filter='tls.handshake')
    for pkt in cap:
        print(pkt.tls.handshake)
        try:
            
            if hasattr(pkt.tls, 'handshake'):
                tls_handshakes.append(pkt)
                
                if hasattr(pkt.tls, 'handshake_certificate'):
                    certificate_exchanges.append(pkt)
        except AttributeError:
            pass

    return tls_handshakes, certificate_exchanges

if __name__ == "__main__":
    pcap_file = "captureCSV/capture4.pcapng"
    tls_handshakes, certificate_exchanges = detect_tls_handshakes(pcap_file)
    print(f"Nombre de handshakes TLS détectés : {len(tls_handshakes)}")
    print(f"Nombre d'échanges de certificats détectés : {len(certificate_exchanges)}")