import ephem
from datetime import datetime


def planet(user_text):
	planet_name_from_user = user_text.split()[1]
	print(planet_name_from_user)
	planet_name = getattr(ephem, planet_name_from_user)(datetime.now())
	print(ephem.constellation(planet_name))


planet("/planet Earth")



