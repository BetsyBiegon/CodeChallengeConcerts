class Band:
    def __init__(self, name, hometown):
        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, new_hometown):
        raise AttributeError("Hometown is immutable")

    def concerts(self):
        return self._concerts

    def venues(self):
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        self._date = date
        self._band = band
        self._venue = venue
        Concert.all.append(self)
        band._concerts.append(self)
        venue._concerts.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, new_date):
        if isinstance(new_date, str) and len(new_date) > 0:
            self._date = new_date
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, new_venue):
        if isinstance(new_venue, Venue):
            self._venue = new_venue
        else:
            raise ValueError("Venue must be a Venue instance")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, new_band):
        if isinstance(new_band, Band):
            self._band = new_band
        else:
            raise ValueError("Band must be a Band instance")

    def hometown_show(self):
        return self._venue.city == self._band.hometown

    def introduction(self):
        return f"Hello {self._venue.city}!!!!! We are {self._band.name} and we're from {self._band.hometown}"


class Venue:
    def __init__(self, name, city):
        self._name = name
        self._city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self._name = new_name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_city):
        if isinstance(new_city, str) and len(new_city) > 0:
            self._city = new_city
        else:
            raise ValueError("City must be a non-empty string")

    def concerts(self):
        return self._concerts

    def bands(self):
        return list(set(concert.band for concert in self._concerts))
