import phonenumbers
from phonenumbers import geocoder

fone = input("Digite o telefone no formato +55988887777: ")

phone_number = phonenumbers.parse(fone)

print(geocoder.description_for_number(phone_number, 'pt'))