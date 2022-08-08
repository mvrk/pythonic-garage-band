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

    @classmethod
    def to_list(cls):
        return cls.instances

    def __repr__(self):
        return

    def __str__(self):
        return


class Musician:
    def __init__(self, name):
        self.name = name


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "guitar"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'

    def get_instrument(self):
        return self.instrument


class Bassist(Musician):

    def __init__(self, name):
        self.name = name
        self.instrument = "bass"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'
#

class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self.instrument = "drums"

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'
