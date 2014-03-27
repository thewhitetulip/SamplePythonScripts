from scapy.all import *

pcap_path = raw_input('Path of pcap file: ')
file_path = raw_input('Enter target file name')

try:
  file = open(file_path,'w')
  pkts = rdpcap(pcap_path)
  for i in range(len(pkts)):
    if ARP in pkts[i]:
     file.write ('%d,%s,%s,%s,%s,%d,%s\n'%( a[i].time, a[i].hwsrc, a[i].psrc, a[i].hwdst, a[i].pdst, a[i].hwtype, a[i].op))
except:
  print 'some error occured'
