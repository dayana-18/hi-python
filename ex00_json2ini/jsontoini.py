import json, os #pour vérifier la gestion d'erreur

file = "file.json"
string = ""

#si le fichier existe
if os.path.exists(file) :
    with open(file, 'r') as file:
        data = json.load(file) #as a dicto

    for section in data.keys():
        string += f"[ {section} ] \n" 
        sectionElement = data[section]
        for key in sectionElement.keys():
            string +=  key + " = " + str(sectionElement[key]) + "\n"
        string += "\n"
    
    with open('file.ini', 'w') as file:
        file.write(string)
        print("Job done !")

else:
    print("file doesn't exists")