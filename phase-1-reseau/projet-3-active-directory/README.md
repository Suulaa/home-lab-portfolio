###################--------------ENG

# Porject 3 : Active Directory and GPO

# What I configured
 -Installed Windows Server 2022 graphic user interface (GUI)
 -Installed Active Directory Domain Service (AD DS)
 -Created a new forest : monlab.local
 -Created user : MSarr (Moustapha Sarr)
 -Created Security group : IT-Admins
 -Added MSarr in IT-Admins group
 -Created GPO : Security-Base
 -Disabled access to control Panel for users
 -Disabled access to CMD for users
 -Applied GPO with grupdate /force on PowerShell

## Tests Passed
 -Domain monlan.local created successfully
 -User MSarr created and added to IT-Admins group
 -GPO Security-Base applied succesfully

## Difficulties
 -Windows Server core installed intead of GUI, I reinstalled choosing Desktop Experience.
 -ISO booting again after restart, then I removed ISO from VirtualBox storage settings.





###################-------------FR

# Projet 3 : Active Directory et GPO

# Ce que j'ai configure : 
 -Installation de Windows Server 2022 avec interface graphique
 -Installation d'Active Directory Domain Services
 -Creation d'une nouvelle foret : monlab.local
 -Creation d'un nouveau utilisateur : MSarr ( Moustapha Sarr )
 -Creation d'un groupe IT-Admins
 -Ajout de MSarr au groupe IT-Admins
 -Creation d'une GPO : Security-Base
 -Desactivation de l'acces au Panneau de configuration
 -Desactivation de l'acces au CMD
 -Application de la GPO avec grupdate /force sur PowerShell

# Tests reussis 
 -Domaine monlab.local cree avec succes
 -Utilisateur MSarr cree et ajoute au groupe IT-Admins
 -GPO Security-Base appliquee avec succes

# Difficultes rencontrees

 -Windows Server Core installe au lieu du GUI, j'ai repris l'installation en choisissant Desktop Experience.
 -L'ISO redemarrait apres extinction, j'ai donc supprime l'ISO dans les parametres de VirtualBox
