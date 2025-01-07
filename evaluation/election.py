import datetime

ddd = input("Entrez votre date de naissance")
nnn = datetime.datetime.strptime(ddd, "%d/%m/%Y")
print(nnn)
d18 =nnn.replace(year=nnn.year+18)
print(f"Tu seras majeur le {d18.strftime("%d/%m/%Y")}")
if d18 <= datetime.datetime(2027, 6, 1):
    print("tu pourras voter le 01/06/2027, t'as interet a voter PS")
else:
    print("tu devras attendre la prochaine élection c'est pas de ton age")
