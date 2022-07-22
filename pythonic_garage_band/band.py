
class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return tuple(solos)

class Musician:
    def __init__(self, name):
        self.name = name

class Guitarist(Musician):
    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'


class Bassist(Musician):
    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'
