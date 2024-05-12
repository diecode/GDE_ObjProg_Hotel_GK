import datetime
from abc import ABC, abstractmethod

from classes import utils
from classes.szalloda import Szalloda
from classes.foglalas import Foglalas


def get_hotel():
    return Szalloda


class Szoba(ABC, Szalloda):

    def __init__(self, room_number, price):
        self.room_number = room_number
        self.price = price
        self.reservations = []

    @abstractmethod
    def get_room_number(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

    def add_reservation(self, name: str, date: datetime):
        self.reservations.append(Foglalas(name, date))

    def remove_reservation(self, date: datetime):
        for reservation in self.reservations:
            if reservation.date == date:
                self.reservations.remove(reservation)
                break

    def is_reserved(self, date: datetime):
        for reservation in self.reservations:
            if reservation.date == date:
                return True
        return False
