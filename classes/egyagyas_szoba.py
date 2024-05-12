from classes.szoba import Szoba


class EgyagyasSzoba(Szoba):

    bed_numbers = 1

    def get_room_number(self):
        print(f"{self.room_number}")

    def get_price(self):
        print(f"{self.price}")

    def print_information(self):
        print(f"\tSzoba szám: {self.room_number}, ágyak száma: {self.bed_numbers}, ár: {self.price} HUF/éj")