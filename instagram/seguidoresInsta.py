from datetime import datetime
import instaloader

insloa = instaloader.Instaloader()
insloa.login('Usuario', 'Senha')

followers = instaloader.Profile.from_username(insloa, 'dayvid_jr_').get_followers()
followees = instaloader.Profile.from_username(insloa, 'dayvid_jr_').get_followees()


# Seguidores
print(str(followers._data['count']))

# Seguindo
print(str(followees._data['count']))

# Informação de seguidores
print(str(followees._data['edges']))