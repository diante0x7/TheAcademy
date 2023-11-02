from scapy.all import *
import argparse

parser = argparse.ArgumentParser(description="Host Discovery Tool")
parser.add_argument('-g', '--gateway', required=True, help="Gateway that we will use to scan.")
parser.add_argument('-a', '--arp', help="ARP Scan | DEFAULT")
parser.add_argument('-t', '--tcp', help="TCP Ack Scan")
args = parser.parse_args()

def tcp_scan(gateway):
    ans,unans=sr( IP(dst=gateway + "/24")/TCP(dport=80,flags="S") )
    ans.summary()

def arp_scan(gateway):
    ans,unans=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=gateway + "/24"),timeout=2)
    ans.summary()