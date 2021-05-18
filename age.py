from datetime import *


def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


print(calculate_age(date(2000, 8, 4)), "years")
