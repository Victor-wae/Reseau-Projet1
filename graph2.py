import pyshark
import matplotlib.pyplot as plt

def analyze_capture_file(capture_file):
    protocol_counts = {}
    cap = pyshark.FileCapture(capture_file)
    for pkt in cap:
        protocol = pkt.highest_layer
        if protocol not in protocol_counts:
            protocol_counts[protocol] = 0
        protocol_counts[protocol] += 1

    return protocol_counts

def plot_protocol_counts(protocol_counts, name):
    protocols = list(protocol_counts.keys())
    counts = list(protocol_counts.values())

    plt.bar(protocols, counts)
    plt.xlabel('Protocol')
    plt.ylabel('Number of Packets')
    plt.title('Number of Packets per Protocol')
    plt.xticks(rotation=90)
    plt.savefig(name)
    plt.show()

if __name__ == "__main__":
    capture_file = "captureCSV/capturegraphs.pcapng"
    protocol_counts = analyze_capture_file(capture_file)
    capture_file2 = "captureCSV/CaptureAddHugeFile.pcapng"
    protocol_counts2 = analyze_capture_file(capture_file2)
    capture_file3 = "captureCSV/ModifyBiggerFile.pcapng"
    protocol_counts3 = analyze_capture_file(capture_file3)
    plot_protocol_counts(protocol_counts,'graphs/graphCapture.png')
    plot_protocol_counts(protocol_counts2, 'graphs/graphAddFile.png')
    plot_protocol_counts(protocol_counts3, 'graphs/graphModifyFile.png')