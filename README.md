SamplePythonScripts
===================

A collection of small snippets in python for doing general purpose activities that we need to do over our machines. python is a very powerful tool for programming in general, you can easily replace shell scripting by scripting in python, and it is platform independant.

These are snippets from my graduation research project, since I can not publish my project, I am publishing small portions of the project to give back to the community. And if you want me to write snippets for the problem you are facing then email me, I will publish them as soon as possible.  Enjoy.

List:

1. createfile.py : When you have to create an awfully large amount of files inside a folder, it is not possible to create it by hand, use this utlity to specify the folder, the path, and the names to be given the files that'll be created
2. networking.py  : some simple scripts to do some amazing stuff over the network, for eg finding MAC address of a client in the network without having physical access to the machine
3. bulkRename.py: rename multiple files programmatically
4. hex2int.py: we have a file EtherType, and we convert it to EtherType2, link for image: https://qph.is.quoracdn.net/main-qimg-cd53d1dd106f20dd19cff0197fb2ac05?convert_to_webp=true
5. type.py: We have a pcap file of packet capture, and we have to print the EtherType for each packet, then we use this script to do so
6. processarp.py: Reads a pcap file into python using scapy and produces a csv file as output in the following format: Timestamp, source MAC address, source IP address, Destination MAC address, Destination IP address
7. ceaser.py: implementing a simple ceaser cipher
8. ceaserde.py: decrypting ceaser cipher
9. mono.py: monoalphabetic cipher encryption
10. monode.py: monoalphabetic cipher decryption
11. removing_numbers.py: suppose you have a file which starts with numbers, then this script can remove the numbers from the file
12. tables: generates mathematical tables
13. generateAllPossibleWords.txt: A step by step tutorial of generating all possible strings from an imput string, this is a session stored from the IDLE
14. builtinFunctions.py: demo of major builtin functions that are used all the time
15. video.py: takes a path of the folder where there are videos and stores the path in a file and will play a random video when you execute the file, it uses subprocess module to call vlc so you need to have vlc installed
