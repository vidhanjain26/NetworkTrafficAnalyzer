# Network Traffic Analyzer

A simple network traffic analyzer tool built using Python and Scapy, with an optional GUI created using Tkinter. This tool captures and displays network packets in real-time.

## Features

- Capture network traffic in real-time.
- Display IP and TCP packet information.
- Start and stop packet capturing via a simple GUI (optional).
- Dark-themed GUI for a modern look.
- Cross-platform support for Windows and Linux.

## Installation

### **Windows**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/vidhanjain26/NetworkTrafficAnalyzer.git
    
2. Navigate to the project directory
    ```sh
    cd NetworkTrafficAnalyzer

3. **Install the required Python packages**:

   ```sh
    pip install scapy 
    pip install tk

4. **Install Npcap**:
   
   - Download and install Npcap from [Npcap website](https://nmap.org/npcap/#download).
   - During installation, ensure that "Install Npcap in WinPcap API-compatible mode" is checked.

5. **Run the Tool**:

    - Command-line mode:
      ```bash
      python Network-Traffic-Analyzer.py
      ```

    - GUI mode:
      ```bash
      python Network-Traffic-Analyzer.py
      ```

### **Linux**

1. **Clone the repository**:

    ```bash
    git clone https://github.com/vidhanjain26/NetworkTrafficAnalyzer.git
2. Navigate to the project directory
   ```sh
    cd NetworkTrafficAnalyzer
    ```

3. **Install the required Python packages**:

    ```bash
    pip3 install scapy
    ```

4. **Install Tkinter** (for GUI):

    ```bash
    sudo apt-get install python3-tk
    ```

5. **Install Additional Tools**:

    ```bash
    sudo apt-get install tcpdump
    sudo apt-get install libpcap-dev
    ```

6. **Run the Tool**:

    - Command-line mode:
      ```bash
      sudo python Network-Traffic-Analyzer.py
      ```

    - GUI mode:
      ```bash
      sudo python Network-Traffic-Analyzer.py
      ```

## Usage

### **Command-line Mode**

You can run the script in command-line mode without the GUI by executing:

```bash
python Network-Traffic-Analyzer.py
