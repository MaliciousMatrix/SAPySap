from named_with_id import NamedWithId

class Category(NamedWithId):
    def __init__(self, id, name, *args, **kwargs):
        return super().__init__(id, name, *args, **kwargs)

    def __str__(self):
        return 'Category named %s' % (self.name)
