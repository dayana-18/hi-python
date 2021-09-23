import json
import csv

#ouvre le fichier json et recupère ses données
with open('data.json') as dat_file:
    data = json.load(dat_file)
stud_data = data['Singers'] #array du fichier
 
#ouvre un fichier CSV pour écrire dessus
data_file = open('data_file.csv', 'w') 
csv_writer = csv.writer(data_file)

count = 0
#pour chaque élément du array
for cnt in stud_data:
    if count == 0:
        header = cnt.keys()
        csv_writer.writerow(header) #les titres
        count += 1
    csv_writer.writerow(cnt.values()) #les valeurs
data_file.close()