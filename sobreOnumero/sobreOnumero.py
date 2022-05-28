import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

telefone = "+5521999999999"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)

local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print('Localização: '+local)



telefone_formulario_ajustado = phonenumbers.parse(telefone, "BR")

telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado,phonenumbers.PhoneNumberFormat.NATIONAL)

telefone_internacional = phonenumbers.format_number(telefone_ajustado,phonenumbers.PhoneNumberFormat.INTERNATIONAL)

print('formatado local: '+telefone_formatado)
print('formatado internacional: '+telefone_internacional)




operadora = carrier.name_for_number(telefone_ajustado,'pt-br')

print('operadora: ' + operadora)