from named_with_id import NamedWithId

class Location(NamedWithId):
    def __init__(self, id, name, address='',*args, **kwargs):
        self.address = address
        return super().__init__(id, name, *args, **kwargs)

    def __str__(self):
        return 'Location named %s' % (self.name)