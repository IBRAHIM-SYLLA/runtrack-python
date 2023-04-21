import re
# compte le nombre de mots
def find_data():
    data_txt = open('jour03/job02/data.txt', 'r')
    pattern = r"\w+"
    words = re.findall(pattern, data_txt.read())
    # print(f"{len(words)} mots trouves dans le fichier.")
    return words
mots = find_data()
taille = int(input("mettez une taille de mots: "))
count = 0
for i in range (0, len(mots)):
    if len(mots[i]) == taille:
        count += 1

print(f"{count} nombre de mot long comme la taille que vous avez définit")