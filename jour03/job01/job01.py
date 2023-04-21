import re

def recupe_domaines():


    f = open('jour03/job01/domains.xml', 'r')
    # Le pattern qui détermine là où le curseur doit commencer
    start_pattern = r"<database name=\"test\">"
    contenu = f.read()
    regex = r"(\.\w+)"
    start = re.search(start_pattern, contenu, flags = re.MULTILINE)
    start_pos = 0
    if start:
        start_pos = start.end()
    # place le curseur
    f.seek(start_pos)

    domaines = re.findall(regex, contenu)
    print(f"{len(domaines)} extension de domaine ont été trouvé")

recupe_domaines()