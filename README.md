# Network Traffic Analyzer

A simple network traffic analyzer tool built using Python and Scapy, with an optional GUI created using Tkinter. This tool captures and displays network packets in real-time.

## Features

- Capture network traffic in real-time.
- Display IP and TCP packet information.
- Start and stop packet capturing via a simple GUI (optional).
- Dark-themed GUI for a modern look.

## Prerequisites

- Python 3.x
- Scapy
- Tkinter (for GUI)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/NetworkTrafficAnalyzer.git
    cd NetworkTrafficAnalyzer
    ```

2. **Install the required Python packages**:

    ```bash
    pip install scapy
    ```

3. **Install Npcap** (for Windows users):
   
   - Download and install Npcap from [Npcap website](https://nmap.org/npcap/#download).
   - During installation, ensure that "Install Npcap in WinPcap API-compatible mode" is checked.

## Usage

### **Command-line Mode**

You can run the script in command-line mode without the GUI by executing:

```bash
python main.py
