import os
import pyshark
import matplotlib.pyplot as plt

def analyze_pcapng_capture(pcapng_file):
    domain_counts = {}
    ipv4_counts = {}

    try:
        capture = pyshark.FileCapture(pcapng_file)

        for packet in capture:
            if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
                domain = packet.dns.qry_name
                if 'kdrive' in domain:
                    if domain not in domain_counts:
                        domain_counts[domain] = 0
                        ipv4_counts[domain] = 0

                    domain_counts[domain] += 1

                    if hasattr(packet, 'ip') and packet.ip.version == '4':
                        ipv4_counts[domain] += 1

        capture.close()
    except FileNotFoundError:
        print(f"Error: File '{pcapng_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return domain_counts, ipv4_counts

def plot_domain_counts(domain_counts, ipv4_counts):
    domains = list(domain_counts.keys())
    counts = list(domain_counts.values())
    ipv4_counts = [ipv4_counts[domain] for domain in domains]

    plt.bar(domains, counts, label='IPv6 DNS Requests')
    plt.bar(domains, ipv4_counts, label='IPv4 DNS Requests')
    plt.xlabel('Domain')
    plt.ylabel('Number of DNS Requests')
    plt.title('Number of DNS Requests per Domain')
    plt.xticks(rotation=0)
    plt.legend()
    plt.savefig('graphs/graph.png')
    plt.show()

# Usage example
pcapng_dir = 'captureCSV/'
pcapng_files = [os.path.join(pcapng_dir, file) for file in os.listdir(pcapng_dir) if file.endswith('.pcapng')]

domain_counts = {}
ipv4_counts = {}

for pcapng_file in pcapng_files:
    file_domain_counts, file_ipv4_counts = analyze_pcapng_capture(pcapng_file)
    
    for domain, count in file_domain_counts.items():
        if domain not in domain_counts:
            domain_counts[domain] = 0
        domain_counts[domain] += count

    for domain, count in file_ipv4_counts.items():
        if domain not in ipv4_counts:
            ipv4_counts[domain] = 0
        ipv4_counts[domain] += count

plot_domain_counts(domain_counts, ipv4_counts)