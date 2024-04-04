import pyshark
from datetime import datetime

def extract_cert_lifetime(cert_data):
    # Extraire les dates de début et de fin de validité du certificat
    not_before = cert_data['not_before']
    not_after = cert_data['not_after']
    
    # Convertir les dates en objets datetime
    valid_from = datetime.strptime(not_before, '%b %d %H:%M:%S %Y %Z')
    valid_until = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
    
    # Calculer la durée de vie du certificat
    lifetime = valid_until - valid_from
    
    return lifetime

def analyze_certificates(pcapng_file):
    # Charger le fichier PCAPNG avec Wireshark
    cap = pyshark.FileCapture(pcapng_file, keep_packets=False)
    
    # Initialiser une liste pour stocker les durées de vie des certificats
    certificate_lifetimes = []
    
    # Parcourir chaque paquet dans le fichier PCAPNG
    for packet in cap:
        # Vérifier si le paquet contient des informations sur le certificat TLS
        if 'TLS' in packet and hasattr(packet.tls, 'x509sat.uTF8String'):
            cert_data = {
                'not_before': packet.tls.get_field_by_showname('Not Before').show,
                'not_after': packet.tls.get_field_by_showname('Not After').show
            }
            lifetime = extract_cert_lifetime(cert_data)
            certificate_lifetimes.append(lifetime)
    
    # Calculer la durée de vie moyenne des certificats
    if certificate_lifetimes:
        avg_lifetime = sum(certificate_lifetimes, datetime.timedelta()) / len(certificate_lifetimes)
        print(f"Durée de vie moyenne des certificats : {avg_lifetime}")
    else:
        print("Aucun certificat TLS trouvé dans le fichier PCAPNG.")

def main():
    pcapng_file = 'captureCSV/capture2.pcapng'
    analyze_certificates(pcapng_file)
    analyze_certificates('captureCSV/capture2.pcapng')
    analyze_certificates('captureCSV/captureWifi.pcapng')

if __name__ == "__main__":
    main()
