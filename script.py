# coding=utf-8

print("Bienvenue sur PronoteTools ! Version 1.0.0.0")
print("--------------------------------------------")
print("1. Calculer ta moyenne")
select = input("Pour commencer que veux-tu faire ? Saisis le numéro : ")

if(select=="1"):
    print("Bienvenue sur le calculateur de moyenne ! Il te suffit de copier-coller le fichier json, vas lire les instructions !")
    releve = open('pronote-json.txt', 'r').read()
    ms = releve.count("satisfaisante")
    mts = releve.count("bonne")
    mf = releve.count("fragile")
    mi = releve.count("insuffisante")
    total = ms+mts+mf+mi
    mssur20 = ms*15
    mtssur20 = mts*20
    mfsur20 = mf*10
    misur20 = mi*5
    moyennebrut = mssur20 + mtssur20 + mfsur20 + misur20
    moyenne = moyennebrut/total
    print(moyenne)
