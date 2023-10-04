from datetime import datetime
import json

# Supposons que date_debut soit un objet de type date
date_debut = datetime.now()

# Convertir la date en une chaîne de caractères au format ISO (YYYY-MM-DD)
date_debut_str = date_debut.isoformat()

print("test", date_debut)
print("en format jon", date_debut_str)

with open("testdate.json", "w") as my_file:
    json.dump(date_debut_str, my_file, indent=4)

# Vous pouvez maintenant utiliser date_debut_str dans votre structure JSON