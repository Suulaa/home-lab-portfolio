##################-------------ENG

# Project 6 : Intrusion Detection System with Suricata ( IDS )

# What I Configured

 -Installed Suricata 8.0.3 on ubuntu Server
 -Configured HOME_NET : 192.168.10.0/24
 -Configured interface : enp0s8
 -Updated detection rules with suricata-update
 -Created custom rules in local.rules :
  -Alert on ICMP ping
  -Alert on SSH connection attempts
  -Aler on port scan (20+ SYN in 10 seconds)

# Tests performed
 
 -Launched nmap -A -T4 192.168.10.1 from my kali
 -Monitored alerts in real time with tail -f fast.log

# Resulsts
 -ICMP Ping detected 
 -Port scan detected
 -SSH connection attempt detected

# What I learned
 -Difference between IDS and IPS
 -How Suricata rules are structured ( alert. protocol, source, destination, options )
 -How to write custom detection rules.
 -Diiference between Suricata ( network traffic ) and Splunk ( log analysis )

# Difficulties
 -0 rules loaded at startup : the file local.rules was in wrong directory.
 -Rules not found : Copied local.rules to /var/lib/suricata/rules/ because it was in /var/log/suricata/rules/.




##############################-------------FR 

# Projet 6 : Detection d'intrusion avec Suricata ( IDS )

# Ce que j'ai configure

 -Installation de Suricata 8.0.3 sur mon Ubuntu server.
 -Configuration HOME_NET : 192.168.10.0/24
 -Configuration de l'interface enp0s8
 -Mise a jour des regles avec suricata-update
 -Creation des regles personnalisees dans local.rules:
  -Alerte sur Ping ICMP
  -Alerte sur tentatives de connexion SSH
  -Alerte sur scan de ports ( 20+ SYN en 10 secondes )

# Tests realises
 -Lancement de nmap -A -T4 192.168.10.1 depuis mon kali
 -Surveillance des alertes en temps reel avec tail -f fast-log
 

# Resultats
 -ICMP Ping detecte
 -Scan de ports detecte
 -Tentative de connexion SSH detectee

# Ce que j'ai appris
 -Difference entre IDS et IPS
 -Structure des regles Suricata
 -Comment ecrire des regles de detection personnalisees
 -Difference entre Suricata ( traffic reseau ) et Splunk ( analyse de logs (Journeaux))

# Difficultes rencontrees
 -0 regles chargee au demarrage : le fichier local.rules etait dans le mauvais repertoire.
 -Regles non trouvees : J'ai ainsi copie le fichier local.rules dans /var/lib/suricata/rules/ puisqu'il etait dans dans /var/log/suricata/rules/
