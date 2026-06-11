import nmap
import json
from datetime import datetime

def scan_reseau(cible):
    nm=nmap.PortScanner()
    print ("Scan de "+cible+" en cours...")
    nm.scan(hosts=cible, arguments='-sV --open')

    resultats= []
    for host in nm.all_hosts():
        info = {
             'ip': host,
             'hostname': nm[host].hostname(),
             'etat': nm[host].state(),
             'ports':[]
        }
        for proto in nm[host].all_protocols():
            for port in nm[host][proto].keys():
                svc = nm[host][proto][port]
                info['ports'].append({
                    'port': port,
                    'protocole': proto,
                    'service': svc['name'],
                    'version':svc.get('version', 'N/A')
                })
        resultats.append(info)
    return resultats

def generer_rapport(resultats):
    html="""<!DOCTYPE html>
<html>
<head>
    <title> Rapport Scan Reseau </title>
    <style>
         body {font-family: Arial; background : #f5f5f5; padding 20px;}
         h1 { color : #1A5276;}
        .host { background: white; padding: 15px; marging: 10px 0; border-radius :8px; border-left:4px solid #2E86C1;}
         table { border-callapse: collapse width:100%; }
         th { background: #1A5276; color: white; padding: 8px: text-align: left;}
         td { border: 1px solid #ddd; padding: 8px; }
         tr:nth-child(even) { background : #f2f2f2; }
    </style>
</head>
<body>"""

    html += "<h1> Rapport de Scan Reseau </h1>"
    html += "<p> Genere le : " +datetime.now().strftime('%d/%m/%Y a %H:%M') + "</p>"
    html += "<p> Hotes trouves : " + str(len(resultats)) + "</p>"

    for host in resultats:
        html += "div class='host'>"
        html += "<h2>" + host['ip']+ " - " + (host['hostname'] or  'Sans nom') + "</h2>"
        html += "<p> Etat : "+ host['etat']+ "</p>"
        html += "<table><tr><th>Port</th><th>Protocole</th><th>Service</th><th>Version</th></tr>"
        for port in host ['ports']:
            html += "<tr><td>" + str(port['port'])+ "</td>"
            html += "<td>" + port['protocole'] + "</td>"
            html += "<td>" + port['service']+ "</td>"
            html += "<td>" + port['version']+ "</td></tr>"
        html += "</table></div>"
    html += "</body></html>"

    with open('rapport_scan.html', 'w') as f:
        f.write(html)
    print("Rapport genere : rapport-scan.html")

if __name__ == '__main__':
    cible = '192.168.10.0/24'
    resultats = scan_reseau(cible)

    with open('scan_resultats.json','w') as f:
        json.dump(resultats, f, indent=2)

    generer_rapport(resultats)
    print(str(len(resultats))+ "hotes trouves.")
