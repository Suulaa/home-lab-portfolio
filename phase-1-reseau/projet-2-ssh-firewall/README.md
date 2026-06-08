##############################-------------ENG

#Project 2 - SSH Hardenning + Firewall iptables

## what i configured

 -Installed OpenSSH server on ubuntu Server
 -Generated ED25519 key pair on kali Linux
 -Copied publied Key to Ubuntu Server (ssh-copy-id)
 -Disabled password authentication (PasswordAuthentication no)
 -Disbaled root login (PermitRootLogin no)
 -Configured iptables firewall with strict rules :
   -Default policy : DROP everything
   -Allow : SSH (22), DNS (53), DHCP(67), loopback
 -Saved firewall rules with netfilter-persistent

##Tests Passed
 -nmap -sV 192.168.10.1 -> only port 22 and 53 open
 -ssh userver@192.168.10.1 -> connected without password
 -Password authentication blocked

##Difficulties 
 -SSH service not found : Service named 'ssh' not 'sshd' on ubuntu 24.04
 -Port 22 closed on nmap : Openssh-server was not installed
 



#########################################------------FR 

##Projet 2 - Securisation SSH et Firewall iptables

##Ce que j'ai configure
 -Installation du server OpenSSH sur Ubuntu Server
 -Generation d'une paire de cles ED25519 sur kali linux
 -Copie de la cle publique vers Ubuntu Server (ssh-copy-id)
 -Desactivation de l'authentification par mot de passe
 -Interdiction de connection root 
 -Configuration du firewall iptables : 
  -Politique par defaut : Bloquer tout
  -Autorise : SSH (22). DNS (53), DHCP(67), loopback
  -Sauvegarde des regles avec netfilter-persistent

##Tests reussis
 -nmap -sV 192.168.10.1 -> Uniquements les ports 22 et 54 sont ouverts
 -ssh userver@192.168.10.1 -> connection sans mot de passe a mon ubuntu server
 -Authentification par mot de passe bloquee\

##Difficultes rencontrees

 -Service SSH introuvable : Le service s'appelle 'ssh' et non 'sshd' sur ubuntu 24.04
 -Port 22 ferme sur Nmap : Openss-server n'etait pas installee sur ubuntu 
