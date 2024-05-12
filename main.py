import datetime

from classes.ketagyas_szoba import KetagyasSzoba
from classes.szalloda import Szalloda
from classes.menu import Menu
from classes.egyagyas_szoba import EgyagyasSzoba

# Fő program
# Hotel objektum létrehozása
hotel = Szalloda("HOTEL Krisztián", 1036, "Budapest", "Teszt Elek utca 6-8")

# Hotel szobákkal való feltöltése
room100 = EgyagyasSzoba(100, 15000)
room101 = EgyagyasSzoba(101, 17500)
room200 = KetagyasSzoba(200, 25000)

# Foglalások beállítása
room100.add_reservation("Bekre Pál", datetime.date.fromisoformat("2024-06-11"))
room100.add_reservation("Lekv Áron", datetime.date.fromisoformat("2024-07-05"))
room101.add_reservation("Gipsz Elek", datetime.date.fromisoformat("2024-08-02"))
room200.add_reservation("Boro Zoltán", datetime.date.fromisoformat("2024-09-09"))
room200.add_reservation("Kispál Inka", datetime.date.fromisoformat("2024-11-27"))

hotel.add_room(room100)
hotel.add_room(room101)
hotel.add_room(room200)

print()
print()
print('██╗  ██╗ ██████╗ ████████╗███████╗██╗         ██╗  ██╗██████╗ ██╗███████╗███████╗████████╗██╗ █████╗ ███╗   ██╗')
print('██║  ██║██╔═══██╗╚══██╔══╝██╔════╝██║         ██║ ██╔╝██╔══██╗██║██╔════╝╚══███╔╝╚══██╔══╝██║██╔══██╗████╗  ██║')
print('███████║██║   ██║   ██║   █████╗  ██║         █████╔╝ ██████╔╝██║███████╗  ███╔╝    ██║   ██║███████║██╔██╗ ██║')
print('██╔══██║██║   ██║   ██║   ██╔══╝  ██║         ██╔═██╗ ██╔══██╗██║╚════██║ ███╔╝     ██║   ██║██╔══██║██║╚██╗██║')
print('██║  ██║╚██████╔╝   ██║   ███████╗███████╗    ██║  ██╗██║  ██║██║███████║███████╗   ██║   ██║██║  ██║██║ ╚████║')
print('╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝')
print()
print()

Menu(hotel).cmdloop()