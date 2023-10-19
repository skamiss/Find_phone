import phonenumbers
from phonenumbers import carrier,geocoder

numero = input("saisir le numéro de téléphone avec l'indicateur \n")
verifie = phonenumbers.parse(numero)

print("le pays : ", geocoder.description_for_number(verifie, "fr"))
print("opérateur : ", carrier.name_for_number(verifie, "fr"))

print("By sekou")

