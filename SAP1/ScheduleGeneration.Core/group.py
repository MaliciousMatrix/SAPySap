from named_with_id import NamedWithId
class Group(NamedWithId):
    def __init__(self, id, name, *args, **kwargs):
        return super().__init__(id, name, *args, **kwargs)

    def __str__(self):
        return 'Group named %s' % (self.name)
