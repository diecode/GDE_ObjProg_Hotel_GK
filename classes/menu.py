import cmd
import datetime

from classes import utils


class Menu(cmd.Cmd):
    intro = 'Hotel Krisztian - Kérlek gépeld be a \'help\' parancsot vagy egy \'?\' jelet az elérhető parancsok listázásához.'
    prompt = 'Hotel Krisztian cli > '
    file = None

    def __init__(self, hotel):
        super().__init__()
        self.hotel = hotel

    def do_hotel_info(self, arg):
        """ Információkat jelenít meg a Hotel Krisztianról """
        print(f"\t{self.hotel.name}'s address is {self.hotel.zipcode} {self.hotel.city}, {self.hotel.address}")

    def do_szoba_lista(self, arg):
        """ Hotel szobáinak listázása """
        for room in self.hotel.get_rooms():
            room.print_information()

    def do_foglalas(self, arg):
        """ Szoba foglalása.
            Dátumra vonatkozó formátum: YYYY-MM-DD, pl.: 2024-09-09
            Kizárólag olyan jövőbe mutató dátum adható meg ami még nincs foglalva.
        """

        print("Elérhető szobák: ")
        for room in self.hotel.get_rooms():
            room.print_information()

        while True:
            room_number = input("Kérlek add meg a foglaláshoz a szobaszámot: ")

            if not utils.is_number(room_number):
                print("Csak szám megadása lehetséges.")
                continue

            room = self.hotel.get_room_by_room_number(int(room_number))

            if room is None:
                print("Nem található a megadott szobaszám.")
                continue

            break

        while True:
            date = input("Kérlek add meg a foglalás időpontját (Kötelező az alábbi formátum: YYYY-MM-DD, pl.: 2024-09-09): ")

            if not utils.is_correct_date_format(date):
                print("Rossz dátum formátum.")
                continue

            date = datetime.date.fromisoformat(date)

            if date < datetime.date.today():
                print("Nem foglalható a mai napnál korábbi dátum.")
                continue

            if room.is_reserved(date):
                print("A megadott dátumra már van foglalás.")
                continue

            break

        name = input("Kérlek add meg a foglaláshoz a neved: ")
        room.add_reservation(name, date)
        print("Sikeres foglalás az alábbi időpontra: " + str(date))
        room.print_information()

    def do_foglalas_lemondas(self, arg):
        """ Foglalás lemondása.
            Dátumra vonatkozó formátum: YYYY-MM-DD, pl.: 2024-09-09
            Kizárólag olyan jövőbe mutató dátum adható meg ami már foglalva van.
        """
        while True:
            room_number = input("Kérlek add meg a foglalás lemondásához a szobaszámot: ")

            if not utils.is_number(room_number):
                print("Csak szám megadása lehetséges.")
                continue

            room = self.hotel.get_room_by_room_number(int(room_number))

            if room is None:
                print("Nem található a megadott szobaszám.")
                continue

            break

        while True:
            date = input("Kérlek add meg a lemondásra szánt foglalás időpontját (Kötelező az alábbi formátum: YYYY-MM-DD, pl.: 2024-09-09): ")

            if not utils.is_correct_date_format(date):
                print("Rossz dátum formátum.")
                continue

            date = datetime.date.fromisoformat(date)

            if date < datetime.date.today():
                print("Nem lehet a mai napnál korábbi foglalást lemondani.")
                continue

            if not room.is_reserved(date):
                print("A megadott dátumra nincs foglalás.")
                continue

            break

        room.remove_reservation(date)
        print("Sikeres foglalás lemondás: " + str(date))

    def do_foglalas_lista(self, arg):
        """ Foglalások listázása """

        for room in self.hotel.get_rooms():
            print()
            room.print_information()
            print("\t-----------------")
            print("\tFoglalások: ")
            for reservation in room.reservations:
                print(f"\tNév: {reservation.name}, Dátum: {reservation.date}")
            print()

    def do_exit(self, arg):
        """Kilépés a programból. Alternatív parancsok: quit, kilepes"""
        return True

    def do_quit(self, arg):
        """Kilépés a programból. Alternatív parancsok: exit, kilepes"""
        return self.do_exit(arg)

    def do_kilepes(self, arg):
        """Kilépés a programból. Alternatív parancsok: exit, quit"""
        return self.do_exit(arg)