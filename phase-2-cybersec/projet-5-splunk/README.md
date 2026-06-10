#########################-----------------ENG

# Project 5 :  SIEM ( Splunk Entreprise )

# What I configured 
 -Downloaded and installed Splunk Enterprise 10.4.0 on my ubuntu Server
 -Extended disk partition from 12 GB to 25 GB to accomodate Splunk
 -Installed rsyslog to generate traditionnal log files
 -Added 3 log sources to Splunk
   -/var/log/auth.log ( SSH authentications )
   -/var/log/syslog ( System logs )
   -/var/log/kern.log ( kernel logs )
 -Created alert : " Tentatives SSH suspectes " 
   -Scheduled every 5 minutes
   -Triggers when more 3 failed attemps detected
   -Severity : High

# Test Performed
 -Simulated SSH brute-force from Kali ( Invalid Users )
 -Verified logs appear in splunk in real time
 -SPL query used : source="/var/log/auth.log" Invalid user

# Results
 -Splunk successfully indexed auth.log events
 -Invalid SSH attemps from 192.168.10.2 ( Kali ) visible in splunk
 -Alert created and saved successfully

# What I learned 
 -How a SIEM collects and indexes logs
 -How to write basic SPL queries
 -How to create automated alerts in Splunk
 -Differences between log sources and sources types

# Difficulties
 -Disk 100% full after Splunk installation : So I extended LVM partition with lvextend + resize2fs.
 -No auth.log on Ubuntu 24.04 : I installed rsyslog to generate classic log files.
 -Port 8000 not accessible : Added iptables rules to allow port 8000.
 -Hydra brute-force failed : SSH password ath disabled ( it's our security config )


########################---------------------FR

# Projet 5 : SIEM ( Splunk Entreprise )

# Ce que j'ai configure

 -Telechargement et installation de Splunk Entreprise 10.4.0 sur mon ubuntu Server
 -Extension de la partition du disque de 12 GB a 25 GB pour accomoder Splunk
 -Installation de rsyslog pour generer des fichiers logs classiques.
 -Ajout de 3 sources de logs dans Splunk :
   -/var/log/auth.log ( authentification SSH )
   -/var/log/syslog ( logs systeme )
   -/var/log/kern.log ( logs kernel )
 -Creation d'une alerte : " Tentative SSH suspectes "
   -Planifiee toutes les 5 minutes 
   -Se declenche si plus de 3 tentatives echouees
   -Severite : High ( fort )

# Test realises
 -Simulation brute force SSH depuis Kali.
 -Verificationb que les logs apparaissent dans Splunk en temps reel.
 -Requetes SPL utilisee : source="/var/log/auth.log" Invalid user.
 
# Resultats
 -Splunk indexe correctement les evenements auth.log
 -Tentatives SSH invalides depuis 192.168.10.1 ( Kali ) visible dans Splunk.
 -Alerte creee et sauvegardee avec succes

# Ce que j'ai appris
 -Comment un SIEM collectes et indexes les logs.
 -Comment ecrire des requetes SPL de base.
 -Comment creer des alertes automatiques dans Splunk.
 -Difference entre sources de logs et types de logs.

# Difficultes rencontrees
 -Disque 100% plein apres installation de Splunk : Extension de la partition LVM avec lvextend et resize2fs.
 -Pas de auth.log sur Ubuntu 24.04 : j'ai donc installe rsyslog pour generer des fichiers log.
 -Port 8000 inaccessible : Ajout de regle iptables pour autoriser port le port 8000
 -Hydra brute-force echoue : Authentification SHH par mot de passe echouee ( a cause de notre configuration )
