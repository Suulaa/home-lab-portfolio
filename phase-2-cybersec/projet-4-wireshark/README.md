##########################---------------ENG

# Project 4 : Network Traffic Analysis ( Wireshark and Nmap )

# What i configured
 -Installed wireshark on kali linux
 -Captured network traffic on eth1 ( internal network )
 -Performed different Nmap scans on Ubuntu Server
 -Analyzed packets with Wireshark filters

# Scan Performed

 -nmap 192.168.10.1 : basic port scan
 -nmap -sV 192.168.10.1 : Service version detection
 -nmap -A 192.168.10.1 : Agressive scan ( OS and scripts )

# Results
 -Port 22 ( SSH ) : open
 -Port 53 ( DNS ) : open
 -998 ports : filtered ( iptables DROP policy )

# Wireshark filters used 
 -icmp : show ping packets
 -tcp : show all TCP packets
 -tcp.flags.syn==1 && tcp.flags.ack==0 : show port scan ( SYN packets )
 -tcp.flags.syn==1 && tcp.flags.ack==1 : show open ports responses

# What I learned 
 - How Nmap TCP SYN scan works
 -Difference between open/cloed/filtered ports
 -Difference between DROP and REJECT in iptables
 -How to read TCP flags in wireshark





########################################-----------------FR

# Projet 4 : Analyse de traffic reseau : Wireshark et Nmap

# Ce que j'ai fait

 -Installation de wireshark sur kali linux
 -Captures du traffic reseau sur eth1 ( reseau interne )
 -Realisation de differentes scans Nmap sur Ubuntu Server
 -Analyse des paquets avec les filtres wireshark

# Scans realises
 -nmap 192.168.10.1 : scan de ports basique
 -nmap -sV 192.168.10.1 : Detection des versions des services
 -nmap -A 192.168.10.1 : scan agressif ( OS + scripts )

# Resultats
 -Port 22 ( SSH ) : Ouvert
 -Port 53 ( DNS ) : Ouvert
 -998 ports : filtres ( politique DROP iptables )

# Filtres wireshark utilises
 -icmp : voir les paquets ping
 -tcp : voir tout le trafic TCP
 -tcp.flags.syn==1 && tcp.flags.ack==0 : voir le scan de ports
 -tcp.flags.syn==1 && tcp.flags.ack==0 : Voir les reponses des ports ouverts

# Ce que j'ai appris :
 -Fonctionnement du scan SYN TCP de Nmap
 -Difference entre ports open, closed, filtered
 -Difference entre DROP et REJECT dans iptables
 -Comment lire les flags dans wireshark
