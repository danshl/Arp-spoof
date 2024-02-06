# Arp-spoof
ARP spoofing is a deceptive technique used to manipulate the Address Resolution Protocol (ARP) tables in a network, allowing an attacker to intercept, modify, or block network traffic. 

As part of our university project, we developed an attack enabling
* Man-in-the-Middle (MITM) scenarios. This entails intercepting and altering communications between devices, potentially leading to further exploits like DNS spoofing or file tampering.
 
* Additionally, ARP spoofing can be leveraged to disconnect specific devices from the network by spoofing the MAC address of the router's DEFAULTGETWAY. 

*Furthermore, it can disrupt the entire network by identifying and spoofing the MAC addresses of all devices, causing widespread communication failures.

## Installation

(a) Download the files 
```bash
git clone https://github.com/danshl/Arp-spoof.git
```
(b) Install dependencies - To install the required dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```

(c) Activate the code as *sudo* by 3 parameters:
```bash
sudo python3 ./act.py -t TARGET_IP -g GATEWAY_IP -m MODE
```

Links
------
- **Documentation Flask:** https://flask.palletsprojects.com/
- **API Google Sheets:** https://developers.google.com/sheets/api/guides/concepts
- **API Google Drive:** https://developers.google.com/drive/api/guides/about-files
- **Source Code:** https://github.com/danshl/WebConncectionDrive
