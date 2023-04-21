import re
# compte le nombre de mots
def find_data():
    data_txt = open('jour03/job02/data.txt', 'r')
    pattern = r"\w+"
    words = re.findall(pattern, data_txt.read())
    print(f"{len(words)} mots trouves dans le fichier.")

find_data()