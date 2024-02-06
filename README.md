# Arp-spoof
ARP spoofing is a deceptive technique used to manipulate the Address Resolution Protocol (ARP) tables in a network, allowing an attacker to intercept, modify, or block network traffic. 

As part of our university project,we developed an attack that consist:
* Man-in-the-Middle (MITM) scenarios. This entails intercepting and altering communications between devices, potentially leading to further exploits like DNS spoofing or file tampering. (mode 1)
 
* Additionally, ARP spoofing can be leveraged to disconnect specific devices from the network by spoofing the MAC address of the router's default gateway. (mode 2)

* Furthermore, it can disrupt the entire network by identifying and spoofing the MAC addresses of all devices, causing widespread communication failures. (mode 3)

## Installation

(a) Download the files 
```bash
git clone https://github.com/danshl/Arp-spoof.git
```
(b) Install dependencies - to install the required dependencies for this project, run the following command:

```bash
pip install -r requirements.txt
```

(c) Activate the code as *sudo* by 3 parameters:
```bash
sudo python3 ./arp_code.py -t TARGET_IP -g GATEWAY_IP -m MODE
```
TARGET_IP : the victim ip.

GATEWAY_IP : the default gateway of the router

MODE (1, 2 or 3):

- **Mode 1:** ARP spoofing by our computer as a Man-in-the-Middle (MITM) attack.
- **Mode 2:** Block the Target IP communication with the network.
- **Mode 3:** Block all devices' communication on the network (mix mac:ip).

For more help run "sudo python3 ./arp_code.py -h" or send mail to dansh@post.bgu.ac.il

Links
------
- **Reading materials:** https://www.golinuxcloud.com/man-in-the-middle-attack-arp-spoofing/
- **Used in prev code:** https://www.geeksforgeeks.org/python-how-to-create-an-arp-spoofer-using-scapy/
- **Source Code:** https://github.com/danshl/Arp-spoof.git

Creators
------
Daniel Shlomo

Daniel Elianov

Ron Haikin
