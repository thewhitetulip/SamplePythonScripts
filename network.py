#uses scapy, you need to have scapy installed

from scapy.all import *
ip = raw_input('Enter IP address')

try:
  alive, dead = alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
  print "MAC  -  IP"
  print alive[0][1].hwsrc  # will print the MAC address of the IP address you specify in the ip
except:
  pass
