# Szám validáció. True ha valóban integer, False ha nem az.
import datetime


def is_number(number):
    try:
        tmp_num = int(number)
        return True
    except ValueError:
        return False

# Dátum validáció. True ha megfelelő a formátum, False ha nem az.
def is_correct_date_format(date):
    try:
        tmp_date = datetime.date.fromisoformat(date)
        return True
    except ValueError:
        return False
