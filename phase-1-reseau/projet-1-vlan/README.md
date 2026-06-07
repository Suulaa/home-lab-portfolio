############### ENG
# Porject 1 : VLAN, DHCP AND DNS

# What I configured
 -Two network interfaces : enp0s3 (NAT) and ens0p8(192.168.10.1) in my ubuntu server
 -IP forwarding enabled between subnets
 -DHCP server that assigns IPs from 192.169.10.100 to .200
 -DNS server BIND9 : resolve *.monlab.local

## Test passed
 nslookup www.monlab.local 192.168.10.1
 -> Adderess : 192.168.10.1
##Difficulties
 During the lab setup, I changed the IP addresses of my Ubuntu Serve and kali, but I couln't install any packages
 because my VMs had no internet access. After some researches, I undestood that I need 2 netwokr adapters on each Vm :
 on in NAT mode for internet access and one in Host-Only mode, so both machines are on the same network and cam
 communicate with ech other








##################### FR
# Projet 1 : VLAN, DHCP et DNS


## Ce que que viens de configurer :
 -Deux interfaces reseaux : enp0s3 (NAT) et enp0s8 (192.168.10.1) sur mon ubuntu server
 -Routage IP active entre sous-reseaux
 -Serveur DHCP qui distribue des adresses IPs, j'ai choisi une plage entre 192.168.10.100 a .200
 -Serveur DNS BIND9 : resout *.monlab.local

## Test reussi
 nslookup www.monlab.local 192.168.10.1
 -> Address : 192.168.10.1

## Dificultees
 Lors de l'installation de mon lab j'avais change les adresses ip de mon ubuntu server et de mon kali mais je parvenais
 pas a faire des installations de packages. Apres avoir fait des recherches j'ai compris que c'est parceque mes machines virtuelles ne 
 parvenaient pas a internet. Du coup j'ai cree 2 adaptateur pour chaque machine. Une en NAT et en Host only pour ainsi avoir 2 interafaces
 et faire en sorte que mes machines soient dans le meme reseau et puisse communiquer normalement. 





