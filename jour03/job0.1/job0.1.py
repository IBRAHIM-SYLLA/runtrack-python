fichier = open("jour03/job0.1/output.txt", "w")
fichier.write(input("Enter une chaîne de caractère: "))
fichier = open("jour03/job0.1/output.txt", "r")
print(fichier.read())