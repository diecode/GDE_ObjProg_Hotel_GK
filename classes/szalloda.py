class Szalloda():

    rooms = []

    def __init__(self, name, zipcode, city, address):
        self.name = name

        try:
            self.zipcode = int(zipcode)

            if (len(str(self.zipcode))) != 4:
                raise "Az irányítószámnak 4 számjegyűnek kell lennie."
        except ValueError:
            raise "Az irányítószám csak számokból állhat."

        self.city = city
        self.address = address

    def add_room(self, room):
        if self.get_room_by_room_number(room.room_number) is None:
            self.rooms.append(room)

    def get_rooms(self):
        return self.rooms


    def get_room_by_room_number(self, number):
        for room in self.rooms:
            if room.room_number == number:
                return room
        return None

