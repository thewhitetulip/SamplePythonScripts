from scapy.all import *

def printType(element):
   i=0
   while i<100:
     try:
       print element.type
       i+=1
     except:
       print('%d does not have a type'%i)
       i+=1

def main():
path = raw_input('Enter the path of the pcap file you want to read: ')
try:
   a = rdpcap(path)
except:
  print 'Error opening the pcap file'
printType(a)

main() 
   
   
