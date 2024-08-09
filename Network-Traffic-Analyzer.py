import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff, IP, TCP
from threading import Thread

class NetworkTrafficAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Traffic Analyzer")

        # Set background color
        self.root.configure(bg='#282c34')

        # Create and configure the text area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=100, height=20, bg='#1e2127', fg='#ffffff')
        self.text_area.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

        # Create and configure buttons
        self.start_button = tk.Button(root, text="Start Capture", command=self.start_capture, bg='#61afef', fg='#282c34')
        self.start_button.grid(column=0, row=1, padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop Capture", command=self.stop_capture, bg='#e06c75', fg='#282c34', state=tk.DISABLED)
        self.stop_button.grid(column=1, row=1, padx=10, pady=10)

        self.is_capturing = False
        self.sniff_thread = None

    def start_capture(self):
        self.is_capturing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Start sniffing in a separate thread to prevent freezing the GUI
        self.sniff_thread = Thread(target=self.sniff_packets)
        self.sniff_thread.start()

    def stop_capture(self):
        self.is_capturing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def sniff_packets(self):
        sniff(prn=self.process_packet, stop_filter=lambda x: not self.is_capturing)

    def process_packet(self, packet):
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            protocol = packet[IP].proto
            packet_info = f"IP Packet: {ip_src} -> {ip_dst} (Protocol: {protocol})"

            if TCP in packet:
                sport = packet[TCP].sport
                dport = packet[TCP].dport
                packet_info += f"\nTCP Segment: {ip_src}:{sport} -> {ip_dst}:{dport}\n"

            # Insert the packet information into the text area
            self.text_area.insert(tk.END, packet_info + "\n")
            self.text_area.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkTrafficAnalyzer(root)
    root.mainloop()
